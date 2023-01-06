# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto 
# y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

conexion = sqlite3.connect('Base_Datos.db')
cursor = conexion.cursor()

cursor.execute("CREATE TABLE Alumnos (id INT, nombre TEXT, apellido TEXT)")
cursor.execute("INSERT INTO Alumnos VALUES (1, 'Juan', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES (2, 'Carlos', 'Rojas')")
cursor.execute("INSERT INTO Alumnos VALUES (3, 'Camila', 'Diaz')")
cursor.execute("INSERT INTO Alumnos VALUES (4, 'Manuel', 'Soto')")
cursor.execute("INSERT INTO Alumnos VALUES (5, 'Sergio', 'Contreras')")
cursor.execute("INSERT INTO Alumnos VALUES (6, 'Matias', 'Silva')")
cursor.execute("INSERT INTO Alumnos VALUES (7, 'Vania', 'Torres')")
cursor.execute("INSERT INTO Alumnos VALUES (8, 'Claudia', 'Martinez')")

conexion.commit()
cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'Camila'")

fila = cursor.fetchall()
print(fila)

cursor.close()
conexion.close()