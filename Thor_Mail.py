import smtplib
from email.mime.text import MIMEText

def sending(email,password,subject,message,smtp_server):
    header  = 'From: %s\n' % email
    header += 'To: %s\n' % email
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtp_server)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    errors = server.sendmail(email,email, message)
    server.close()
    return errors

eror = sending('wladi.schneider13@googlemail.com','139197713','test123','test from thor123','smtp.gmail.com:587')
print eror
