from pyinstaller_setuptools import setup

setup(
    name = "REG_INTT",
    options={
        "build_exe": {
            "icon": "icon.ico"
        }
    },
    version = "1.0.0",
    description = 'Este es un programa para extraer, procesar, preparar, formatear y generar registros de motos en un archivo .txt, apartir de un archivo .xlsx formateado de acuerdo al manual de muestra compartido junto con el ejecutable de este programa para importación de motos de acuerdo al numeral 4,5 y 6 del documento de estructura y diseño de archivo de carga de origen para empresas bajo convenio, que está vigente en la fecha 2024-02-08',
	 scripts=['generar_registro.py'],
    entry_points={
        'console_scripts': ['entry=generar_registro.py']
    },
	 py_modules=['obtener_datos_de_excel', 'generar_registro', 'generar_registros_de_numeral_5', 'Modelo_4', 'Modelo_5', 'Modelo_6'],
)