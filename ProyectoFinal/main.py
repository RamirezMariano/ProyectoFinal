#Importar los otros archivos python, para que pueda ser más legible y entendible
from funciones_menu import *
from funciones_db import db_crear_tabla_productos

# Se declara la función principal MAIN
def main():
    # Se inicia con la database, en caso que no exista, se va a crear una
    db_crear_tabla_productos()
    while True:
        # El menú muestra las siguientes 7 opciones y devuelve la opcion seleccionada por el usuario
        opcion = menu_mostrar_opciones()
        print("Usted seleccionó la opción: ", opcion)

        if opcion == "1":
            menu_registrar_producto()
        elif opcion == "2":
            menu_mostrar_productos()
        elif opcion == "3":
            menu_actualizar_producto()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_buscar_producto()
        elif opcion == "6":
            menu_reporte_bajo_stock()
        elif opcion == "7":
            print("Gracias por usar nuestra App")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        continuar = input(
            "\nIngrese 's' para salir o cualquier tecla para continuar: ").lower()   #por si el usuario escribe s en mayúscula
        if continuar == "s":
            print("\nGracias por usar nuestra App")
            break

# Llamar a la función principal MAIN
main() 