import gspread
from google.oauth2.service_account import Credentials

class DataManager:
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    def __init__(self, google_sheets_creds, spreadsheet_name, worksheet_name):
        """
        Initializes the DataManager instance with Google Sheets credentials,
        and opens the specified spreadsheet and worksheet.

        :param google_sheets_creds: Service account credentials for Google Sheets API.
        :param spreadsheet_name: Name of the Google Sheets spreadsheet.
        :param worksheet_name: Name of the worksheet within the spreadsheet.
        """
        self.creds = Credentials.from_service_account_info(google_sheets_creds)
        self.scoped_creds = self.creds.with_scopes(self.SCOPE)
        self.client = gspread.authorize(self.scoped_creds)
        self.sheet = self.client.open(spreadsheet_name)
        self.worksheet = self.sheet.worksheet(worksheet_name)
    
    def get_all_data(self):
        """
        Retrieve all data from the worksheet.

        :return: A list of lists representing all data rows in the worksheet.
        """
        return self.worksheet.get_all_values()
    
    def get_row(self, row_index):
        """
        Retrieve data from a specific row.

        :param row_index: Index of the row to retrieve.

        :return: A list representing the data in the specified row.
        """
        return self.worksheet.row_values(row_index)
    
    def get_row_by_id(self, id):
        """
        Retrieve a row by its ID.

        :param id: ID of the row to retrieve.

        :return: A list representing the data in the row with the specified ID,
                 or None if the ID is not found.
        """
        id_col = self.worksheet.col_values(1)
        try:
            row_index = id_col.index(str(id)) + 1
            return self.get_row(row_index)
        except ValueError:
            return None

    def append_row(self, values):
        """
        Append a new row to the worksheet.

        :param values: A list of values to append as a new row.
        """
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
        """
        Delete a row by its index.

        :param row_index: Index of the row to delete.
        """
        self.worksheet.delete_rows(row_index)

    def delete_row_by_id(self, id):
        """
        Delete a row by its ID.

        :param id: ID of the row to delete.

        :return: True if the row was successfully deleted, False otherwise.
        """
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

        :param query: The search query string.

        :return: A list of lists representing rows that match the search query.
        """
        all_data = self.get_all_data()
        search_results = []

        for row in all_data:
            if any(query.lower() in column.lower() for column in row):
                search_results.append(row)

        return search_results
    
    def update_row_by_id(self, id, new_values):
        """
        Update a row by its ID with new values.

        :param id: ID of the row to update.
        :param new_values: A list of new values to update the row with.

        :return: True if the row was successfully updated, False otherwise.
        """
        id_col = self.worksheet.col_values(1)
        try:
            row_index = id_col.index(str(id)) + 1
            values_to_update = [new_values]
            self.worksheet.update(f'A{row_index}', values_to_update)
            return True
        except ValueError:
            return False

