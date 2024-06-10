import time

from rich import print
from rich.style import Style
from rich.console import Console
from rich.table import Table

from data_manager import DataManager
from validator import Validator

# Initialize rich console
console = Console()

# Define database location
creds_file = 'creds.json'
spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

# Define styles
error_style = Style(color="red", blink=True, bold=True)
success_sytle = Style(color="green", blink=True, bold=True)

# Initialize the data manager
with console.status("[bold green]Connecting to Database...") as status:
    data_manager = DataManager(creds_file, spreadsheet_name, worksheet_name)

ascii_logo = """
   _____                      _       _____ _____  __  __ 
  / ____|                    | |     / ____|  __ \|  \/  |
 | |     ___  _ __  ___  ___ | | ___| |    | |__) | \  / |
 | |    / _ \| '_ \/ __|/ _ \| |/ _ \ |    |  _  /| |\/| |
 | |___| (_) | | | \__ \ (_) | |  __/ |____| | \ \| |  | |
  \_____\___/|_| |_|___/\___/|_|\___|\_____|_|  \_\_|  |_|
"""

class CRM:
    def __init__(self):
        # Print welcome message
        print("Welcome in your [bold green]ConsoleCRM[/bold green]!")

    def run(self):
        self.main_menu()

    def main_menu(self):
        """
        Starts the main menu
        """
        console.clear()

        print(ascii_logo)

        print("What would you like to do?")
        table = Table(title="Main Menu")

        table.add_column("Option", justify="left", style="green", no_wrap=True)
        table.add_column("Description", style="green")

        table.add_row("1", "See all customers")
        table.add_row("2", "Search customer")
        table.add_row("3", "Edit customer")
        table.add_row("4", "Add new customer")
        table.add_row("5", "Delete customer")
        table.add_row("6", "Exit")

        print(table)
        choice = input("> ").strip()
            
        if choice == '1':
            self.show_all_customers()
        elif choice == '2':
            self.search_customer()
        elif choice == '4':
            self.add_new_customer()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            return
        else:
            print("[bold red]Invalid choice, please select a valid option.[/bold red]")
    
    def show_all_customers(self):
        """
        Display all customers
        """
        console.clear()
        customers = data_manager.get_all_data()
        if customers:
            table = Table(title="All Customers")
            table.add_column("Firstname", justify="left", style="green")
            table.add_column("Lastname", style="green")
            table.add_column("Birthday", style="green")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="green")
            table.add_column("Company", style="green")
            table.add_column("Position", style="green")
            table.add_column("Relation", style="green")

            for contact in customers[1:]:
                table.add_row(contact[1], contact[2], contact[3], contact[4], contact[5], contact[6], contact[7], contact[8], )

            console.print(table)
        else:
            print("[bold red]No customers found.[/bold red]")

        input("Press Enter to return to the main menu...")
        self.main_menu()

    def add_new_customer(self):
        """
        Add a new customer
        """
        console.clear()
        new_customer_description = '''Input the data about the new customer.
If you don't have the information, you can just use a backslash(/).
Required fields are mark with a asterisk(*).'''
        print(new_customer_description)
        
        # Get and validate firstname
        console.print("Firstname*:")
        firstname = input("> ").strip()
        while Validator.backslash(firstname) == True or Validator.not_empty(firstname) == False or Validator.max_length(firstname) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Firstname needs to be between 1 and 24 characters!", style=error_style)
            console.print("Firstname*:")
            firstname = input("> ").strip()

        console.clear()
        console.print(new_customer_description)

        # Get and validate lastname
        console.print("Lastname:")
        lastname = input("> ").strip()
        while Validator.not_empty(lastname) == False or Validator.max_length(lastname) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Lastname needs to be between 1 and 24 characters!", style=error_style)
            console.print("Lastname:")
            lastname = input("> ").strip()
        if Validator.backslash(lastname) == True:
            lastname = ""
        
        console.clear()
        console.print(new_customer_description)

        # Get and validate dob
        console.print("Birthday:")
        dob = input("> ").strip()
        while Validator.validate_dob(dob) == False and Validator.backslash(dob) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Please enter a valide date. (Format: YEAR/MONTH/DAY)", style=error_style)
            console.print("Birthday:")
            dob = input("> ").strip()
        if Validator.backslash(dob) == True:
            dob = ""

        console.clear()
        console.print(new_customer_description)

        # Get and validate email
        console.print("Email:")
        email = input("> ").strip()
        while Validator.backslash(email) == False and (Validator.validate_email(email) == False or Validator.max_length(email) == False):
            console.clear()
            console.print(new_customer_description)
            console.print("Not a valid Email, please try again!", style=error_style)
            console.print("Email:")
            email = input("> ").strip()
        if Validator.backslash(email) == True:
            email = ""
        
        console.clear()
        console.print(new_customer_description)

        # Get and validate phone
        console.print("Phone:")
        phone = input("> ").strip()
        while Validator.validate_phone(phone) == False and Validator.backslash(phone) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Please enter a valide phonenumber. (Format: 123-456-7890)", style=error_style)
            console.print("Phone:")
            phone = input("> ").strip()
        if Validator.backslash(phone) == True:
            phone = ""

        console.clear()
        console.print(new_customer_description)

        # Get and validate company
        console.print("Company:")
        company = input("> ").strip()
        while Validator.not_empty(company) == False or Validator.max_length(company) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Company needs to be between 1 and 24 characters!", style=error_style)
            console.print("Company:")
            company = input("> ").strip()
        if Validator.backslash(company) == True:
            company = ""

        console.clear()
        console.print(new_customer_description)

        # Get and validate position
        print("Position:")
        position = input("> ").strip()
        while Validator.not_empty(position) == False or Validator.max_length(position) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Position needs to be between 1 and 24 characters!", style=error_style)
            console.print("Position:")
            company = input("> ").strip()
        if Validator.backslash(position) == True:
            position = ""

        console.clear()
        console.print(new_customer_description)

        # Get and validate relation
        console.print("Relation:")
        relation = input("> ").strip()
        while Validator.not_empty(relation) == False or Validator.max_length(relation) == False:
            console.clear()
            console.print(new_customer_description)
            console.print("Relation needs to be between 1 and 24 characters!", style=error_style)
            console.print("Relation:")
            relation = input("> ").strip()
        if Validator.backslash(relation) == True:
            relation = ""

        console.clear()

        data_manager.append_row([firstname, lastname, dob, email, phone, company, position, relation])
        console.print("A new customer was successfully created!", style=success_sytle)
        time.sleep(2)

        self.main_menu()
    
    def search_customer(self):
        console.clear()
        search_query = input("Enter search query: ").strip()
        search_results = data_manager.search_customer(search_query)

        if search_results:
            table = Table(title="Search Results")
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
                table.add_row(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5], contact[6], contact[7], contact[8])

            console.print(table)
        else:
            print("No matching customers found.")

        input("Press Enter to return to the main menu...")
        self.main_menu()

def main():
    app = CRM()
    app.run()

if __name__ == "__main__":
    main()