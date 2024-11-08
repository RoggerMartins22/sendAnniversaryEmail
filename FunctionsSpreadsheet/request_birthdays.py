import pandas as pd
from datetime import datetime
from FunctionsMails.sendEmail import sendEmailStudent, sendEmailTeacher
from FunctionsSpreadsheet.check_shipping_email import check_shipping_today, register_submission
hoje = datetime.now()

def birthday_students():
    df = pd.read_excel("Spreadsheets/alunos_aniversariantes.xlsx")
    df['DataNascimento'] = pd.to_datetime(df['DataNascimento'], dayfirst=True)

    aniversariantes = df[(df['DataNascimento'].dt.month == hoje.month) & (df['DataNascimento'].dt.day == hoje.day)]
    aniversariantes_dict = aniversariantes.to_dict(orient='records')

    if not aniversariantes.empty: 
        for pessoa in aniversariantes_dict:
            nome = pessoa['Nome']
            email = pessoa['Email']
            if not check_shipping_today(email):
                sendEmailStudent(nome, email)

                print("Alunos:")
                for pessoa in aniversariantes_dict:
                    print(f"Nome: {pessoa['Nome']}, Email: {pessoa['Email']}")
                    
                register_submission(email)
            else:
                print("Alunos:")
                print(f"E-mail já enviado para {email} hoje!")
    else:
        print("Alunos:")
        print("Nenhum aniversariante encontrado para o dia de hoje.")

def birthday_teacher():
    df = pd.read_excel("Spreadsheets/prof_aniversariantes.xlsx")
    df['DataNascimento'] = pd.to_datetime(df['DataNascimento'], dayfirst=True)

    aniversariantes = df[(df['DataNascimento'].dt.month == hoje.month) & (df['DataNascimento'].dt.day == hoje.day)]
    aniversariantes_dict = aniversariantes.to_dict(orient='records')

    if not aniversariantes.empty: 
        for pessoa in aniversariantes_dict:
            nome = pessoa['Nome']
            email = pessoa['Email']
            if not check_shipping_today(email):
                sendEmailTeacher(nome, email)

                print("Professores:")
                for pessoa in aniversariantes_dict:
                    print(f"Nome: {pessoa['Nome']}, Email: {pessoa['Email']}")

                register_submission(email)
            else:
                print("Professores:")
                print(f"E-mail já enviado para {email} hoje!")
    else:
        print("Professores:")
        print("Nenhum aniversariante encontrado para o dia de hoje.")