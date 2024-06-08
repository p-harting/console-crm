from rich import print
from rich.console import Console
from rich.table import Table

from data_manager import DataManager

# Initialize rich console
console = Console()

# Define database location
creds_file = 'creds.json'
spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

# Initialize the data manager
with console.status("[bold green]Connecting to Database...") as status:
    data_manager = DataManager(creds_file, spreadsheet_name, worksheet_name)

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
        print("What would you like to do?")
        table = Table(title="Main Menu")

        table.add_column("Option", justify="left", style="green", no_wrap=True)
        table.add_column("Description", style="green")

        table.add_row("1", "See all contacts")
        table.add_row("2", "Search contact")
        table.add_row("3", "Edit contact")
        table.add_row("4", "Add new contact")
        table.add_row("5", "Delete contact")

        print(table)
        input("> ")
def main():
    app = CRM()
    app.run()

if __name__ == "__main__":
    main()