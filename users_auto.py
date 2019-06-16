 
import sqlite3

conexion = sqlite3.connect('usuarios_auto.db')

cursor = conexion.cursor()

# cursor.execute('''CREATE TABLE usuarios (
#                     id INTEGER PRIMARY KEY,
#                     dni VARCHAR(9) UNIQUE,
#                     nombre VARCHAR(100), 
#                     edad INTEGER,
#                     email VARCHAR(100))''')

# usuarios = [('53456', 'Luis', 27, 'luis@ejemplo.com'),
#             ('23435', 'Juan', 51, 'juan@ejemplo.com'),
#             ('12433', 'Carlos', 38, 'carlos@ejemplo.com'),
#             ('44443', 'Jon', 19, 'jon@ejemplo.com')]

# cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

# cursor.execute("INSERT INTO usuarios VALUES ('11111111A', 'Fernando', 31, 'fernando@ejemplo.com')")

# cursor.execute("SELECT * FROM usuarios WHERE id=2")

# cursor.execute("UPDATE usuarios SET nombre='Tyrion Lannister' WHERE dni=44443")

# cursor.execute("SELECT * FROM  usuarios WHERE dni=44443")

# cursor.execute("INSERT INTO usuarios VALUES (null, '8235875', 'Luis Fernando', 21, 'fernando@gmail.com')")

for usuario in cursor.execute("SELECT * FROM usuarios"):
	print("[{}] {}".format(usuario[0], usuario[1]))

# cursor.execute("DELETE FROM usuarios WHERE dni='8235875'")

# print()

# for usuario in cursor.execute("SELECT * FROM usuarios"):	
	# print(usuario)

# user = cursor.fetchone()
# print(user)

# usuarios = cursor.fetchall()

# for usuario in usuarios:
# 	print(usuario)




conexion.commit()
conexion.close()