 
import sqlite3

# conexion = sqlite3.connect('usuarios.db')

cursor = conexion.cursor()

# Creamos un campo dni como clave primaria


cursor.execute('''CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY,
                    dni VARCHAR(9) UNIQUE,
                    nombre VARCHAR(100), 
                    edad INTEGER,
                    email VARCHAR(100))''')

usuarios = [('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
cursor.execute("INSERT INTO usuarios VALUES ('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")

conexion.commit()
conexion.close()