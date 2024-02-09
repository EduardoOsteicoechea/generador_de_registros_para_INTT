from Modelo_5 import Modelo_5

def completar_longitud_de_campo(campo_inicial, longitud):
	valor = str(campo_inicial)
	longitud_de_campo_inicial = len(str(campo_inicial))
	caracteres_restantes = longitud - longitud_de_campo_inicial
	for unidad in range(caracteres_restantes):
		nuevo_valor = "0" + valor
		valor = nuevo_valor
	return valor

def generar_registros_de_numeral_5_y_6(lista_de_listas_de_campos):
	registros = ''
	
	cantidad_de_registros_tipo_ma = 0
	cantidad_de_registros_tipo_mv = 0
	cantidad_de_registros_tipo_me = 0

	for lista in lista_de_listas_de_campos:

		if lista[0] == "MA":
			cantidad_de_registros_tipo_ma += 1
		elif lista[0] == "MV":
			cantidad_de_registros_tipo_mv += 1
		elif lista[0] == "ME":
			cantidad_de_registros_tipo_me += 1	
			
		modelo_5 = Modelo_5(
			lista[0],
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

	texto_de_cantidad_de_registros_tipo_ma = completar_longitud_de_campo(cantidad_de_registros_tipo_ma, 7)
	texto_de_cantidad_de_registros_tipo_mv = completar_longitud_de_campo(cantidad_de_registros_tipo_mv, 7)
	texto_de_cantidad_de_registros_tipo_me = completar_longitud_de_campo(cantidad_de_registros_tipo_me, 7)
	
	registros += "RC" + (texto_de_cantidad_de_registros_tipo_ma + texto_de_cantidad_de_registros_tipo_mv + texto_de_cantidad_de_registros_tipo_me)
	return registros