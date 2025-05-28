class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        self.cantidad += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self.nombre}.")
            return False

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"

def mostrar_inventario(productos):
    print("\nInventario actual:")
    for producto in productos:
        print(producto)
    print()

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None

# Productos iniciales
productos = [
    Producto("manzanas", 1500, 20),
    Producto("pan", 800, 30),
    Producto("leche", 2000, 15)
]

def menu():
    while True:
        print("1. Mostrar inventario")
        print("2. Comprar producto ")
        print("3. Vender producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(productos)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a comprar: ")
            producto = buscar_producto(productos, nombre)
            if producto:
                try:
                    cantidad = int(input("Ingrese la cantidad a agregar: "))
                    producto.aumentar_stock(cantidad)
                    print("Stock actualizado.\n")
                except ValueError:
                    print("Cantidad inválida.\n")
            else:
                print("Producto no encontrado.\n")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a vender: ")
            producto = buscar_producto(productos, nombre)
            if producto:
                try:
                    cantidad = int(input("Ingrese la cantidad a vender: "))
                    if producto.disminuir_stock(cantidad):
                        print("Stock actualizado.\n")
                except ValueError:
                    print("Cantidad inválida.\n")
            else:
                print("Producto no encontrado.\n")
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()