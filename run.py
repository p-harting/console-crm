from data_manager import DataManager

# Initialize the data manager
creds_file = 'creds.json'
spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

data_manager = DataManager(creds_file, spreadsheet_name, worksheet_name)

# Get all data and print it
data = data_manager.get_all_data()
print(data)
