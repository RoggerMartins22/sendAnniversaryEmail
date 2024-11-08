import pandas as pd
from datetime import datetime
from FunctionsSpreadsheet.createSpreadsheet import create_log_if_not_exist

def check_shipping_today(email):
    create_log_if_not_exist()

    hoje = datetime.now().date()
    log_df = pd.read_excel('Spreadsheets/enviados.xlsx')
    
    log_df["DataEnvio"] = pd.to_datetime(log_df["DataEnvio"]).dt.date
    return ((log_df["Email"] == email) & (log_df["DataEnvio"] == hoje)).any()

def register_submission(email):

    hoje = datetime.now().date()
    novo_registro = pd.DataFrame({"Email": [email], "DataEnvio": [hoje]})
    novo_registro.to_excel('Spreadsheets/enviados.xlsx', index=False)