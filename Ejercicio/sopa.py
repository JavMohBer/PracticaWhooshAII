#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from pip._vendor import requests
import datetime

# f = open("", "w")
#
# f.write()
#
# f.close()

req = requests.get("http://www.marca.com/futbol/primera-division/calendario.html")
data = req.text
soup = BeautifulSoup(data,'html.parser')

elementos = soup.find_all("ul", {"class": ["contenedor-calendario"]})

jornadas = []
locales = []
visitantes = []
resultados = []
fechas = []
autores = []
titulares = []
titulos = []
textos = []
for elemento in elementos:
    aux = elemento.find_all("li", {"id": "contenedorCalendarioInt"})
    local = elemento.find_all("span", {"class": ["local", "equipo"]})
    visitante = elemento.find_all("span", {"class": ["visitante", "equipo"]})
    resultado = elemento.find_all("span", {"class": ["resultado"]})
    href = elemento.find_all("a", {"class": "final"})
    for a in aux:
        jornadas.append(a.span.h2.string)
    for l in local:
        locales.append(l.string)
    for v in visitante:
        visitantes.append(v.string)
    for r in resultado:
        resultados.append(r.string)
    for h in href:
        req2 = requests.get(h.get("href"))
        data2 = req2.text
        soup2 = BeautifulSoup(data2, 'html.parser')

        fecha = soup2.find_all("span", {"class": "fecha"})
        autor = soup2.find_all("span", {"class": "nombre"})
        titular = soup2.find_all("section", {"class": "columnaTitular"})
        texto = soup2.find_all("div", {"class": "cuerpo_articulo"})
        for f in fecha:
            fechas.append(f.text.split("-")[0])
            # list =  f.p.text.split(" ")[2:]
            # fech =''.join(str(e) for e in list )
            # print list
        for au in autor:
            autores.append(au.string)
        for t in titular:
            titulares.append(t.h4.string)
            titulos.append(t.h3.string)
        for t2 in texto:
            textos.append(t2.find_all("p"))







    # aux2 = elemento.find_all("div", {"class": "author"})
    # aux3 = elemento.find_all("a", {"class": "understate"})
    # aux4 = elemento.find_all("ul", {"class": ["threadingstate", "td", "alt"]})
    # for a in aux:
    #     print (a.a.string)
    #     print ("https://foros.derecho.com/" + a.a.get("href"))
    # for a2 in aux2:
    #     print (a2.span.a.string)
    #     print ("https://foros.derecho.com/" + a2.a.get("href"))
    #     print (a2.span.a.get("title").split(",")[-1])
    # for a3 in aux3:
    #     try:
    #         if a3.string.isdigit():
    #             print ("Respuestas : " + a3.string)
    #             url_respuestas = requests.get("https://foros.derecho.com/" + a3.get("href"))
    #             soup2 = BeautifulSoup(url_respuestas, "html.parser")
    #             elementos2 = soup2.find_all("ul", {"class": ["posterlist"]})
    #             for e2 in elementos2:
    #                 print (e2)
    #
    #
    #     except Exception as e:
    #         pass
    # for a4 in aux4:
    #     try:
    #         li = a4.find_all("li")
    #         print ("Visitas : " + li[1].string.split(":")[-1])
    #     except Exception as e:
    #         pass
