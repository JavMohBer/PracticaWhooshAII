#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
#import bs4

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

    datos.menu.add_command(label="Cargar")
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