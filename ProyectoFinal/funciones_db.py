import sqlite3 #importar el módulo de SQLite

#Se conecta o crea la database inventario
def db_crear_tabla_productos(): 
    try:
        conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nombre TEXT NOT NULL, 
                       descripcion TEXT, 
                       categoria TEXT NOT NULL, 
                       cantidad INTEGER NOT NULL, 
                       precio REAL NOT NULL )
        """)
        conexion.commit()
        # print("""El registro
        #        se inserto
        #        exitosamente""")

    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()

#Agregar el producto a la database, con sus respectivas características
def db_insertar_producto(producto):
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?,?,?,?,?)"
    placeholders = (                
        producto["nombre"],
        producto["descripcion"],
        producto["categoria"],
        producto["cantidad"],
        producto["precio"],
    )
#placeholders son los marcadores de posición para SQL
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


#Busca todos los productos dentro de la database, y lo devuelve en una lista de tuplas
def db_get_productos():
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()  # retorna una lista de tuplas
    conexion.close()
    return lista_productos

#Busca el ID seleccionado del producto en particular dentro de la database y lo devuelve en una tupla
def db_get_producto_by_id(id):
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()   #devuelve una tupla
    conexion.close()
    return producto


#Busca el ID del producto para poder modificarle la cantidad
def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()

#Busca el ID del producto para poder eliminarlo por completo de la database
def db_eliminar_producto(id):
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()

#Busca los productos que tengan menor cantidad de la elegida por el usuario
def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect("C:/Users/Mariano/Documents/ProyectoFinal/inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall()  #lo almacena en esta variable para retornarlo al final
    conexion.close()
    return lista_productos