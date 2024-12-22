
def validacion_get_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:  # si la variable nombre esta vacia
            break
        else:
            print("No se admite dato nulo. Ingrese el nombre: ")
    return nombre


def validacion_get_descripcion():
    descripcion = input("Descripción: ").strip()
    return descripcion  # return es equivalente a break


def validacion_get_categoria():
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("No se admite dato nulo. Ingrese la categoría: ")
        else:
            return categoria


def validacion_get_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(f"{mensaje} ").strip())
            if not cantidad:
                print("No se admite dato nulo. Ingrese la cantidad: ")
            elif cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Ingrese la cantidad: ")
            else:
                return cantidad

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


def validacion_get_precio():
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if not precio:
                print("No se admite dato nulo. Ingrese el precio: ")
            else:
                return precio

        except ValueError:
            print("Tipo de dato no valido. Ingrese el precio: ")