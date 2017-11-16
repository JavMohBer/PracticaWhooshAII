#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

def ventana():
    top = tk.Tk()

    inicio = tk.Menubutton(top, text="Inicio")
    inicio.menu = tk.Menu(inicio, tearoff=0)
    inicio["menu"] = inicio.menu
    inicio.grid(row=0, column=0)

    inicio.menu.add_command(label="Indexar")
    inicio.menu.add_command(label="Salir", command=top.quit)

    temas = tk.Menubutton(top, text="Temas")
    temas.menu = tk.Menu(temas, tearoff=0)
    temas["menu"] = temas.menu
    temas.menu.add_command(label="Título")
    temas.menu.add_command(label="Autor")

    respuestas = tk.Menubutton(top, text="Respuestas")
    respuestas.menu = tk.Menu(respuestas, tearoff=0)
    respuestas["menu"] = respuestas.menu
    respuestas.menu.add_command(label="Texto")

    buscar = tk.Menubutton(top, text="Buscar")
    buscar.menu = tk.Menu(buscar, tearoff=0)
    buscar["menu"] = buscar.menu
    buscar.grid(row=0, column=1)
    buscar.menu.add_cascade(label="Temas", menu=temas.menu)
    buscar.menu.add_cascade(label="Respuestas", menu=respuestas.menu)

    top.mainloop()

if __name__ == '__main__':
    ventana()