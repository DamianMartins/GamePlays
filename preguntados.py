# importar librerías necesarias para la creación del juego
import sqlite3
import random

# conectar a la base de datos
db = sqlite3.connect("preguntas.db")

# obtener un cursor para realizar operaciones en la base de datos
cursor = db.cursor()

# obtener la cantidad de preguntas en la base de datos
cursor.execute("SELECT COUNT(*) FROM preguntas")
num_preguntas = cursor.fetchone()[0]

# elegir un número aleatorio entre 0 y el número de preguntas
num_aleatorio = random.randint(0, num_preguntas - 1)

# obtener la pregunta correspondiente al número aleatorio
cursor.execute("SELECT * FROM preguntas WHERE id={}".format(num_aleatorio))
pregunta = cursor.fetchone()

# imprimir la pregunta y sus posibles respuestas
print("Pregunta: {}".format(pregunta[1]))
print("A) {}".format(pregunta[2]))
print("B) {}".format(pregunta[3]))
print("C) {}".format(pregunta[4]))

# esperar la respuesta del usuario
respuesta = input("Respuesta: ")

# comprobar si la respuesta es correcta
if respuesta == pregunta[5]:
    print("¡Respuesta correcta!")
else:
    print("Respuesta incorrecta. La respuesta correcta es {}".format(pregunta[5]))

# cerrar la conexión a la base de datos
db.close()