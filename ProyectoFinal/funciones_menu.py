from funciones_db import *
from funciones_validacion import *

def menu_mostrar_opciones():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")
    return opcion

#1) REGISTRO DE PRODUCTOS
def menu_registrar_producto(): 
    print("\nIngrese los siguientes datos del producto:")
    nombre = validacion_get_nombre()
    descripcion = validacion_get_descripcion()
    categoria = validacion_get_categoria()
    cantidad = validacion_get_cantidad()
    precio = validacion_get_precio()

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }

    db_insertar_producto(producto)
    print("\nProducto insertado exitosamente")

#2) VISUALIZACION DE PRODUCTOS
def menu_mostrar_productos():
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos que mostrar")

#3) ACTUALIZACION DE PRODUCTOS
def menu_actualizar_producto():
    id = int(input("\nIngrese el id del producto a actualizar"))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(f"Cantidad actual {get_producto[4]} ")
        nueva_cantidad = validacion_get_cantidad("Nueva cantidad")
        db_actualizar_producto(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")

#4) ELIMINACION DE PRODUCTOS
def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print("Registro eliminado exitosamente!")
        else:
            print("Operación cancelada.")

#5) BUSQUEDA DE PRODUCTOS
def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)

#6) REPORTE DE BAJO STOCK
def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)