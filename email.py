# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import smtplib
from time import sleep
sender = "SEU EMAIL"
print("Programa para enviar e-mail")
receiver = input("\033[36mDigite o email destinatário:\033[m ")
password = "SENHA"
subject = str.encode(input ("\033[36mEscreva o assunto do e-mail (não utilize acentos):\033[m "))
body = str.encode(input( """\033[36mDigite o corpo do e-mail (Não utilize acentos e não use ENTER):\033[m\n"""))
# header
message = f"""From: REMETENTE{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender,password)
    print("\033[35mConectando na conta...\033[m")
    server.sendmail(sender, receiver, message)
    sleep(3)
    print("🤘 \033[1;32mEmail enviado com sucesso!\033[m")
except smtplib.SMTPAuthenticationError:
    print("\033[1;31mNão foi possível fazer a autenticação")
    
