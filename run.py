from rich import print
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
        print("Input the data about the new customer. (If you don't have the information, you can just leave the field empty)")

        print("Firstname:")
        firstname = input("> ").strip()
        print("Lastname:")
        lastname = input("> ").strip()
        print("Birthday:")
        dob = input("> ").strip()
        print("Email:")
        email = input("> ").strip()
        print("Phone:")
        phone = input("> ").strip()
        print("Company:")
        company = input("> ").strip()
        print("Position:")
        position = input("> ").strip()
        print("Relation:")
        relation = input("> ").strip()

        data_manager.append_row([firstname, lastname, dob, email, phone, company, position, relation])

        self.main_menu()

def main():
    app = CRM()
    app.run()

if __name__ == "__main__":
    main()