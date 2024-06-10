import gspread
from google.oauth2.service_account import Credentials

class DataManager:
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    def __init__(self, creds_file, spreadsheet_name, worksheet_name):
        self.creds = Credentials.from_service_account_file(creds_file)
        self.scoped_creds = self.creds.with_scopes(self.SCOPE)
        self.client = gspread.authorize(self.scoped_creds)
        self.sheet = self.client.open(spreadsheet_name)
        self.worksheet = self.sheet.worksheet(worksheet_name)
    
    def get_all_data(self):
        return self.worksheet.get_all_values()
    
    def get_row(self, row_index):
        return self.worksheet.row_values(row_index)
    
    def get_row_by_id(self, id):
        id_col = self.worksheet.col_values(1)
        try:
            row_index = id_col.index(str(id)) + 1
            return self.get_row(row_index)
        except ValueError:
            return None

    def append_row(self, values):
        id_col = self.worksheet.col_values(1)
        if id_col:
            try:
                last_id = int(id_col[-1])
            except ValueError:
                last_id = int(id_col[-2]) if len(id_col) > 1 else 0
        else:
            last_id = 0
        
        next_id = last_id + 1
        new_row = [next_id] + values
        self.worksheet.append_row(new_row)

    def delete_row(self, row_index):
        self.worksheet.delete_rows(row_index)

    def delete_row_by_id(self, id):
        id_col = self.worksheet.col_values(1)
        try:
            row_index = id_col.index(str(id)) + 1
            self.delete_row(row_index)
            return True
        except ValueError:
            return False
        
    def search_customer(self, query):
        """
        Search for customers based on a query.
        """
        all_data = self.get_all_data()
        search_results = []

        for row in all_data:
            if any(query.lower() in column.lower() for column in row):
                search_results.append(row)

        return search_results

