import pandas 

def obtener_datos_de_excel(nombre_de_archivo):

	df = pandas.read_excel(nombre_de_archivo)

	lista_de_filas = []

	contador = 1

	for index, row in df.iterrows():
		fila_como_lista = row.values.tolist()
		nueva_lista_de_textos = []
		contador_de_celda = 1
		
		for celda in fila_como_lista:
			nueva_lista_de_textos.append(str(celda))
			contador_de_celda = contador_de_celda + 1
		
		lista_de_filas.append(nueva_lista_de_textos)
		contador = contador + 1

	return lista_de_filas

