class Modelo_4:
	def __init__(self, inciales_de_compañia, numero_de_envio, fecha_de_envio, hora, nombre_de_importadora, numero_de_registro, hecha_de_fin_de_convenio) -> str:
		self.re = "RE"
		self.inciales_de_compañia = inciales_de_compañia
		self.numero_de_envio = numero_de_envio
		self.fecha_de_envio = fecha_de_envio
		self.hora = hora
		self.nombre_de_importadora = nombre_de_importadora
		self.numero_de_registro = numero_de_registro
		self.hecha_de_fin_de_convenio = hecha_de_fin_de_convenio
		self.espacios_en_blanco = ""
		self.asterisco = "*"
		self.numero_de_caracteres_en_blanco = 230
		self.numero_de_caracteres = 322
		self.caracter_de_edicion = " "
		self.campos_unidos = ""
		self.completar_nombre_de_importadora()
		self.completar_campo_espacios_en_blanco()
		self.juntar_campos()
	
	def __str__(self):
		return self.juntar_campos()
	
	def completar_nombre_de_importadora(self):
		longitud_inicial = len(self.nombre_de_importadora)
		longitud_restante = 50 - longitud_inicial
		caracteres_a_anadir = ""
		if longitud_inicial > -1:
			for x in range(longitud_restante):
				caracteres_a_anadir += self.caracter_de_edicion
			self.nombre_de_importadora += caracteres_a_anadir
		else:
			mensaje_de_error = "\"" + self.nombre_de_importadora + "\""
			mensaje_de_error += " No se conforma a la regla de 50 caracteres como máximo"

	def completar_campo_espacios_en_blanco(self):
		for x in range(self.numero_de_caracteres_en_blanco):
			self.espacios_en_blanco += self.caracter_de_edicion

	def juntar_campos(self):
		self.campos_unidos += self.re
		self.campos_unidos += self.inciales_de_compañia
		self.campos_unidos += self.numero_de_envio
		self.campos_unidos += self.fecha_de_envio
		self.campos_unidos += self.hora
		self.campos_unidos += self.nombre_de_importadora
		self.campos_unidos += self.numero_de_registro
		self.campos_unidos += self.hecha_de_fin_de_convenio
		self.campos_unidos += self.espacios_en_blanco
		self.campos_unidos += self.asterisco
		self.campos_unidos += "\n"

	def imprimir_linea(self):
		return self.campos_unidos