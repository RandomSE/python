import smtplib
# this seems like it could be used for malicious purposes for sure

sender = "cheesus1232@gmail.com"
receiver = "cheesus1232@gmail.com"  # unnecessary to have 2 variables as sender = receiver but eh
password = "wiwb opjk atnj vqgo"  # app password. linked to sender, to change one must change both.
subject = "simple test"
body = "it better work."  # simplified because


# header
message = f""" From: Python user {sender}
To: {receiver}
Subject: {subject}\n
Body: {body} 
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:
    server.login(sender, password)
    print("logged in")
    server.sendmail(sender, receiver, message)
    print("Email has been sent.")
except smtplib.SMTPAuthenticationError:
    print("You need to create an app password for the account, and then put that in password slot.")
