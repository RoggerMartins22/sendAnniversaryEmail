import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from FunctionsMails.infoEmail import conexao, porta, email_de_envio, senha, returnBirthdayStudentEmailBody, returnBirthdayTeacherEmailBody

def sendEmailStudent(nome, email):
        
    server_smtp = conexao
    port = porta
    sender_email = email_de_envio
    password = senha
    receive_email = email
    subject = 'Feliz Aniversário!'
    body = returnBirthdayStudentEmailBody(nome)


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receive_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    with open("FunctionsMails/assinatura.jpg", "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<assinatura_inepg>')
        message.attach(img)

    try:
        server = smtplib.SMTP(server_smtp, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receive_email, message.as_string())
    except Exception:
        print("Erro: Endereço de E-mail Inválido")
    finally:
        server.quit()


def sendEmailTeacher(nome, email):
        
    server_smtp = conexao
    port = porta
    sender_email = email_de_envio
    password = senha
    receive_email = email
    subject = 'Feliz Aniversário!'
    body = returnBirthdayTeacherEmailBody(nome)


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receive_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    with open("FunctionsMails/assinatura.jpg", "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<assinatura_inepg>')
        message.attach(img)

    try:
        server = smtplib.SMTP(server_smtp, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receive_email, message.as_string())
    except Exception:
        print("Erro: Endereço de E-mail Inválido")
    finally:
        server.quit()