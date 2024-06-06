from data_manager import DataManager

# Initialize the data manager
creds_file = 'creds.json'
spreadsheet_name = 'crm_data'
worksheet_name = 'contacts'

data_manager = DataManager(creds_file, spreadsheet_name, worksheet_name)

# Get all data
data = data_manager.get_all_data()
print(data)

# Get row by row number
row_data = data_manager.get_row(2)
print(row_data)

# Get row by id
row_data = data_manager.get_row_by_id(1)
print(row_data)

# Append data to end
append_data = ['John', 'Smith', '1985-02-14', 'john.smith@example.com', '555-123-4567', 'Acme Corp', 'Sales Manager', 'Lead']
data_manager.append_row(append_data)