import os
from FunctionsSpreadsheet.createSpreadsheet import verify_spreadsheet_exists, verify_folder
from FunctionsSpreadsheet.request_birthdays import birthday_students, birthday_teacher
from FunctionsSpreadsheet.createSpreadsheet import create_log_if_not_exist
os.system("cls")
verify_folder()
verify_spreadsheet_exists()
create_log_if_not_exist()

if __name__ == "__main__":
    birthday_students()
    birthday_teacher()