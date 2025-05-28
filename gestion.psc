Algoritmo gestion
		
	Dimension nombres[3]
    Dimension precios[3]
    Dimension cantidades[3]
    Definir i, cambio, opcion Como Entero
	
    nombres[1] <- "Manzanas"
    precios[1] <- 1500
    cantidades[1] <- 20
	
    nombres[2] <- "Pan"
    precios[2] <- 800
    cantidades[2] <- 30
	
    nombres[3] <- "Leche"
    precios[3] <- 2000
    cantidades[3] <- 15
	
    Repetir
        Escribir "MENU DE INVENTARIO"
        Escribir "1. Mostrar inventario"
        Escribir "2. Aumentar stock"
        Escribir "3. Disminuir stock"
        Escribir "4. Salir"
        Leer opcion
		
        Segun opcion Hacer
            1:
                Para i <- 1 Hasta 3 Con Paso 1
                    Escribir "Producto: ", nombres[i]
                    Escribir "Precio: $", precios[i]
                    Escribir "Stock: ", cantidades[i]
                    Escribir "---------------------------"
                FinPara
				
            2:
                Escribir "Ingrese el numero del producto (1-Manzanas, 2-Pan, 3-Leche):"
                Leer i
                Escribir "¿Cuantas unidades desea agregar?"
                Leer cambio
                cantidades[i] <- cantidades[i] + cambio
                Escribir "Stock actualizado: ", cantidades[i]
				
            3:
                Escribir "Ingrese el número del producto (1-Manzanas, 2-Pan, 3-Leche):"
                Leer i
                Escribir "¿Cuantas unidades desea vender?"
                Leer cambio
                Si cambio <= cantidades[i] Entonces
                    cantidades[i] <- cantidades[i] - cambio
                    Escribir "Venta realizada. Stock restante: ", cantidades[i]
                Sino
                    Escribir "Stock insuficiente para realizar la venta."
                FinSi
				
            4:
                Escribir "Saliendo del sistema..."
            De Otro Modo:
                Escribir "Opcion invalida"
        FinSegun
		
    Hasta Que opcion = 4
FinAlgoritmo
