#Calcular el areas de figuras geométricas
import math

# 1. Cuadrado
def area_cuadrado(lado):
    """
    Calcula el area de un cuadrado
    area = lado * lado
    :param lado: float
    :return: float
    """
    area = lado ** 2
    return area


#2. Círculo
def area_circulo(radio):
    """
    Calcula el area de un circulo
    area = pi * radio^2
    :param radio: float
    :return: float
    """
    area = math.pi * (radio ** 2)
    return area


#3. Triángulo
def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo
    area = (base * altura) / 2
    :param base: float
    :param altura: float
    :return: float
    """
    area = (base * altura) / 2
    return area


# 4. Rectángulo
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Fórmula: A = base * altura

    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    area = base * altura
    return area


# 5. Pentágono regular
def area_pentagono(lado, apotema):
    """
    Calcula el área de un pentágono regular.
    Fórmula: A = (P * apotema) / 2, donde P = 5 * lado

    para lado: Longitud de un lado del pentágono (float)
    para apotema: Apotema del pentágono (float)
    return: Área del pentágono (float)
    """
    perimetro = 5 * lado
    area = (perimetro * apotema) / 2
    return area


# 6. Trapecio
def area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio.
    Fórmula: A = ((base mayor + base menor) * altura) / 2

    para base_mayor: Base mayor del trapecio (float)
    para base_menor: Base menor del trapecio (float)
    para altura: Altura del trapecio (float)
    return: Área del trapecio (float)
    """
    area = ((base_mayor + base_menor) * altura) / 2
    return area


# 7. Rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo.
    Fórmula: A = (diagonal mayor * diagonal menor) / 2

    para diagonal_mayor: Longitud de la diagonal mayor (float)
    para diagonal_menor: Longitud de la diagonal menor (float)
    return: Área del rombo (float)
    """
    area = (diagonal_mayor * diagonal_menor) / 2
    return area


# 8. Romboide
def area_romboide(base, altura):
    """
    Calcula el área de un romboide.
    Fórmula: A = base * altura

    para base: Base del romboide (float)
    para altura: Altura del romboide (float)
    return: Área del romboide (float)
    """
    area = base * altura
    return area
