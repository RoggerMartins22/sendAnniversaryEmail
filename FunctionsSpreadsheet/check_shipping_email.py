import pandas as pd
from datetime import datetime

def check_shipping_today(email):

    hoje = datetime.now().date()
    log_df = pd.read_excel('Spreadsheets/enviados.xlsx')
    
    log_df["DataEnvio"] = pd.to_datetime(log_df["DataEnvio"]).dt.date
    return ((log_df["Email"] == email) & (log_df["DataEnvio"] == hoje)).any()

def register_submission(email):

    hoje = datetime.now().date()
    diretorio = ('Spreadsheets/enviados.xlsx')
    
    log_df = pd.read_excel(diretorio)
    novo_registro = pd.DataFrame({"Email": [email], "DataEnvio": [hoje]})
    log_df = pd.concat([log_df, novo_registro], ignore_index=True)
    
    log_df.to_excel(diretorio, index=False)