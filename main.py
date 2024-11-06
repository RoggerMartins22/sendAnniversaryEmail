import pandas as pd
import os
from datetime import datetime
from FunctionsSpreadsheet.createSpreadsheet import verify_spreadsheet_exists
from FunctionsMails.sendEmail import sendEmail
os.system("cls")
verify_spreadsheet_exists()

df = pd.read_excel("aniversarios.xlsx")
df['DataNascimento'] = pd.to_datetime(df['DataNascimento'], dayfirst=True)
hoje = datetime.now()

aniversariantes = df[(df['DataNascimento'].dt.month == hoje.month) & (df['DataNascimento'].dt.day == hoje.day)]

aniversariantes_dict = aniversariantes.to_dict(orient='records')


if not aniversariantes.empty: 
    for pessoa in aniversariantes_dict:
        nome = pessoa['Nome']
        email = pessoa['Email']
        sendEmail(nome, email)
else:
    print("Nenhum aniversariante encontrado para o dia de hoje.")

for pessoa in aniversariantes_dict:
        print(f"Nome: {pessoa['Nome']}, Email: {pessoa['Email']}")