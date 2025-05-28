"""
Buenos días, en este punto se simulará una cola de clientes en un banco.
Donde la persona encargada del banco podra tener en cuenta a quien esta atendiendo y supervisará el monto del banco dependiendo los depositos
o retiros del cliente, teniendo asi mayor organizacion y supervición del dinero dentro del banco. 
"""
# Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self):
        self.saldo = 5000000 #Se da inicio a la cuenta con un saldo de 5.000.000 para simular el dinero del banco

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso!!!")
            print(f"Saldo actual en el banco: ${self.saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto debe ser positivo.")
        else:
            self.saldo -= monto
            print("Retiro exitoso!!!")
            print(f"Saldo en actual en el banco: ${self.saldo}")

    def consultar_saldo(self):
        print(f"Monto actual en el banco: ${self.saldo}")


# Función para simular la cola de clientes
def procesar_cola_clientes():
    banco = CuentaBancaria()
    cola = ["Camila", "Daniela", "Angie"]

    for cliente in cola:
        print(f"\nAtendiendo a {cliente}")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo en banco")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            monto = float(input("Ingrese el monto a depositar: "))
            banco.depositar(monto)
        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            banco.retirar(monto)
        elif opcion == 3:
            banco.consultar_saldo()
        else:
            print("Opción incorrecta. Por favor, intente de nuevo.")
        print(f"Fin de la atención a {cliente}")


# Programa principal
procesar_cola_clientes()
