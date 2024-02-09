from Modelo_4 import Modelo_4
from generar_registros_de_numeral_5_y_6 import generar_registros_de_numeral_5_y_6
from obtener_datos_de_excel import obtener_datos_de_excel

print("Creador de registros para carga de origen importado y nacional en Venezuela.")
print("Versión 1.0.0.")
print("Desarollado por Eduardo Osteicoechea en febrero del 2024.")
print("Este programa posee garantía hasta mayo del 2024.")
print("Para mantenimiento y actualización contáctame a eduardooost@gmail.com.")
print("\n")
print("Genera los registros siguiendo las indicaciones que encontrarás más abajo: ")
print("\n")

inciales_de_compañia = input("Inciales de compañia: ")
numero_de_envio = input("Numero de envio: ")
fecha_de_envio = input("Fecha de envio: ")
hora = input("Hora: ")
nombre_de_importadora = input("Nombre de importadora: ")
numero_de_registro = input("Número de registro: ")
fecha_de_fin_de_convenio = input("Fecha de fin de convenio: ")

registros_de_numeral_4 = Modelo_4(
	inciales_de_compañia,
	numero_de_envio,
	fecha_de_envio,
	hora,
	nombre_de_importadora,
	numero_de_registro,
	fecha_de_fin_de_convenio
).imprimir_linea()

ruta_de_archivo = input("Ruta del archivo .xlsx: ")
datos_de_archivo_xlsx = obtener_datos_de_excel(ruta_de_archivo)
registros_de_numeral_5_y_6 = generar_registros_de_numeral_5_y_6(datos_de_archivo_xlsx)

nombre_de_archivo_a_generar = input("Nombre de archivo a generar: ")

with open(nombre_de_archivo_a_generar + ".txt","w") as archivo:
	archivo.write(registros_de_numeral_4)
	archivo.write(registros_de_numeral_5_y_6)

print("\n")
print("Archivo \"" + nombre_de_archivo_a_generar + ".txt\" creado exitosamente.")
print("Ubique el archivo \"" + nombre_de_archivo_a_generar + ".txt\" en la misma carpeta donde ejecutó este programa.")
input("Presione la tecla \"enter\" o \"esc\" para culminar.")
print("\n")






