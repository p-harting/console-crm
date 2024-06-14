import time
import json

from rich import print
from rich.style import Style
from rich.console import Console
from rich.table import Table

from data_manager import DataManager
from validator import Validator
from mail_manager import MailManager

# Initialize rich console
console = Console()

# Define database
creds_file = 'creds.json'
with open(creds_file, 'r') as f:
    creds = json.load(f)

google_sheets_creds = creds.get('google_sheets')
app_password = creds.get('app_password')

spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

# Define styles
error_style = Style(color="red", blink=True, bold=True)
success_style = Style(color="green", blink=True, bold=True)

# Initialize the data manager
with console.status("[bold green]Connecting to Database...") as status:
    data_manager = DataManager(google_sheets_creds, spreadsheet_name,
                               worksheet_name)

with open('ascii_logo.txt', 'r') as file:
    ascii_logo = file.read()

new_customer_description = (
    "Input the data about the new customer.\n"
    "If you don't have the information, you can just use a backslash(/).\n"
    "Required fields are marked with an asterisk(*)."
    )


class CRM:
    def __init__(self):
        """
        Initializes the ConsoleCRM instance and prints a welcome message.
        """
        print("Welcome in your [bold green]ConsoleCRM[/bold green]!")

    def run(self):
        """
        Starts the ConsoleCRM application by displaying the main menu.
        """
        self.main_menu()

    def main_menu(self):
        """
        Displays the main menu, handles user input for various
        customer-related actions, and directs the user to the
        appropriate method based on their choice.
        """
        console.clear()

        print(ascii_logo)

        while True:  # Loop until a valid choice is made
            print("What would you like to do?")
            table = Table(title="Main Menu", width=console.width)

            table.add_column("Option", justify="left", style="green")
            table.add_column("Description", style="green")

            table.add_row("1", "See all customers")
            table.add_row("2", "Search customer")
            table.add_row("3", "Edit customer")
            table.add_row("4", "Add new customer")
            table.add_row("5", "Delete customer")
            table.add_row("6", "Send an email")
            table.add_row("7", "Exit")

            print(table)
            choice = input("> ").strip()

            if choice == '1':
                self.show_all_customers()
            elif choice == '2':
                self.search_customer()
            elif choice == '3':
                self.edit_customer()
            elif choice == '4':
                self.add_new_customer()
            elif choice == '5':
                self.delete_customer()
            elif choice == '6':
                self.send_customer_email()
            elif choice == '7':
                console.print("Exiting the program. Goodbye!")
                return
            else:
                console.print("Invalid choice, please select a valid option.",
                              style=error_style)

    def get_input(self, prompt, validator, error_message, required=False):
        """
        Prompts the user for input, validates the input using a
        provided validator function, and handles errors and
        required fields. Returns the validated input or a default
        value if specified.

        :param prompt: The message to display to the user.
        :param validator: A function to validate the user's input.
        :param error_message: The message to display if the validation fails.
        :param required: A boolean indicating if the input is required.
                                Defaults to False.
        """
        while True:
            console.print(prompt)
            value = input("> ").strip()
            if required and Validator.backslash(value):
                console.clear()
                console.print(new_customer_description)
                console.print(error_message, style=error_style)
            elif not required and Validator.backslash(value):
                return "/"
            elif validator(value):
                return value
            else:
                console.clear()
                console.print(new_customer_description)
                console.print(error_message, style=error_style)

    def get_multiline_input(self, prompt):
        """
        Prompts the user to input multiple lines of text until
        they type 'exit'.
        Returns the concatenated string of all input lines.
        :param prompt: The prompt message to display to the user.
        :return: A string containing the concatenated input lines.
        """
        print(prompt)
        lines = []
        while True:
            line = input()
            if line.strip().lower() == "exit":
                break
            lines.append(line)
        return "\n".join(lines)

    def show_all_customers(self):
        """
        Displays all customers in a formatted table. If no customers are found,
        notifies the user.
        After displaying, waits for user input to return to the main menu.
        """
        console.clear()
        customers = data_manager.get_all_data()
        if customers:
            table = Table(title="All Customers", width=console.width)
            table.add_column("Firstname", justify="left", style="green")
            table.add_column("Lastname", style="green")
            table.add_column("Birthday", style="green")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="green")
            table.add_column("Company", style="green")
            table.add_column("Position", style="green")
            table.add_column("Relation", style="green")

            for contact in customers[1:]:
                table.add_row(contact[1], contact[2], contact[3], contact[4],
                              contact[5], contact[6], contact[7], contact[8])

            console.print(table)
        else:
            console.print("No customers found.", style=error_style)

        input("Press Enter to return to the main menu...")
        self.main_menu()

    def edit_customer(self):
        """
        Allows editing of existing customer information based on ID.
        Displays search results for customer lookup and supports editing
        of various fields. Validates input before updating the record.
        """
        console.clear()
        while True:
            search_query = input("Enter search query: ").strip()
            if (lambda x: Validator.not_empty(x) and
                    Validator.max_length(x))(search_query):
                break
            else:
                console.print("Invalid input. Search query must be between 1 "
                              "and 128 chars!", style=error_style)

        search_results = data_manager.search_customer(search_query)

        fields = ["id", "firstname", "lastname", "birthday", "email", "phone",
                  "company", "position", "relation"]

        required_fields = {"firstname"}

        if search_results:
            search_results_table = Table(title="Search Results",
                                         width=console.width)
            search_results_table.add_column("ID", justify="left",
                                            style="green")
            search_results_table.add_column("Firstname", style="green")
            search_results_table.add_column("Lastname", style="green")
            search_results_table.add_column("Birthday", style="green")
            search_results_table.add_column("Email", style="green")
            search_results_table.add_column("Phone", style="green")
            search_results_table.add_column("Company", style="green")
            search_results_table.add_column("Position", style="green")
            search_results_table.add_column("Relation", style="green")

            for contact in search_results:
                search_results_table.add_row(contact[0], contact[1],
                                             contact[2], contact[3],
                                             contact[4], contact[5],
                                             contact[6], contact[7],
                                             contact[8])

            console.print(search_results_table)

            print("Enter the ID of the customer you want to edit:")
            while True:
                selected_customer_id = input("> ")
                customer_row = data_manager.get_row_by_id(selected_customer_id)

                if customer_row is not None:
                    break
                else:
                    print("Invalid ID. Please try again.")

            while True:
                console.print("Enter the name of the field you want to edit "
                              "or 'save' to save changes:")
                choice = input("> ").strip()
                lowercase_choice = choice.lower()

                if choice.lower() == "save":
                    console.print("Customer updated successfully!",
                                  style=success_style)
                    time.sleep(2)
                    self.main_menu()
                    return
                elif choice.lower() == "id":
                    console.print("Unable to edit ID!", style=error_style)
                    time.sleep(2)
                if lowercase_choice in [field.lower() for field in fields]:
                    field_index = fields.index(lowercase_choice)
                    required = lowercase_choice in required_fields
                    prompt = f"Enter new value for {choice}:"
                    error_message = f"Invalid value for {choice}!"
                    if lowercase_choice == "firstname":
                        def validator(x):
                            return (Validator.not_empty(x) and
                                    Validator.max_length(x))
                        error_message = ("Firstname needs to be between 1 and "
                                         "128 characters!")
                    elif lowercase_choice == "lastname":
                        def validator(x):
                            return (Validator.not_empty(x) and
                                    Validator.max_length(x))
                        error_message = ("Lastname needs to be between 1 and "
                                         "128 characters!")
                    elif lowercase_choice == "birthday":
                        def validator(x):
                            return Validator.validate_dob(x)
                        error_message = ("Please enter a valid date. "
                                         "(Format: YEAR/MONTH/DAY)")
                    elif lowercase_choice == "email":
                        def validator(x):
                            return (Validator.validate_email(x) and
                                    Validator.max_length(x))
                        error_message = "Not a valid Email, please try again!"
                    elif lowercase_choice == "phone":
                        def validator(x):
                            return Validator.validate_phone(x)
                        error_message = ("Please enter a valid phone number. "
                                         "(Format: 123-456-7890)")
                    elif lowercase_choice == "company":
                        def validator(x):
                            return (Validator.not_empty(x) and
                                    Validator.max_length(x))
                        error_message = ("Company needs to be between 1 and "
                                         "128 characters!")
                    elif lowercase_choice == "position":
                        def validator(x):
                            return (Validator.not_empty(x) and
                                    Validator.max_length(x))
                        error_message = ("Position needs to be between 1 and "
                                         "128 characters!")
                    elif lowercase_choice == "relation":
                        def validator(x):
                            return (Validator.not_empty(x) and
                                    Validator.max_length(x))
                        error_message = ("Relation needs to be between 1 and "
                                         "128 characters!")
                    else:
                        def validator(x):
                            return True
                        error_message = ""

                    new_value = self.get_input(prompt, validator,
                                               error_message, required)
                    updated_row = customer_row.copy()
                    updated_row[field_index] = new_value

                    if data_manager.update_row_by_id(selected_customer_id,
                                                     updated_row):
                        console.print("Field updated successfully!",
                                      style=success_style)
                    else:
                        console.print("Failed to update the field!",
                                      style=error_style)
                else:
                    console.print("Invalid choice!", style=error_style)

                time.sleep(2)
        else:
            console.print("No results found for the search query.",
                          style=error_style)
            time.sleep(2)
            self.edit_customer()
            return

    def add_new_customer(self):
        """
        Guides user through adding a new customer with basic details,
        validates inputs, and stores the new customer in the
        data manager. Returns to main menu afterward.
        """
        console.clear()
        console.print(new_customer_description)

        firstname = self.get_input(
            "Firstname*:",
            lambda x: Validator.not_empty(x) and Validator.max_length(x),
            "Firstname needs to be between 1 and 128 characters!",
            required=True
        )

        lastname = self.get_input(
            "Lastname:",
            lambda x: Validator.not_empty(x) and Validator.max_length(x),
            "Lastname needs to be between 1 and 128 characters!"
        )

        dob = self.get_input(
            "Birthday:",
            lambda x: Validator.validate_dob(x) or Validator.backslash(x),
            "Please enter a valid date. (Format: YEAR/MONTH/DAY)"
        )

        email = self.get_input(
            "Email:",
            lambda x: (Validator.validate_email(x) and
                       Validator.max_length(x) or Validator.backslash(x)),
            "Not a valid Email, please try again!"
        )

        phone = self.get_input(
            "Phone:",
            lambda x: Validator.validate_phone(x) or Validator.backslash(x),
            "Please enter a valid phone number. (Format: 123-456-7890)"
        )

        company = self.get_input(
            "Company:",
            lambda x: (Validator.not_empty(x) and
                       Validator.max_length(x) or Validator.backslash(x)),
            "Company needs to be between 1 and 128 characters!"
        )

        position = self.get_input(
            "Position:",
            lambda x: (Validator.not_empty(x) and
                       Validator.max_length(x) or Validator.backslash(x)),
            "Position needs to be between 1 and 128 characters!"
        )

        relation = self.get_input(
            "Relation:",
            lambda x: (Validator.not_empty(x) and
                       Validator.max_length(x) or Validator.backslash(x)),
            "Relation needs to be between 1 and 128 characters!"
        )

        console.clear()
        data_manager.append_row([firstname, lastname, dob, email, phone,
                                 company, position, relation])
        console.print("A new customer was successfully created!",
                      style=success_style)
        time.sleep(2)

        self.main_menu()

    def search_customer(self):
        """
        Allows user to search for customers based on a query input.
        Displays search results in a formatted table if matches are found.
        Returns to the main menu after displaying results.
        """
        console.clear()

        while True:
            search_query = input("Enter search query: ").strip()
            if (lambda x: Validator.not_empty(x) and
                    Validator.max_length(x))(search_query):
                break
            else:
                console.print("Invalid input. Search query must be between 1 "
                              "and 128 chars!", style=error_style)

        search_results = data_manager.search_customer(search_query)

        if search_results:
            table = Table(title="Search Results", width=console.width)
            table.add_column("ID", justify="left", style="green")
            table.add_column("Firstname", style="green")
            table.add_column("Lastname", style="green")
            table.add_column("Birthday", style="green")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="green")
            table.add_column("Company", style="green")
            table.add_column("Position", style="green")
            table.add_column("Relation", style="green")

            for contact in search_results:
                table.add_row(contact[0], contact[1], contact[2], contact[3],
                              contact[4], contact[5], contact[6], contact[7],
                              contact[8])

            console.print(table)
        else:
            print("No matching customers found.")

        input("Press Enter to return to the main menu...")
        self.main_menu()

    def delete_customer(self):
        """
        Allows user to search for and delete a customer based on a query input.
        Displays search results in a table and prompts for confirmation before
        deletion.
        Returns to the main menu after completing the deletion process.
        """
        console.clear()
        search_query = input("Enter search query: ").strip()
        search_results = data_manager.search_customer(search_query)

        if search_results:
            table = Table(title="Search Results", width=console.width)
            table.add_column("ID", justify="left", style="green")
            table.add_column("Firstname", style="green")
            table.add_column("Lastname", style="green")
            table.add_column("Birthday", style="green")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="green")
            table.add_column("Company", style="green")
            table.add_column("Position", style="green")
            table.add_column("Relation", style="green")

            for contact in search_results:
                table.add_row(contact[0], contact[1], contact[2], contact[3],
                              contact[4], contact[5], contact[6], contact[7],
                              contact[8])

            console.print(table)

            print("Enter the ID to delete:")
            deleted_customer_id = input("> ")

            if deleted_customer_id in [result[0] for result in search_results]:
                confirmation = input("Are you sure you want to delete this "
                                     "customer? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    data_manager.delete_row_by_id(deleted_customer_id)
                    console.print("Customer deleted successfully!",
                                  style=success_style)
                elif confirmation == "no":
                    console.print("Customer deletion cancelled.",
                                  style=error_style)
                else:
                    console.print("Invalid input. Deletion cancelled.",
                                  style=error_style)
            else:
                console.print("Invalid ID. Customer deletion cancelled.",
                              style=error_style)
        else:
            print("No matching customers found.")

        input("Press Enter to return to the main menu...")
        self.main_menu()

    def send_customer_email(self):
        """
        Allows user to search for a customer and send an email to the
        selected customer.
        Displays search results in a table and prompts for email details
        (subject and body).
        Sends the email using MailManager and returns to the main menu after
        completion.
        """
        console.clear()
        search_query = input("Enter search query to find customer: ").strip()
        search_results = data_manager.search_customer(search_query)

        if search_results:
            table = Table(title="Search Results", width=console.width)
            table.add_column("ID", justify="left", style="green")
            table.add_column("Firstname", style="green")
            table.add_column("Lastname", style="green")
            table.add_column("Birthday", style="green")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="green")
            table.add_column("Company", style="green")
            table.add_column("Position", style="green")
            table.add_column("Relation", style="green")

            for contact in search_results:
                table.add_row(contact[0], contact[1], contact[2], contact[3],
                              contact[4], contact[5], contact[6], contact[7],
                              contact[8])

            console.print(table)

            print("Enter the ID of the customer you want to email:")
            selected_customer_id = input("> ")

            selected_customer = next(
                (result for result in search_results
                 if result[0] == selected_customer_id), None)

            if selected_customer:
                if selected_customer[4]:
                    receiver_mail = selected_customer[4]
                else:
                    console.print("No email found for this customer!",
                                  style=error_style)
                    input("Press Enter to return to the main menu...")
                    self.main_menu()
                    time.sleep(2)
                    self.main_menu()
                    return
                subject = input("Subject: ")
                message = self.get_multiline_input("Enter the email body. "
                                                   "Write exit to finish:")
                mailer = MailManager()
                mailer.send_mail(receiver_mail, subject, message, app_password)
                console.print("Email sent successfully!", style=success_style)
            else:
                console.print("Invalid ID. Returning to the main menu.",
                              style=error_style)
        else:
            console.print("No matching customers found.", style=error_style)

        input("Press Enter to return to the main menu...")
        self.main_menu()


def main():
    """
    Creates an instance of the CRM application and starts it by calling
    the 'run' method.
    """
    app = CRM()
    app.run()


if __name__ == "__main__":
    main()
