from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import END, Toplevel, StringVar
from tkinter.ttk import Button, Label, Entry
from tkinter import Listbox
from database import DB
# from preguntados import juego_preguntados

class VentanaCantidad(tk.Toplevel):
    def __inti__(self, parent):
        super().__init__(parent)

        self.title = "Cantidad de usuarios"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        main_frame = tk.Frame(self, padx=3, pady=3)
        
        # inputs
        frame_inputs = self.get_inputs_frame(main_frame)
        frame_inputs.grid(row=0, column=0)

        # Table
        frame_table = self.get_table_frame(main_frame)
        frame_table.grid(row=1, column=0)

        main_frame.grid(row=0,column=0)

        # center app
        center_width = self.winfo_screenwidth()//2
        center_height = self.winfo_screenheight()//2
        width = 300
        heigth = 450
        self.geometry(f"{width}x{heigth}+{center_width-(width//2)}+{center_height-(heigth//2)}")


    def get_inputs_frame(self, parent):
        """Genera el frame para el ingreso de los nombres"""
        inputs_frame = ttk.Frame(parent)

        self.nombre_var = tk.StringVar()

        ttk.Label(inputs_frame, text= 'Nombre').grid(row=0, column=0)
        ttk.Entry(inputs_frame, textvariable=self.nombre_var).grid(row=0, column=1)
        ttk.Button(inputs_frame, text="Agregar", command=self.add_nombre).grid(row=0, column=2)

        return inputs_frame


    def get_table_frame(self, parent):
        """genera el frame para el treeview (tabla)"""

        frame_table = ttk.Frame(parent)

        self.table = ttk.Treeview(frame_table, columns=('name',), show='headings')

        self.table.heading('name', text='Nombre')
        self.table.grid(row=0, column=0, sticky=tk.NSEW)

        return frame_table
    

    def add_nombre(self):
        nombre = self.nombre_var.get()
        self.table.insert('', tk.END, values=(nombre))
        DB.insert_name(name=nombre)

    def print_nombres(self):
        pass


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
    
    boton_aceptar = Button(cantidad_ventana, text="Aceptar", command=aceptar_cantidad)
    boton_aceptar.pack()



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



    # Llamar a función abrir_ventana_nombres cuando se haga click en el botón Aceptar
    def aceptar_cantidad():
        cantidad = entrada_cantidad.get()
        abrir_ventana_nombres(int(cantidad))
        cantidad_ventana.destroy()



if __name__ == '__main__':
    DB.exec("""
    create table if not exists gamers (
        id integer primary key,
        name varchar
    );
    """)
    DB.clean_table()
    app = App()
    app.mainloop()
