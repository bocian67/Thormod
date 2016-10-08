#Special Thanks to 'rosettacode.org'
import smtplib

def sending(email,subject,message,password,smtp_server):
    header  = 'From: %s\n' % email
    header += 'To: %s\n' % ','.join(email)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.login(email,password)
    problems = server.sendmail(email,email, message)
    server.quit()
    return problems
