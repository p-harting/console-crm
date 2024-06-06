from data_manager import DataManager

# Initialize the data manager
creds_file = 'creds.json'
spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

data_manager = DataManager(creds_file, spreadsheet_name, worksheet_name)

class CRM:
    def __init__(self):
        data = data_manager.get_all_data()
        print(data)

    def run(self):
        print('hello world')

def main():
    app = CRM()
    app.run()

if __name__ == "__main__":
    main()