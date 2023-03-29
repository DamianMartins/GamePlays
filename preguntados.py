import sqlite3
import random
import tkinter as tk
from tkinter import messagebox

def obtener_pregunta():
    #conectar python a base de datos SQL server

    # conectar a la base de datos
    db = sqlite3.connect("preguntas.db")

    # obtener un cursor para realizar operaciones en la base de datos
    cursor = db.cursor()

    # Si la tabla preguntas no existe, crearla
    # TODO: Definir la tabla `preguntas`
    cursor.execute("""create table if not exists preguntas (
        id integer primary key,
        pregunta text,
        opcion_a text,
        opcion_b text,
        opcion_c text,
        respuesta text)
    """)

    # obtener la cantidad de preguntas en la base de datos
    cursor.execute("SELECT COUNT(*) FROM preguntas")
    num_preguntas = cursor.fetchone()[0]

    # Chequeo de que hay preguntas en la base de datos
    if num_preguntas == 0:
        messagebox.showerror(message="No hay preguntas en la base de datos.")
        raise AssertionError("No hay preguntas en la base de datos.")

    # elegir un número aleatorio entre 1 y el número de preguntas
    num_aleatorio = random.randint(1, num_preguntas) # Los id usualmente empiezan en 1

    # obtener la pregunta correspondiente al número aleatorio
    cursor.execute("SELECT * FROM preguntas WHERE id={}".format(num_aleatorio))
    pregunta = cursor.fetchone()


    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Juego Preguntados")

    # Crear la etiqueta con la pregunta
    etiqueta_pregunta = tk.Label(ventana, text=pregunta[1])
    etiqueta_pregunta.pack()

    # Crear las opciones de respuesta como botones
    def seleccionar_respuesta(letra):
        if letra == pregunta[5]:
            resultado = "¡Respuesta correcta!"
        else:
            resultado = "Respuesta incorrecta. La respuesta correcta es {}".format(pregunta[5])
        label_resultado = tk.Label(ventana, text=resultado)
        label_resultado.pack()

    boton_a = tk.Button(ventana, text=pregunta[2], command=lambda: seleccionar_respuesta("A"))
    boton_a.pack()
    boton_b = tk.Button(ventana, text=pregunta[3], command=lambda: seleccionar_respuesta("B"))
    boton_b.pack()
    boton_c = tk.Button(ventana, text=pregunta[4], command=lambda: seleccionar_respuesta("C"))
    boton_c.pack()

    # Iniciar el bucle de la ventana
    ventana.mainloop()

    # cerrar la conexión a la base de datos
    db.close()

    # devolver la pregunta y las opciones
    return pregunta[1], pregunta[2], pregunta[3], pregunta[4]

def juego_preguntados():
    pregunta, opcion_a, opcion_b, opcion_c = obtener_pregunta()

    # imprimir la pregunta y las opciones
    print("Pregunta: {}".format(pregunta))
    print("A) {}".format(opcion_a))
    print("B) {}".format(opcion_b))
    print("C) {}".format(opcion_c))

    # esperar la respuesta del usuario
    respuesta = input("Respuesta: ")

    # comprobar si la respuesta es correcta
    if respuesta == pregunta[5]:
        print("¡Respuesta correcta!")
    else:
        print("Respuesta incorrecta. La respuesta correcta es {}".format(pregunta[5]))