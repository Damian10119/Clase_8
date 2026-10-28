
# NOMBRE: DAMIAN PILLAJO
# FECHA: 01/11/2026
# CLASE: 8
# Sistema básico de gestión de inventario y pedidos
# Tema 5: Arreglos unidimensionales

# Listas que almacenan los productos y pedidos.
productos = []
pedidos = []


def registrar_producto():
    # Registra un producto con su nombre, precio y stock.
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad disponible: "))

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    print("Producto registrado correctamente.")


def mostrar_productos():
    # Muestra todos los productos registrados.
    if not productos:
        print("No hay productos registrados.")
        return

    for i, producto in enumerate(productos):
        print(
            f"{i + 1}. {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Stock: {producto['stock']}"
        )


def editar_producto():
    # Modifica los datos de un producto existente.
    mostrar_productos()

    if productos:
        try:
            indice = int(input("Número del producto a editar: ")) - 1

            if 0 <= indice < len(productos):
                productos[indice]["nombre"] = input("Nuevo nombre: ")
                productos[indice]["precio"] = float(input("Nuevo precio: "))
                productos[indice]["stock"] = int(input("Nuevo stock: "))
                print("Producto actualizado.")
            else:
                print("Número de producto no válido.")
        except ValueError:
            print("Debes introducir valores numéricos válidos.")


def eliminar_producto():
    # Elimina un producto de la lista.
    mostrar_productos()

    if productos:
        try:
            indice = int(input("Número del producto a eliminar: ")) - 1

            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                print(f"Producto {eliminado['nombre']} eliminado.")
            else:
                print("Número de producto no válido.")
        except ValueError:
            print("Debes introducir un número válido.")


def registrar_pedido():
    # Registra una descripción y el estado del pedido.
    cliente = input("Nombre del cliente: ")
    descripcion = input("Descripción del pedido: ")

    pedidos.append({
        "cliente": cliente,
        "descripcion": descripcion
    })
    print("Pedido registrado correctamente.")


def mostrar_pedidos():
    # Recorre y muestra la lista de pedidos.
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    for i, pedido in enumerate(pedidos):
        print(
            f"{i + 1}. Cliente: {pedido['cliente']} | "
            f"Pedido: {pedido['descripcion']}"
        )


def editar_pedido():
    # Permite actualizar un pedido existente.
    mostrar_pedidos()

    if pedidos:
        try:
            indice = int(input("Número del pedido a editar: ")) - 1

            if 0 <= indice < len(pedidos):
                pedidos[indice]["cliente"] = input("Nuevo cliente: ")
                pedidos[indice]["descripcion"] = input("Nueva descripción: ")
                print("Pedido actualizado.")
            else:
                print("Número de pedido no válido.")
        except ValueError:
            print("Debes introducir un número válido.")


def eliminar_pedido():
    # Elimina un pedido de la lista.
    mostrar_pedidos()

    if pedidos:
        try:
            indice = int(input("Número del pedido a eliminar: ")) - 1

            if 0 <= indice < len(pedidos):
                pedidos.pop(indice)
                print("Pedido eliminado correctamente.")
            else:
                print("Número de pedido no válido.")
        except ValueError:
            print("Debes introducir un número válido.")


# Menú principal: se repite hasta seleccionar la opción de salida.
def menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Registrar pedido")
        print("6. Mostrar pedidos")
        print("7. Editar pedido")
        print("8. Eliminar pedido")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_pedido()
        elif opcion == "6":
            mostrar_pedidos()
        elif opcion == "7":
            editar_pedido()
        elif opcion == "8":
            eliminar_pedido()
        elif opcion == "9":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


# Punto de entrada del programa.
if __name__ == "__main__":
    menu()
