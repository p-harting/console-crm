from data_manager import DataManager
import time

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
append_data = ['Example', 'Example', '2000-01-01', 'example@example.com', '000-000-0000', 'Example', 'Example', 'Example']
data_manager.append_row(append_data)

# Delete row by row number
data_manager.delete_row(2)

# Delete row by id
data_manager.delete_row_by_id(1)