import sqlite3

conexion = sqlite3.connect('productos.db')

cursor = conexion.cursor()

cursor.execute('''CREATE TABLE productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(100) NOT NULL, 
                    marca VARCHAR(50) NOT NULL, 
                    precio FLOAT NOT NULL)''')

productos = [('Teclado', 'Logitech', 19.95),
             ('Pantalla 19"','LG', 89.95),
             ('Altavoces 2.1','LG', 24.95)]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()

for producto in productos:
	print(producto)

conexion.commit()
conexion.close()
