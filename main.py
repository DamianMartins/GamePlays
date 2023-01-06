from logging import root
import tkinter as tk
from tkinter import END, Toplevel, StringVar
from tkinter.ttk import Button, Label, Entry
from tkinter import Listbox
from preguntados import juego_preguntados

def abrir_ventana_juegos(nombres):
    # Crear ventana modal
    juegos_ventana = Toplevel()
    juegos_ventana.title("Menú de GamePlays")
    juegos_ventana.grab_set()
    
    # Crear widgets
    etiqueta_juegos = Label(juegos_ventana, text="Seleccione un juego para los usuarios {}:".format(", ".join(nombres)))
    etiqueta_juegos.pack()
    lista_juegos = Listbox(juegos_ventana)
    lista_juegos.pack()
    lista_juegos.insert(END, "Preguntados")
    lista_juegos.insert(END, "Karaoke")
    lista_juegos.insert(END, "Ponele la cola al burro")
    lista_juegos.insert(END, "Adivina la pelicula")
    
    # Llamar a función juego_preguntados cuando el usuario seleccione "Preguntados" en la lista de juegos
    def ejecutar_juego():
        juego_seleccionado = lista_juegos.get(lista_juegos.curselection())
        if juego_seleccionado == "Preguntados":
            juego_preguntados()
            juegos_ventana.destroy()
    boton_aceptar = Button(juegos_ventana, text="Aceptar", command=ejecutar_juego)
    boton_aceptar.pack()
    

def abrir_ventana_nombres(cantidad):
    # Crear ventana 
    nombres_ventana = Toplevel()
    nombres_ventana.title("Nombres de los usuarios")
    nombres_ventana.grab_set()
    
    # Crear widgets
    etiqueta_nombres = Label(nombres_ventana, text="Ingrese los nombres de los usuarios:")
    etiqueta_nombres.pack()
    nombres = []
    for i in range(cantidad):
        etiqueta_nombre = Label(nombres_ventana, text="Usuario {}:".format(i+1))
        etiqueta_nombre
    etiqueta_nombre.pack()
    entrada_nombre = Entry(nombres_ventana)
    entrada_nombre.pack()
    nombres.append(entrada_nombre.get())
    
    # Llamar a función abrir_ventana_juegos cuando se haga click en el botón Aceptar
    def aceptar_nombres():
        abrir_ventana_juegos(nombres)
        nombres_ventana.destroy()
    boton_aceptar = Button(nombres_ventana, text="Aceptar", command=aceptar_nombres)
    boton_aceptar.pack()

def abrir_ventana_cantidad():
    # Crear ventana modal
    cantidad_ventana = Toplevel()
    cantidad_ventana.title("Cantidad de usuarios")
    cantidad_ventana.grab_set()
    
    # Crear widgets
    etiqueta_cantidad = Label(cantidad_ventana, text="Ingrese la cantidad de usuarios:")
    etiqueta_cantidad.pack()
    entrada_cantidad = Entry(cantidad_ventana)
    entrada_cantidad.pack()
    
    # Llamar a función abrir_ventana_nombres cuando se haga click en el botón Aceptar
    def aceptar_cantidad():
        cantidad = entrada_cantidad.get()
        abrir_ventana_nombres(int(cantidad))
        cantidad_ventana.destroy()
    boton_aceptar = Button(cantidad_ventana, text="Aceptar", command=aceptar_cantidad)
    boton_aceptar.pack()

# Crear widget para abrir ventana modal de cantidad de usuarios
root = tk.Tk()
boton_cantidad = tk.Button(root, text="Cantidad de usuarios", command=abrir_ventana_cantidad)
boton_cantidad.pack()
root.mainloop()