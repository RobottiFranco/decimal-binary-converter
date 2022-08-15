def convertidor(entradaNumero, entradaConvertidor):
	
	#decimal a binario
	if (entradaConvertidor == 1):
		
		salidaNumero = ""
		resto = 0
		
		while (entradaNumero > 0):
			resto = int(entradaNumero % 2)
			entradaNumero = int(entradaNumero / 2)

			salidaNumero = str(resto) + salidaNumero
			
	#binario a decimal
	else:
		salidaNumero = 0
		posicion = 0
		potencia = len(str(entradaNumero)) - 1
		
		while (potencia >= 0):
			
			numero = (str(entradaNumero)[posicion])
			salidaNumero = salidaNumero + (int(numero) * (2 ** potencia))
			
			potencia = potencia - 1
			posicion = posicion + 1

	return salidaNumero


def impresion(caso, entradaNumero, entradaConvertidor):

	if entradaConvertidor == 1:
		resultado += (f"el numero decimal {entradaNumero} tiene el binario {caso}")
	else:
		resultado += (f"el numero binario {entradaNumero} tiene el el decimal {caso}")

	resultado += "\n"

	return resultado



#caso 1
#salida esperada "11101"
	
entradaNumero = 29
entradaConvertidor = 1
	
caso = convertidor(entradaNumero, entradaConvertidor)
print(impresion(caso, entradaNumero, entradaConvertidor))


#caso 2
#salida esperada "29"

entradaNumero = 11101
entradaConvertidor = 2

caso = convertidor(entradaNumero, entradaConvertidor)
print(impresion(caso, entradaNumero, entradaConvertidor))


#caso 3
#salida esperada "110101"

entradaNumero = 53
entradaConvertidor = 1

caso = convertidor(entradaNumero, entradaConvertidor)
print(impresion(caso, entradaNumero, entradaConvertidor))


#caso 4
#salida esperada "11"

entradaNumero = 1011
entradaConvertidor = 2

caso = convertidor(entradaNumero, entradaConvertidor)
print(impresion(caso, entradaNumero, entradaConvertidor))
