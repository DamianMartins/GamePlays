import pyodbc
import sqlite3
# Conexion a la base de datos
conn = pyodbc.connect('DRIVER={SQL Server};''SERVER=PRACTIAARNB1677;''DATABASE=preguntas;''UID=sa;PWD=Mada3983')
#conn = pyodbc.connect('Driver={SQL Server};''Server=PRACTIAARNB1677;''Database=preguntas;''Trusted_Connection=yes;')

# Obtener un cursor para realizar operaciones en la base de datos
#cursor = conn.cursor()
db = sqlite3.connect("preguntas.db")
# Preguntar al usuario el filtro
cursor = db.cursor()
# Ejecutar una consulta para obtener todas las películas
cursor.execute('SELECT titulo, anio, genero, protagonista FROM [preguntas].[dbo].[peliculas]')

# Obtener todos los resultados de la consulta
peliculas = cursor.fetchall()

# Pedir al usuario que seleccione un campo
campo_seleccionado = input("Seleccione un campo para buscar (anio, genero o protagonista): ")

# Validar que el campo seleccionado sea válido
campos_validos = ['anio', 'genero', 'protagonista']
if campo_seleccionado not in campos_validos:
    print("Campo no válido. Seleccione uno de los siguientes campos: ", campos_validos)
    exit()

# Pedir al usuario que ingrese el valor a buscar
valor_buscado = input("Ingrese el valor a buscar: ")

# Buscar las películas que coincidan con el valor buscado en el campo seleccionado
peliculas_coincidentes = []
for pelicula in peliculas:
    if valor_buscado.lower() in str(pelicula[campos_validos.index(campo_seleccionado)]).lower():
        peliculas_coincidentes.append(pelicula)

# Mostrar los nombres de las películas coincidentes
if len(peliculas_coincidentes) == 0:
    print("No se encontraron películas que coincidan con el valor buscado.")
else:
    print("Películas que coinciden con el valor buscado:")
    for pelicula in peliculas_coincidentes:
        print(pelicula[0])

# Cerrar la conexión a la base de datos
conn.close()






#hacer un Select a la base de datos segun el filtro, y que ese develva los nombres de las peliculas
