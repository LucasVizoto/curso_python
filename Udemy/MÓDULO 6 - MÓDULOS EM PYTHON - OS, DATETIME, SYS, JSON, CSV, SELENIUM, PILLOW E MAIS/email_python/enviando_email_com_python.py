#criar no .env um lugar para o email que vai enviar e a senha
# ativar o IMAP no gmail
# criar senha de app
# Eviando emails SMTP com Python

import os
import pathlib
from string import Template
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv #type: ignore

load_dotenv()
#Caminho do arquivo html
CAMINHO_ARQUIVO_HTML = pathlib.Path(__file__).parent / 'email.html'
#dados do remetente e destinatário

remetente = os.getenv('FROM_EMAIL','')

destinatario = remetente

# Configurações do servidor sntp

smtp_server = 'smtp.gmail.com'

smtp_port = 587

smtp_username = os.getenv('FROM_EMAIL','')

smtp_password = os.getenv('EMAIL_PASSWORD','')

with open(CAMINHO_ARQUIVO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Fulano')

# Trasformar mensagem em MIMEMultipart
# Mais ou menos como uma multifatoração dos itens requeridos em um email
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do meu email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# abrir uma conexão smtp (Envia o email)
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() #dando um hello pro servidor
    server.starttls() # iniciando o servidor de forma mais segura
    server.login(smtp_username, smtp_password) #literalmente logando no servidor
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')