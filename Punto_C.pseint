Algoritmo  Simulacion_Red_Sensores
		Definir n, m, i, j Como Entero
		Definir matriz Como Entero
		
		Escribir "Ingrese número de filas de sensores: "
		Leer n
		Escribir "Ingrese número de columnas de sensores: "
		Leer m
		
		Dimension matriz[n, m]
		
		// Generar matriz con temperaturas aleatorias
		Para i <- 0 Hasta n - 1
			Para j <- 0 Hasta m - 1
				matriz[i, j] <- Aleatorio(60, 100)
			FinPara
		FinPara
		
		// Mostrar matriz
		Escribir ""
		Escribir "Matriz de sensores:"
		Para i <- 0 Hasta n - 1
			Para j <- 0 Hasta m - 1
				Escribir Sin Saltar matriz[i, j], "  "
			FinPara
			Escribir ""
		FinPara
		
		// Detectar sensores críticos
		Escribir ""
		Escribir "Sensores críticos (>80°C):"
		Para i <- 0 Hasta n - 1
			Para j <- 0 Hasta m - 1
				Si matriz[i, j] > 80 Entonces
					Escribir "Sensor [", i, "][", j, "] = ", matriz[i, j], "°C"
				FinSi
			FinPara
		FinPara
		
	
FinAlgoritmo
