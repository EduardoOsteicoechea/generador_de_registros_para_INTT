class Modelo_6:
	def __init__(
		self, 
		cantidad_de_registros_tipo_ma: str = "0000000",
		cantidad_de_registros_tipo_mm: str = "0000000",
		cantidad_de_registros_tipo_me: str = "0000000"
	):
		self.rc = "RC"
		self.cantidad_de_registros_tipo_ma = cantidad_de_registros_tipo_ma
		self.cantidad_de_registros_tipo_mm = cantidad_de_registros_tipo_mm
		self.cantidad_de_registros_tipo_me = cantidad_de_registros_tipo_me
		self.completar_caracteres_en_campos()
		self.campos_unidos = ''
		self.sumar_campos()
		
		

	def __str__(self):
		return self.sumar_campos()
	
	def sumar_campos(self):
		valor = ''
		for key,value in vars(self).items():
			valor += value
		self.campos_unidos = valor
	
	def completar_caracteres_en_campos(self):
		longitud_de_campos = [
			["rc","str",2," "],
			["cantidad_de_registros_tipo_ma","str",7,"0"],
			["cantidad_de_registros_tipo_mm","str",7,"0"],
			["cantidad_de_registros_tipo_me","str",7,"0"]
		]
		counter = 0	
		for key in longitud_de_campos:
			valor = vars(self)[key[0]]
			campo = key[0]
			tipo = key[1]
			longitud_requerida = key[2]
			caracter_a_anadir = key[3]
			longitud_de_valor = len(valor)
			longitud_faltante = longitud_requerida - longitud_de_valor
		
			if longitud_de_valor != longitud_requerida:
				for caracter in range(longitud_faltante):
					nuevo_valor = caracter_a_anadir + vars(self)[campo]
					vars(self)[campo] = nuevo_valor
	
	def imprimir_linea(self):
		return self.campos_unidos


		