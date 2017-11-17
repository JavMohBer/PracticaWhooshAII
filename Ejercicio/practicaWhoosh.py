#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from bs4 import BeautifulSoup
from pip._vendor import requests
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, DATETIME, NUMERIC
from whoosh.qparser import QueryParser
import os

def sopa():
    req = requests.get("http://www.marca.com/futbol/primera-division/calendario.html")
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')

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
            jornadas.append(unicode(a.span.h2.string))
        for l in local:
            locales.append(unicode(l.string))
        for v in visitante:
            visitantes.append(unicode(v.string))
        for r in resultado:
            resultados.append(unicode(r.string))
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
                autores.append(unicode(au.string))
            for t in titular:
                if t.h4 is not None:
                    titulares.append(unicode(t.h4.string))
                elif t.h4 is None:
                    titulares.append("")
                titulos.append(unicode(t.h3.string))
            for t2 in texto:
                textos.append(unicode(t2.find_all("p")))
    return jornadas, locales, visitantes, resultados, fechas, autores, titulares, titulos, textos

def crear_ficheros():
    jornadas, locales, visitantes, resultados, fechas, autores, titulares, titulos, textos= sopa()
    for i in range(0,3):
        f = open("Jornada" + str(i) + ".txt", "w")
        f.write(jornadas[i].encode('ascii', 'ignore'))
        f.write(locales[i].encode('ascii', 'ignore'))
        f.write(visitantes[i].encode('ascii', 'ignore'))
        f.write(resultados[i].encode('ascii', 'ignore'))
        f.write(fechas[i].encode('ascii', 'ignore'))
        f.write(autores[i].encode('ascii', 'ignore'))
        f.write(titulares[i].encode('ascii', 'ignore'))
        f.write(titulos[i].encode('ascii', 'ignore'))
        f.write(textos[i].encode('ascii', 'ignore'))


def get_schema():
    return Schema(numJornada=NUMERIC(stored=True), equipoLocal=TEXT(stored=True), equipoVisitante=TEXT(stored=True),
                  resultado=TEXT(stored=True), fecha=DATETIME(stored=True), autor=TEXT(stored=True),
                  titular=TEXT(stored=True), texto=TEXT(stored=True))
def crearIndice():
    dirdocs = ""
    dirindex = ""
    if not os.path.exists(dirdocs):
        os.mkdir(dirdocs)
    else:
        if not os.path.exists(dirindex):
            os.mkdir(dirindex)

    ix = create_in(dirindex, schema=get_schema())
    writer = ix.writer()

    writer.commit()

def entryNoticia():
    entryNoticiaTop = tk.Tk()

    labelNoticia = tk.Label(entryNoticiaTop, text="Noticia")
    labelNoticia.pack()

    entry = tk.Entry(entryNoticiaTop)
    entry.pack()

    def buscarPorNoticia():
        ventanaNoticias = tk.Tk()

        listaPorNoticias = tk.Listbox(ventanaNoticias)
        #HAY QUE BORRAR
        listaPorNoticias.insert(1, "Hola1")
        listaPorNoticias.insert(2, "Hola2")
        listaPorNoticias.pack()

        ventanaNoticias.mainloop()

    buscar = tk.Button(entryNoticiaTop, text="Buscar", command=buscarPorNoticia)
    buscar.pack()

    entryNoticiaTop.mainloop()

def entryFecha():
    entryFechaTop = tk.Tk()

    labelFecha = tk.Label(entryFechaTop, text="Fecha")
    labelFecha.pack()

    entry = tk.Entry(entryFechaTop)
    entry.pack()

    def buscarPorFecha():
        ventanaFechas = tk.Tk()

        listaPorFechas = tk.Listbox(ventanaFechas)
        # HAY QUE BORRAR
        listaPorFechas.insert(1, "Hola1")
        listaPorFechas.insert(2, "Hola2")
        listaPorFechas.pack()

        ventanaFechas.mainloop()

    buscar = tk.Button(entryFechaTop, text="Buscar", command=buscarPorFecha)
    buscar.pack()

    entryFechaTop.mainloop()

def spinboxAutor():
    spinboxAutorTop = tk.Tk()
    # HAY QUE BORRAR
    listaAux = ["autor1", "autor2", "autor3", "autor4", "autor5"]

    labelAutores = tk.Label(spinboxAutorTop, text="Autores")
    labelAutores.pack()

    spinbox = tk.Spinbox(spinboxAutorTop, values=listaAux)
    spinbox.pack()

def ventana():
    top = tk.Tk()

    datos = tk.Menubutton(top, text="Datos")
    datos.menu = tk.Menu(datos, tearoff=0)
    datos["menu"] = datos.menu
    datos.grid(row=0, column=0)

    datos.menu.add_command(label="Cargar", command=crear_ficheros)
    datos.menu.add_command(label="Salir", command=top.quit)

    buscar = tk.Menubutton(top, text="Buscar")
    buscar.menu = tk.Menu(buscar, tearoff=0)
    buscar["menu"] = buscar.menu
    buscar.grid(row=0, column=1)

    buscar.menu.add_command(label="Noticia", command=entryNoticia)
    buscar.menu.add_command(label="Fecha", command=entryFecha)
    buscar.menu.add_command(label="Autor", command=spinboxAutor)

    top.mainloop()

if __name__ == '__main__':
    ventana()