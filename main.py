import os
from FunctionsSpreadsheet.createSpreadsheet import verify_spreadsheet_exists, verify_folder
from FunctionsSpreadsheet.request_birthdays import birthday_students, birthday_teacher
os.system("cls")
verify_folder()
verify_spreadsheet_exists()

if __name__ == "__main__":
    birthday_students()
    birthday_teacher()