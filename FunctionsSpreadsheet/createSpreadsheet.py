import pandas as pd
import os

def verify_spreadsheet_exists():
    if not os.path.exists('alunos_aniversariantes.xlsx') and  not os.path.exists('prof_aniversariantes.xlsx'):
        generate_spreadsheet()
    else:
        print("As planilhas já existem. Nenhuma ação necessária.")

def generate_spreadsheet():
    dados_vazios = {
        'Nome': [],
        'Email': [],
        'DataNascimento': []
    }

    df = pd.DataFrame(dados_vazios)
    df.to_excel('alunos_aniversariantes.xlsx', index=False)
    df.to_excel('prof_aniversariantes.xlsx', index=False)
    print("Planilhas criadas com sucesso!")
