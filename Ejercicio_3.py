#c)	Simulación de una red de sensores
import random

n = int(input("Ingrese número de filas de sensores: "))
m = int(input("Ingrese número de columnas de sensores: "))

# Generación de matriz
matriz = [[random.randint(60, 100) for _ in range(m)] for _ in range(n)]

# Detección de valores críticos
def detectar_criticos(matriz):
    print("\nSensores críticos (>80°C):")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 80:
                print(f"Sensor [{i}][{j}] = {matriz[i][j]}°C")

# Mostrar matriz y detectar críticos
print("\nMatriz de sensores:")
for fila in matriz:
    print(fila)

detectar_criticos(matriz)
