import pandas as pd
import os

def verify_folder():
    if not os.path.exists('Spreadsheets'):
        try:
            os.makedirs('Spreadsheets', exist_ok=True)
            print(f"Pasta '{'Spreadsheets'}' criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar a pasta: {e}")

def verify_spreadsheet_exists():
    if not os.path.exists('Spreadsheets/alunos_aniversariantes.xlsx') and not os.path.exists('Spreadsheets/prof_aniversariantes.xlsx'):
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
    df.to_excel('Spreadsheets/alunos_aniversariantes.xlsx', index=False)
    df.to_excel('Spreadsheets/prof_aniversariantes.xlsx', index=False)
    print("Planilhas criadas com sucesso!")

def create_log_if_not_exist():
    try:
        pd.read_excel('Spreadsheets/enviados.xlsx')
    except FileNotFoundError:
        dados_vazios = {
            'Email': [],
            'DataEnvio': []
        }
        log_df = pd.DataFrame(dados_vazios)
        log_df.to_excel('Spreadsheets/enviados.xlsx', index=False)