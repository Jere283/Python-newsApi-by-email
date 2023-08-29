import smtplib
import ssl
import os

def send_email(rmessage):

    host = 'smtp.gmail.com'
    port = 465
    username = "jeremyfigueroa2021@gmail.com"
    password = os.getenv("GMAILPASS")
    receiver = 'jeremyfigueroa2015@outlook.com'
    context = ssl.create_default_context()

    message = rmessage

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("email was sent")