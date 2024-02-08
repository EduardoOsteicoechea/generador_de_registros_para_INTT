from Modelo_4 import Modelo_4
from Modelo_6 import Modelo_6
from generar_registros_de_numeral_5 import generar_registros_de_numeral_5
from obtener_datos_de_excel import obtener_datos_de_excel

inciales_de_compañia = input("inciales de compañia: ")
numero_de_envio = input("numero de envio: ")
fecha_de_envio = input("fecha de envio: ")
hora = input("hora: ")
nombre_de_importadora = input("nombre de importadora: ")
numero_de_registro = input("numero de registro: ")
hecha_de_fin_de_convenio = input("hecha de fin de convenio: ")

modelo_4 = Modelo_4(
	inciales_de_compañia,
	numero_de_envio,
	fecha_de_envio,
	hora,
	nombre_de_importadora,
	numero_de_registro,
	hecha_de_fin_de_convenio
)

ruta_de_archivo = input("especifique la ruta del archivo .xlsx: ")
datos_de_archivo_xlsx = obtener_datos_de_excel(ruta_de_archivo)
registros_de_numeral_5 = generar_registros_de_numeral_5(datos_de_archivo_xlsx)

cantidad_de_registros_tipo_ma = input("cantidad de registros tipo ma: ")
cantidad_de_registros_tipo_mm = input("cantidad de registros tipo mm: ")
cantidad_de_registros_tipo_me = input("cantidad de registros tipo me: ")

modelo_6 = Modelo_6(
	cantidad_de_registros_tipo_ma,
	cantidad_de_registros_tipo_mm,
	cantidad_de_registros_tipo_me,
)

nombre_de_archivo_a_generar = input("nombre de archivo a generar: ")


with open(nombre_de_archivo_a_generar + ".txt","w") as archivo:
	archivo.write(modelo_4.imprimir_linea())
	archivo.write(registros_de_numeral_5)
	archivo.write(modelo_6.imprimir_linea())

print("archivo \"" + nombre_de_archivo_a_generar + "\" creado exitosamente")






