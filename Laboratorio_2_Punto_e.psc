Proceso SimuladorBanco
    Definir cliente0, cliente1, cliente2 Como Cadena
    Definir saldo, monto Como Real
    Definir opcion, i Como Entero
	
    //Aca asignamos los nombres a cada cliente
    cliente0 <- "Camila"
    cliente1 <- "Daniela"
    cliente2 <- "Angie"
    saldo <- 5000000
	
    Para i <- 0 Hasta 2 Con Paso 1
        Si i = 0 Entonces
            Escribir "Atendiendo a: " + cliente0
        FinSi
        Si i = 1 Entonces
            Escribir "Atendiendo a: " + cliente1
        FinSi
        Si i = 2 Entonces
            Escribir "Atendiendo a: " + cliente2
        FinSi
		
        Escribir "1. Depositar"
        Escribir "2. Retirar"
        Escribir "3. Consultar saldo"
        Leer opcion
		
        Segun opcion Hacer
            1:
                Escribir "Ingrese monto a depositar:"
                Leer monto
                saldo <- saldo + monto
				Escribir "Deposito exitoso"
				Escribir "Saldo actual en banco es: $", saldo
            2:
                Escribir "Ingrese monto a retirar:"
                Leer monto
                Si monto <= saldo Entonces
                    saldo <- saldo - monto
                    Escribir "Retiro exitoso"
					Escribir "Saldo actual en banco es: $", saldo
                SiNo
                    Escribir "Fondos insuficientes"
                FinSi
            3:
                Escribir "Saldo actual en banco es: ", saldo
            De Otro Modo:
                Escribir "Opción inválida"
        FinSegun
    FinPara
FinProceso
