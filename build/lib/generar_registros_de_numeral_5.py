from Modelo_5 import Modelo_5

def generar_registros_de_numeral_5(lista_de_listas_de_campos):
	registros = ''
	for lista in lista_de_listas_de_campos:
		modelo_5 = Modelo_5(
			lista[0], # tipo_de_movimiento
			lista[1],
			lista[2],
			lista[3],
			lista[4],
			lista[5],
			lista[6],
			lista[7],
			lista[8],
			lista[9],
			lista[10],
			lista[11],
			lista[12],
			lista[13],
			lista[14],
			lista[15],
			lista[16],
			lista[17],
			lista[18],
			lista[19],
			lista[20],
			lista[21],
			lista[22],
			lista[23],
			lista[24],
			lista[25],
			lista[26],
			lista[27],
			lista[28],
			lista[29],
			lista[30],
			lista[31],
			lista[32],
			lista[33],
			lista[34],
			lista[35],
			lista[36],
			lista[37],
			lista[38],
			lista[39],
			lista[40],
			lista[41],
			lista[42],
			lista[43],
		)
		nuevo_valor = registros + modelo_5.imprimir_linea() + "\n"
		registros = nuevo_valor
	return registros