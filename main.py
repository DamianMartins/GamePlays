import tkinter as tk
from tkinter import *

root = Tk()


def abrir_ventana_juegos(nombres):
    juegos_ventana = Toplevel()
    juegos_ventana.title("Menú de juegos")
    etiqueta_juegos = Label(juegos_ventana, text="Seleccione un juego para los usuarios {}:".format(", ".join(nombres)))
    etiqueta_juegos.pack()
    lista_juegos = Listbox(juegos_ventana)
    lista_juegos.pack()
    lista_juegos.insert(END, "Preguntados")
    lista_juegos.insert(END, "Karaoke")
    lista_juegos.insert(END, "Ponele la cola al burro")
    lista_juegos.insert(END, "Adivina la pelicula")
    boton_aceptar = Button(juegos_ventana, text="Aceptar")
    boton_aceptar.pack()
    juegos_ventana.mainloop()

def abrir_ventana_nombres(cantidad):
    nombres_ventana = Toplevel()
    nombres_ventana.title("Nombres de los usuarios")
    etiqueta_nombres = Label(nombres_ventana, text="Ingrese los nombres de los usuarios:")
    etiqueta_nombres.pack()
    nombres = []
    for i in range(cantidad):
        etiqueta_nombre = Label(nombres_ventana, text="Usuario {}:".format(i+1))
        etiqueta_nombre.pack()
        entrada_nombre = Entry(nombres_ventana)
        entrada_nombre.pack()
        nombres.append(entrada_nombre.get())
    boton_aceptar = Button(nombres_ventana, text="Aceptar", command=lambda: abrir_ventana_juegos(nombres))
    boton_aceptar.pack()
    nombres_ventana.mainloop()

def abrir_ventana_cantidad():
    cantidad_ventana = Toplevel()
    cantidad_ventana.title("Cantidad de usuarios")
    etiqueta_cantidad = Label(cantidad_ventana, text="Ingrese la cantidad de usuarios:")
    etiqueta_cantidad.pack()
    entrada_cantidad = Entry(cantidad_ventana)
    entrada_cantidad.pack()
    boton_aceptar = Button(cantidad_ventana, text="Aceptar", command= lambda : abrir_ventana_nombres(int(entrada_cantidad.get())))
    boton_aceptar.pack()
    cantidad_ventana.mainloop()
 

boton_cantidad = Button(root, text="Cantidad de usuarios", command=abrir_ventana_cantidad)
boton_cantidad.pack()
root.mainloop()