#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pip._vendor import requests

# f = open("", "w")
#
# f.write()
#
# f.close()

req = requests.get("https://foros.derecho.com/foro/20-Derecho-Civil-General")
data = req.text
soup = BeautifulSoup(data,'html.parser')

elementos = soup.find_all("div", {"class": ["rating", "nonsticky"]})

for elemento in elementos:
    aux = elemento.find_all("h3", {"class": "threadtitle"})
    aux2 = elemento.find_all("div", {"class": "author"})
    aux3 = elemento.find_all("a", {"class": "understate"})
    aux4 = elemento.find_all("ul", {"class": ["threadingstate", "td", "alt"]})
    for a in aux:
        print (a.a.string)
        print ("https://foros.derecho.com/" + a.a.get("href"))
    for a2 in aux2:
        print (a2.span.a.string)
        print ("https://foros.derecho.com/" + a2.a.get("href"))
        print (a2.span.a.get("title").split(",")[-1])
    for a3 in aux3:
        try:
            if a3.string.isdigit():
                print ("Respuestas : " + a3.string)
                url_respuestas = requests.get("https://foros.derecho.com/" + a3.get("href"))
                soup2 = BeautifulSoup(url_respuestas, "html.parser")
                elementos2 = soup2.find_all("ul", {"class": ["posterlist"]})
                for e2 in elementos2:
                    print (e2)


        except Exception as e:
            pass
    for a4 in aux4:
        try:
            li = a4.find_all("li")
            print ("Visitas : " + li[1].string.split(":")[-1])
        except Exception as e:
            pass
