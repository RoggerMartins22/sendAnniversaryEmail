import locale
from FunctionsMails.config import CONECTION, PORT, MAIL, MAIL_PASSWORD
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
conexao = CONECTION
porta = PORT
email_de_envio = MAIL
senha = MAIL_PASSWORD

def returnBirthdayStudentEmailBody(nome):
    body = f"""
    <html>
      <body>
        <p>Prezado Aluno <strong>{nome}</strong>,</p>

        <p>Hoje é o seu aniversário e queremos aproveitar esta oportunidade para desejar-lhe um dia fantástico! Parabéns pelo seu dia especial.</p>

        <p>Esperamos que você aproveite este momento para relaxar e se divertir. Continue sendo o excelente aluno que você é e esperamos que este ano traga ainda mais conquistas e sucesso para você.</p>

        <p><strong>Feliz aniversário!</strong></p>

        <p>Atenciosamente,<br>
        Instituto de Ensino e Pesquisa de Goiás - INEPG</p>
        <p><img src="cid:assinatura_inepg" alt="Assinatura INEPG" width="200"></p>
      </body>
    </html>
    """
    return body


def returnBirthdayTeacherEmailBody(nome):
    body = f"""
    <html>
      <body>
        <p>Caro(a) {nome}</strong>,</p>

        <p>Hoje é o seu aniversário e queremos aproveitar esta oportunidade para desejar-lhe um dia fantástico! Parabéns pelo seu dia especial.</p>

        <p>Esperamos que você aproveite este momento para relaxar e se divertir. Continue sendo o excelente profissional que você é e esperamos que este ano traga ainda mais conquistas e sucesso para você.</p>

        <p><strong>Feliz aniversário!</strong></p>

        <p>Atenciosamente,<br>
        Instituto de Ensino e Pesquisa de Goiás - INEPG</p>
        <p><img src="cid:assinatura_inepg" alt="Assinatura INEPG" width="200"></p>
      </body>
    </html>
    """
    return body