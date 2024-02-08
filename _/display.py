from Modelo_4 import Modelo_4
from Modelo_5 import Modelo_5
from Modelo_6 import Modelo_6
from obtener_datos_de_excel import obtener_datos_de_excel

modelo_4 = Modelo_4(
	"LU", # inciales_de_compañia
	"0000001", # numero_de_envio
	"20240125", # fecha_de_envio
	"041259", # hora
	"CSK MOTOS IMPORT C.A.", # nombre_de_importadora
	"MDMVP122", # numero_de_registro
	"20231231", # hecha_de_fin_de_convenio
)

modelo_5 = Modelo_5(
	
	"MA", # tipo_de_movimiento
	"1", # numero_de_registro_correlativo_de_la_empresa
	"00", # numero_de_modificacion
	"LIM", # marca
	"150", # serie
	"XS 150", # modelo
	"2023", # ano_modelo
	"L2YPCKLC8POLO4654", # serial_de_la_carroceria RELLENAR CON CEROS(0) AL PRINCIPIO HASTA 18 CARACTERES
	"162FMJ23204654", # serial_del_motor RELLENAR CON CEROS(0) AL PRINCIPIO HASTA 18 CARACTERES
	"AD0K02R", # placa
	"NR", # color_1
	"", # color_2
	"112", # peso_tara
	"2", # tipo_de_capacidad
	"150", # capacidad_de_carga
	"2", # numero_de_ejes
	"17", # diametro_de_rueda
	"MT", # clase
	"MT", # tipo
	"PR", # uso
	"20231213", # fecha_de_emision_del_certificado
	"J", # codigo_del_rif
	"50344463", # numero_del_rif
	"0", # digito_del_rif
	"PC", # puerto_de_entrada
	"C 386", # numero_de_la_planilla_de_liquidacion_de_gravamenes
	"20230812", # fecha_de_la_planilla_de_liquidacion_de_gravamenes
	"VE2023-00120", # numero_de_la_factura_de_adquisicion
	"20230803", # fecha_de_la_factura_de_adquisicion
	"AA0626326", # numero_del_certificado_de_origen_preimpreso
	"2023", # ano_de_fabricacion
	"L2YPCKLC8POLO4654", # serial_niv_numero_de_identificacion_vehicular |  RELLENAR CON CEROS(0) AL PRINCIPIO HASTA 18 CARACTERES | REPITE serial_de_la_carroceria
	"L2YPCKLC8POLO4654", # serial_del_chasis  RELLENAR CON CEROS(0) | AL PRINCIPIO HASTA 18 CARACTERES | REPITE serial_del_motor
	"A000001", # numero_de_la_factura_1
	"20231213", # fecha_de_la_factura_1
	"000000000000000", # numero_de_la_homologacion_intt
	"00000000", # fecha_de_la_homologacion_intt
	"S23", # servicio
	"2", # numero_de_puestos
	"MDMVP122", # numero_de_la_rafaga_de_la_placa_refeciv
	"20231231", # fecha_de_la_rafaga
	"01", # numero_de_secuencia_de_rafaga
	"00000000000000000", # serial_carrozado
	"006" # tipo_de_combustible
)

modelo_6 = Modelo_6(
	"196", # cantidad_de_registros_tipo_ma
	"0", # cantidad_de_registros_tipo_mm
	"0"  # cantidad_de_registros_tipo_me
)


# with open("archivo_INTT_Licet_Prueba_2.txt","w") as archivo:
# 	archivo.write(modelo_4.imprimir_linea())
# 	archivo.write("\n")
# 	archivo.write(modelo_5.imprimir_linea())
# 	archivo.write("\n")
# 	archivo.write(modelo_6.imprimir_linea())

# print("archivo \"archivo_INTT_Licet_Prueba_1\" creado exitosamente")
print(obtener_datos_de_excel("excel_de_prueba.xlsx"))

