import pygsheets
import pandas as pd

# Authenticate and open the Google Sheet
def open_google_sheet(credentials_file, sheet_title, worksheet_title):
    gc = pygsheets.authorize(service_file=credentials_file)
    sheet = gc.open(sheet_title)
    worksheet = sheet.worksheet_by_title(worksheet_title)
    return worksheet

# Read data from a worksheet
def read_worksheet(worksheet):
    return worksheet.get_as_df()

# Write data to a worksheet
def write_to_worksheet(worksheet, data, start='A1', index=False, header=True):
    worksheet.set_dataframe(pd.DataFrame(data), start=start, copy_index=index, copy_head=header)

# Example usage:
if __name__ == "__main__":
    # Replace with your own credentials JSON file
    credentials_file = 'mysheetsproject-403806-bc33bf8cbaeb.json'
    
    # Replace with your Google Sheet and worksheet titles
    sheet_title = 'MyNewSheets'
    worksheet_title = 'Sheet1'
    
    worksheet = open_google_sheet(credentials_file, sheet_title, worksheet_title)

    # Example: Write data to the worksheet
    data_to_write = [
        ['Name', 'Age', 'City'],
        ['Alice', 28, 'New York'],
        ['Bob', 32, 'Los Angeles'],
        ['Charlie', 22, 'Chicago'],
        ['David', 29, 'San Francisco']
    ]

    # data_to_write = your_data_here
    write_to_worksheet(worksheet, data_to_write)
    print('Data write to sheets successfull')
    # Don't forget to save your changes:

    # Read data from the worksheet
    data = read_worksheet(worksheet)
    print("Data from Google Sheet:")
    print(data)
    worksheet.sync()
