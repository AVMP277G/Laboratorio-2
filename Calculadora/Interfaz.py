#Solicita y muestra información
#Menú
def menu():
    """
    Muestra el menú de opciones
    """
    print("Bienvenido a la calculadora de figuras geométricas")
    print("Seleccione una figura para calcular su área:")
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Triángulo")
    print("4. Pentágono")
    print("5. Trapecio")
    print("6. Rombo")
    print("7. Rectángulo")
    print("8. Romboide")
    print("9. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion
#Solicitar datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita el lado de un cuadrado
    :return: float
    """
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado
#Solicitar datos circulo
def solicitar_datos_circulo():
    """
    Solicita el radio de un circulo
    :return: float
    """
    radio = float(input("Ingrese el radio del circulo: "))
    return radio
#Solicitar datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita la base y altura de un triangulo
    :return: float, float
    """
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    return base, altura
#Solicitar datos rectángulo
def solicitar_datos_rectangulo():
    """
    Solicita la base y la altura de un rectángulo
    :return: float, float
    """
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return base, altura

#Solicitar datos pentágono regular
def solicitar_datos_pentagono():
    """
    Solicita el lado y la apotema de un pentágono regular
    :return: float, float
    """
    lado = float(input("Ingrese el lado del pentágono: "))
    apotema = float(input("Ingrese la apotema del pentágono: "))
    return lado, apotema

#Solicitar datos trapecio
def solicitar_datos_trapecio():
    """
    Solicita la base mayor, base menor y altura de un trapecio
    :return: float, float, float
    """
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    return base_mayor, base_menor, altura

#Solicitar datos rombo
def solicitar_datos_rombo():
    """
    Solicita las dos diagonales de un rombo
    :return: float, float
    """
    d_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    d_menor = float(input("Ingrese la diagonal menor del rombo: "))
    return d_mayor, d_menor

#Solicitar datos romboide
def solicitar_datos_romboide():
    """
    Solicita la base y altura de un romboide
    :return: float, float
    """
    base = float(input("Ingrese la base del romboide: "))
    altura = float(input("Ingrese la altura del romboide: "))
    return base, altura

#Mostrar area del cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el area de un cuadrado
    :param area: float
    """
    print(f"El area del cuadrado es: {area}")
#Mostrar area del circulo
def mostrar_area_circulo(area):
    """
    Muestra el area de un circulo
    :param area: float
    """
    print(f"El area del circulo es: {area}")
#Mostrar area del triangulo
def mostrar_area_triangulo(area):
    """
    Muestra el area de un triangulo
    :param area: float
    """
    print(f"El area del triangulo es: {area}")
#Mostrar área del rectángulo
def mostrar_area_rectangulo(area):
    """
    Muestra el área de un rectángulo
    :param area: float
    """
    print(f"El área del rectángulo es: {area}")

#Mostrar área del pentágono
def mostrar_area_pentagono(area):
    """
    Muestra el área de un pentágono regular
    :param area: float
    """
    print(f"El área del pentágono es: {area}")

#Mostrar área del trapecio
def mostrar_area_trapecio(area):
    """
    Muestra el área de un trapecio
    :param area: float
    """
    print(f"El área del trapecio es: {area}")

#Mostrar área del rombo
def mostrar_area_rombo(area):
    """
    Muestra el área de un rombo
    :param area: float
    """
    print(f"El área del rombo es: {area}")

#Mostrar área del romboide
def mostrar_area_romboide(area):
    """
    Muestra el área de un romboide
    :param area: float
    """
    print(f"El área del romboide es: {area}")
