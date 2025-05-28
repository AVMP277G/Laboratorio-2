#Importar funciones de script
from Interfaz import (
    menu,
    solicitar_datos_cuadrado,
    solicitar_datos_circulo,
    solicitar_datos_triangulo,
    solicitar_datos_rectangulo,
    solicitar_datos_pentagono,
    solicitar_datos_trapecio,
    solicitar_datos_rombo,
    solicitar_datos_romboide,
    mostrar_area_cuadrado,
    mostrar_area_circulo,
    mostrar_area_triangulo,
    mostrar_area_rectangulo,
    mostrar_area_pentagono,
    mostrar_area_trapecio,
    mostrar_area_rombo,
    mostrar_area_romboide  
)
from Figuras import (
    area_cuadrado,
    area_circulo,
    area_triangulo,
    area_rectangulo,
    area_pentagono,
    area_trapecio,
    area_rombo, 
    area_romboide
)
#Variables
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
RECTANGULO = 4
PENTAGONO = 5
TRAPECIO = 6
ROMBO = 7
ROMBOIDE = 8
SALIR = 9
#Inicializar variable de opcion
op = 0
#Estructura while
while op != SALIR:
    #Mostrar menu
    op = menu()
    #Seleccionar figura
    if op == CUADRADO:
        #Solicitar datos
        lado = solicitar_datos_cuadrado()
        #Calcular area
        area = area_cuadrado(lado)
        #Mostrar resultado
        mostrar_area_cuadrado(area)
    elif op == CIRCULO:
        #Solicitar datos
        radio = solicitar_datos_circulo()
        #Calcular area
        area = area_circulo(radio)
        #Mostrar resultado
        mostrar_area_circulo(area)
    elif op == TRIANGULO:
        #Solicitar datos
        base, altura = solicitar_datos_triangulo()
        #Calcular area
        area = area_triangulo(base, altura)
        #Mostrar resultado
        mostrar_area_triangulo(area)
    elif op == RECTANGULO:
        # Solicitar datos
        base, altura = solicitar_datos_rectangulo()
        # Calcular área
        area = area_rectangulo(base, altura)
        # Mostrar resultado
        mostrar_area_rectangulo(area)

    elif op == PENTAGONO: 
        # Solicitar datos
        lado, apotema = solicitar_datos_pentagono()
        # Calcular área
        area = area_pentagono(lado, apotema)
        # Mostrar resultado
        mostrar_area_pentagono(area)

    elif op == TRAPECIO:
        # Solicitar datos
        base_mayor, base_menor, altura = solicitar_datos_trapecio()
        # Calcular área
        area = area_trapecio(base_mayor, base_menor, altura)
        # Mostrar resultado
        mostrar_area_trapecio(area)

    elif op == ROMBO:
        # Solicitar datos
        d1, d2 = solicitar_datos_rombo()
        # Calcular área
        area = area_rombo(d1, d2)
        # Mostrar resultado
        mostrar_area_rombo(area)

    elif op == ROMBOIDE:
        # Solicitar datos
        base, altura = solicitar_datos_romboide()
        # Calcular área
        area = area_romboide(base, altura)
        # Mostrar resultado
        mostrar_area_romboide(area)

    elif op == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")
    else:
        print("Opcion no valida!!!")
    
