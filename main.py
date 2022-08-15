def convertidor(inputNumber, converter):
	
	#decimal a binario
	if (converter == 1):
		
		exitNumber = ""
		rest = 0
		
		while (inputNumber > 0):
			rest = int(inputNumber % 2)
			inputNumber = int(inputNumber / 2)

			exitNumber = str(rest) + exitNumber
			
	#binario a decimal
	else:
		exitNumber = 0
		position = 0
		potency = len(str(inputNumber)) - 1
		
		while (potency >= 0):
			
			number = (str(inputNumber)[position])
			exitNumber = exitNumber + (int(number) * (2 ** potency))
			
			potency = potency - 1
			position = position + 1

	return exitNumber


def printer(instancia, inputNumber, converter):

	if converter == 1:
		result = (f"el numero decimal {inputNumber} tiene el binario {instancia}")
	else:
		result = (f"el numero binario {inputNumber} tiene el el decimal {instancia}")

	result += "\n"

	return result



#instancia 1
#expected exit "11101"
	
inputNumber = 29
converter = 1
	
instancia = convertidor(inputNumber, converter)
print(printer(instancia, inputNumber, converter))


#instancia 2
#expected exit "29"

inputNumber = 11101
converter = 2

instancia = convertidor(inputNumber, converter)
print(printer(instancia, inputNumber, converter))


#instancia 3
#expected exit "110101"

inputNumber = 53
converter = 1

instancia = convertidor(inputNumber, converter)
print(printer(instancia, inputNumber, converter))


#instancia 4
#expected exit "11"

inputNumber = 1011
converter = 2

instancia = convertidor(inputNumber, converter)
print(printer(instancia, inputNumber, converter))
