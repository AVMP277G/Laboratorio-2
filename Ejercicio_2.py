#b)	Procesamiento de datos a gran escala
logs = []
print("Ingrese los datos de acceso (usuario, entrada, salida). Escriba 'fin' para terminar.")

# Lectura con bucle while
while True:
    entrada = input("Usuario, entrada, salida: ")
    if entrada.lower() == 'fin':
        break
    logs.append(entrada.split(','))

# Conteo con bucle for
usuarios = {}
for log in logs:
    nombre = log[0].strip()
    if nombre in usuarios:
        usuarios[nombre] += 1
    else:
        usuarios[nombre] = 1

# Almacenamiento en lista
resultados = [[usuario, accesos] for usuario, accesos in usuarios.items()]

print("\nResumen de accesos:")
for usuario, accesos in resultados:
    print(f"{usuario}: {accesos} accesos")
