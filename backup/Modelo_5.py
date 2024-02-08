class Modelo_5:
	def __init__(
		self, 
		
		tipo_de_movimiento: str = "xx",
		numero_de_registro_correlativo_de_la_empresa: str = "0000000",
		numero_de_modificacion: str = "00",
		marca: str = "xxx",
			#(1) 1   espacio(s) de ( )
		serie: str = "xxxxxxxxxxxxxxx",
			#(2)  9   espacio(s) de ( ) 
		modelo: str = "xxxxxxxxxxxxxxx",
			#(3)  9   espacio(s) de ( ) 
		ano_modelo: str = "0000",
		serial_de_la_carroceria: str = "xxxxxxxxxxxxxxxxxx",
			#(4)  1   espacio(s) de ( ) 
		serial_del_motor: str = "xxxxxxxxxxxxxxxxxx",
			#(5)  7   espacio(s) de ( ) 
		placa: str = "xxxxxxx",
			#(6)  2   espacio(s) de ( ) 
		color_1: str = "xx",
		color_2: str = "xx",
		peso_tara: str = "00000",
		tipo_de_capacidad: str = "0",
		capacidad_de_carga: str = "00000",
		numero_de_ejes: str = "0",
		diametro_de_rueda: str = "000",
		clase: str = "xxx",
			#(7) 1   espacio(s)  de ( ) 
		tipo: str = "xxx",
			#(8)  1   espacio(s) de ( )
		uso: str = "xxx",
			#(9)  1   espacio(s) de ( )
		fecha_de_emision_del_certificado: str = "00000000",
		codigo_del_rif: str = "x",
		numero_del_rif: str = "00000000",
		digito_del_rif: str = "0",
		puerto_de_entrada: str = "xx",
		numero_de_la_planilla_de_liquidacion_de_gravamenes: str = "xxxxxxxxxxxxxxx",
		fecha_de_la_planilla_de_liquidacion_de_gravamenes: str = "00000000",
		numero_de_la_factura_de_adquisicion: str = "xxxxxxxxxxxxx",
			#(10)  6   espacio(s) de ( )
		fecha_de_la_factura_de_adquisicion: str = "00000000",
		numero_del_certificado_de_origen_preimpreso: str = "xxxxxxxxx",
		ano_de_fabricacion: str = "0000",
		serial_niv_numero_de_identificacion_vehicular: str = "xxxxxxxxxxxxxxxxx",
		serial_del_chasis: str = "xxxxxxxxxxxxxxxxx",
		numero_de_la_factura_1: str = "xxxxxxxxxxxxxxx",
			#(11)  9   espacio(s) de ( )
		fecha_de_la_factura_1: str = "00000000",
		numero_de_la_homologacion_intt: str = "xxxxxxxxxxxxxxx",
			#(12)  15  espacio(s) de ( ) coincide con numero_de_la_homologacion_intt
		fecha_de_la_homologacion_intt: str = "00000000",
		servicio: str = "xxx",
		numero_de_puestos: str = "000",
		numero_de_la_rafaga_de_la_placa_refeciv: str = "xxxxxxxx",
		fecha_de_la_rafaga: str = "00000000",
		numero_de_secuencia_de_rafaga: str = "00",
		serial_carrozado: str = "xxxxxxxxxxxxxxxxx",
			#(13)  17  espacio(s) de ( ) coincide con serial_carrozado
		tipo_de_combustible: str = "xxx",
			#(14)  1  espacio(s) de ( )

	) -> str:
		self.tipo_de_movimiento = tipo_de_movimiento
		self.numero_de_registro_correlativo_de_la_empresa = numero_de_registro_correlativo_de_la_empresa
		self.numero_de_modificacion = numero_de_modificacion
		self.marca = marca
		self.serie = serie
		self.modelo = modelo
		self.ano_modelo = ano_modelo
		self.serial_de_la_carroceria = serial_de_la_carroceria
		self.serial_del_motor = serial_del_motor
		self.placa = placa
		self.color_1 = color_1
		self.color_2 = color_2
		self.peso_tara = peso_tara
		self.tipo_de_capacidad = tipo_de_capacidad
		self.capacidad_de_carga = capacidad_de_carga
		self.numero_de_ejes = numero_de_ejes
		self.diametro_de_rueda = diametro_de_rueda
		self.clase = clase
		self.tipo = tipo
		self.uso = uso
		self.fecha_de_emision_del_certificado = fecha_de_emision_del_certificado
		self.codigo_del_rif = codigo_del_rif
		self.numero_del_rif = numero_del_rif
		self.digito_del_rif = digito_del_rif
		self.puerto_de_entrada = puerto_de_entrada
		self.numero_de_la_planilla_de_liquidacion_de_gravamenes = numero_de_la_planilla_de_liquidacion_de_gravamenes
		self.fecha_de_la_planilla_de_liquidacion_de_gravamenes = fecha_de_la_planilla_de_liquidacion_de_gravamenes
		self.numero_de_la_factura_de_adquisicion = numero_de_la_factura_de_adquisicion
		self.fecha_de_la_factura_de_adquisicion = fecha_de_la_factura_de_adquisicion
		self.numero_del_certificado_de_origen_preimpreso = numero_del_certificado_de_origen_preimpreso
		self.ano_de_fabricacion = ano_de_fabricacion
		self.serial_niv_numero_de_identificacion_vehicular = serial_niv_numero_de_identificacion_vehicular
		self.serial_del_chasis = serial_del_chasis
		self.numero_de_la_factura_1 = numero_de_la_factura_1
		self.fecha_de_la_factura_1 = fecha_de_la_factura_1
		self.numero_de_la_homologacion_intt = numero_de_la_homologacion_intt
		self.fecha_de_la_homologacion_intt = fecha_de_la_homologacion_intt
		self.servicio = servicio
		self.numero_de_puestos = numero_de_puestos
		self.numero_de_la_rafaga_de_la_placa_refeciv = numero_de_la_rafaga_de_la_placa_refeciv
		self.fecha_de_la_rafaga = fecha_de_la_rafaga
		self.numero_de_secuencia_de_rafaga = numero_de_secuencia_de_rafaga
		self.serial_carrozado = serial_carrozado
		self.tipo_de_combustible = tipo_de_combustible

		
		self.campos_unidos = ''
		self.completar_caracteres_en_campos()
		self.juntar_campos()
	
	def __str__(self):
		# return self.campos_unidos
		return "Clase \"Modelo_5\" instanciada correctamente."
	
	def juntar_campos(self):
		self.campos_unidos += str(self.tipo_de_movimiento)
		self.campos_unidos += str(self.numero_de_registro_correlativo_de_la_empresa)
		self.campos_unidos += str(self.numero_de_modificacion)
		self.campos_unidos += str(self.marca)
		self.campos_unidos += str(self.serie)
		self.campos_unidos += str(self.modelo)
		self.campos_unidos += str(self.ano_modelo)
		self.campos_unidos += str(self.serial_de_la_carroceria)
		self.campos_unidos += str(self.serial_del_motor)
		self.campos_unidos += str(self.placa)
		self.campos_unidos += str(self.color_1)
		self.campos_unidos += str(self.color_2)
		self.campos_unidos += str(self.peso_tara)
		self.campos_unidos += str(self.tipo_de_capacidad)
		self.campos_unidos += str(self.capacidad_de_carga)
		self.campos_unidos += str(self.numero_de_ejes)
		self.campos_unidos += str(self.diametro_de_rueda)
		self.campos_unidos += str(self.clase)
		self.campos_unidos += str(self.tipo)
		self.campos_unidos += str(self.uso)
		self.campos_unidos += str(self.fecha_de_emision_del_certificado)
		self.campos_unidos += str(self.codigo_del_rif)
		self.campos_unidos += str(self.numero_del_rif)
		self.campos_unidos += str(self.digito_del_rif)
		self.campos_unidos += str(self.puerto_de_entrada)
		self.campos_unidos += str(self.numero_de_la_planilla_de_liquidacion_de_gravamenes)
		self.campos_unidos += str(self.fecha_de_la_planilla_de_liquidacion_de_gravamenes)
		self.campos_unidos += str(self.numero_de_la_factura_de_adquisicion)
		self.campos_unidos += str(self.fecha_de_la_factura_de_adquisicion)
		self.campos_unidos += str(self.numero_del_certificado_de_origen_preimpreso)
		self.campos_unidos += str(self.ano_de_fabricacion)
		self.campos_unidos += str(self.serial_niv_numero_de_identificacion_vehicular)
		self.campos_unidos += str(self.serial_del_chasis)
		self.campos_unidos += str(self.numero_de_la_factura_1)
		self.campos_unidos += str(self.fecha_de_la_factura_1)
		self.campos_unidos += str(self.numero_de_la_homologacion_intt)
		self.campos_unidos += str(self.fecha_de_la_homologacion_intt)
		self.campos_unidos += str(self.servicio)
		self.campos_unidos += str(self.numero_de_puestos)
		self.campos_unidos += str(self.numero_de_la_rafaga_de_la_placa_refeciv)
		self.campos_unidos += str(self.fecha_de_la_rafaga)
		self.campos_unidos += str(self.numero_de_secuencia_de_rafaga)
		self.campos_unidos += str(self.serial_carrozado)
		self.campos_unidos += str(self.tipo_de_combustible)

	def imprimir_propiedades(self):
		for attr, value in vars(self).items():
			# print(f'{attr}: {value}')
			pass
	
	def completar_caracteres_en_campos(self):
		longitud_de_campos = [
			["tipo_de_movimiento", "str", 2, " " ,"pos"],
			["numero_de_registro_correlativo_de_la_empresa", "int", 7, "0", "pre"],
			["numero_de_modificacion", "int", 2, "0", "pre"],
			["marca", "str", 3, " " ,"pos"],
			["serie", "str", 15, " " ,"pos"],
			["modelo", "str", 15, " " ,"pos"],
			["ano_modelo", "int", 4, "0", "pos"],
			["serial_de_la_carroceria", "str", 18, " ", "pre"], #correccion aquí
			["serial_del_motor", "str", 18, " ", "pre"], #correccion aquí
			["placa", "str", 7, "0", "pre"],
			["color_1", "str", 2, "0", "pre"],
			["color_2", "str", 2, "0", "pre"],
			["peso_tara", "int", 5, "0", "pre"],
			["tipo_de_capacidad", "int", 1, "0", "pre"],
			["capacidad_de_carga", "int", 5, "0", "pre"],
			["numero_de_ejes", "int", 1, "0", "pre"],
			["diametro_de_rueda", "int", 3, "0", "pre"],
			["clase", "str", 3, " " ,"pos"],
			["tipo", "str", 3, " " ,"pos"],
			["uso", "str", 3, " " ,"pos"],
			["fecha_de_emision_del_certificado", "int", 8, "0", "pre"],
			["codigo_del_rif", "str", 1, "0", "pre"],
			["numero_del_rif", "int", 8, "0", "pre"],
			["digito_del_rif", "int", 1, "0", "pre"],
			["puerto_de_entrada", "str", 2, " " ,"pre"],
			["numero_de_la_planilla_de_liquidacion_de_gravamenes", "str", 15, "0", "pre"],
			["fecha_de_la_planilla_de_liquidacion_de_gravamenes", "int", 8, "0", "pre"],
			["numero_de_la_factura_de_adquisicion", "str", 15, " " ,"pos"],
			["fecha_de_la_factura_de_adquisicion", "int", 8, " " ,"pre"],
			["numero_del_certificado_de_origen_preimpreso", "str", 9, " " ,"pos"],
			["ano_de_fabricacion", "int", 4, " " ,"pre"],
			["serial_niv_numero_de_identificacion_vehicular", "str", 17, " ", "pre"],
			["serial_del_chasis", "str", 17, " ", "pre"],
			["numero_de_la_factura_1", "str", 15, " " ,"pos"],
			["fecha_de_la_factura_1", "int", 8, "0", "pre"],
			["numero_de_la_homologacion_intt", "str", 15, "0", "pre"],
			["fecha_de_la_homologacion_intt", "int", 8, "0", "pre"],
			["servicio", "str", 3, " " ,"pos"],
			["numero_de_puestos", "int", 3, "0", "pre"],
			["numero_de_la_rafaga_de_la_placa_refeciv", "str", 8, "0", "pre"],
			["fecha_de_la_rafaga", "int", 8, "0", "pre"],
			["numero_de_secuencia_de_rafaga", "int", 2, " " ,"pre"],
			["serial_carrozado", "str", 17, " ", "pre"],
			["tipo_de_combustible", "str", 3, "0", "pre"]
		]
		counter = 0	
		for key in longitud_de_campos:
			valor = vars(self)[key[0]]
			campo = key[0]
			tipo = key[1]
			longitud_requerida = key[2]
			caracter_a_anadir = key[3]
			posicion_de_caracter = key[4]
			longitud_de_valor = len(valor)
			longitud_faltante = longitud_requerida - longitud_de_valor
			
			if longitud_requerida != longitud_de_valor:
				for caracter in range(longitud_faltante):
					if posicion_de_caracter == "pre":
						nuevo_valor = caracter_a_anadir + vars(self)[campo]
						vars(self)[campo] = nuevo_valor						
					else:
						nuevo_valor = vars(self)[campo] + caracter_a_anadir
						vars(self)[campo] = nuevo_valor

			# if campo == "numero_de_la_homologacion_intt" or campo == "serial_carrozado":
			if campo == "numero_de_la_homologacion_intt":
				nuevo_valor = vars(self)[campo].replace("0", " ")
				vars(self)[campo] = nuevo_valor

			counter += 1

	def imprimir_linea(self):
		return self.campos_unidos