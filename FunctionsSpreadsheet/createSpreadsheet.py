import pandas as pd
import os

def verify_spreadsheet_exists():
    if not os.path.exists('aniversarios.xlsx'):
        generate_spreadsheet()
    else:
        print("A planilha já existe. Nenhuma ação necessária.")

def generate_spreadsheet():
    dados_vazios = {
        'Nome': [],
        'Email': [],
        'DataNascimento': []
    }

    df = pd.DataFrame(dados_vazios)
    df.to_excel('aniversarios.xlsx', index=False)
    print("Planilha criada com sucesso!")
