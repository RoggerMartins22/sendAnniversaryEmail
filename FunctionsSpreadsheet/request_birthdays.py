import pandas as pd
from datetime import datetime
from FunctionsMails.sendEmail import sendEmailStudent, sendEmailTeacher

def birthday_students():
    df = pd.read_excel("Spreadsheets/alunos_aniversariantes.xlsx")
    df['DataNascimento'] = pd.to_datetime(df['DataNascimento'], dayfirst=True)
    hoje = datetime.now()

    aniversariantes = df[(df['DataNascimento'].dt.month == hoje.month) & (df['DataNascimento'].dt.day == hoje.day)]

    aniversariantes_dict = aniversariantes.to_dict(orient='records')


    if not aniversariantes.empty: 
        for pessoa in aniversariantes_dict:
            nome = pessoa['Nome']
            email = pessoa['Email']
            sendEmailStudent(nome, email)
    else:
        print("Nenhum aniversariante encontrado para o dia de hoje.")

    print("Alunos:")
    for pessoa in aniversariantes_dict:
            print(f"Nome: {pessoa['Nome']}, Email: {pessoa['Email']}")


def birthday_teacher():
    df = pd.read_excel("Spreadsheets/prof_aniversariantes.xlsx")
    df['DataNascimento'] = pd.to_datetime(df['DataNascimento'], dayfirst=True)
    hoje = datetime.now()

    aniversariantes = df[(df['DataNascimento'].dt.month == hoje.month) & (df['DataNascimento'].dt.day == hoje.day)]

    aniversariantes_dict = aniversariantes.to_dict(orient='records')


    if not aniversariantes.empty: 
        for pessoa in aniversariantes_dict:
            nome = pessoa['Nome']
            email = pessoa['Email']
            sendEmailTeacher(nome, email)
    else:
        print("Nenhum aniversariante encontrado para o dia de hoje.")

    print("Professores:")
    for pessoa in aniversariantes_dict:
            print(f"Nome: {pessoa['Nome']}, Email: {pessoa['Email']}")