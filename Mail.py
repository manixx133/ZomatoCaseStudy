import smtplib, ssl, sys

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "geeshonline@gmail.com"
receiver_email = "geeshonline@gmail.com"
password = "rxwuppocjvwihuta"
message = """\
Subject: SSIS Package fail notification!

We have got an error in package: """+sys.argv[1]

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
