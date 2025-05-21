print("--- Lección 1.1. Strings ---")

# Metodos de Cambio de Mayústculas/Minúsculas ---
print("\n--- Mayúsculas/Minúsculas ---")
nombre_farmaco_original = "iBuPrOfEnO SÓDICO"
print(f"Original: '{nombre_farmaco_original}'")
print(f"upper(): '{nombre_farmaco_original.upper()}'")
print(f"lower(): '{nombre_farmaco_original.lower()}'")
print(f"capitalize(): '{nombre_farmaco_original.capitalize()}'")
print(f"title(): '{nombre_farmaco_original.title()}'")

# --- Eliminación de Espacios en Blanco ---
print("\n--- Eliminación de Espacios (strip) ---")
codigo_lote_con_espacios = " LOTE-ABC-001 \n"  # Espacios y salto de línea
print(f"Original con espacios: '{repr(codigo_lote_con_espacios)}'")
print(f"strip(): {repr(codigo_lote_con_espacios.strip())}")
print(f"lstrip(): {repr(codigo_lote_con_espacios.lstrip())})")
print(f"rstrip(): {repr(codigo_lote_con_espacios.rstrip())}")

# strip también puede quitar caracteres específicos
nombre_protocolo_sucio = "***PROTOCOLO-VALIDACION###"
print(f"Protocolo sucio: '{nombre_protocolo_sucio}'")
print(
	f"Limpio: (quitando '*' y '#'): "
	f"{repr(nombre_protocolo_sucio.strip('*#'))}"
)

# --- Búsqueda y Conteo ---
print("\n--- Búsqueda y Conteo ---")
descripcion_muestra = (
	"Muestra de suero sanguíneo para análisis de electrolitos y glucosa"
)
print(f"Descripción: {repr(descripcion_muestra)}")
print(
	"descripción_muestra_startswith('Muestra'): "
	f"{descripcion_muestra.startswith('Muestra')}"
)
print(
	"descripción_muestra_startswitch('Plasma'): "
	f"{descripcion_muestra.startswith('Plasma')}"
)
print(
	"descripción_de_la_muestra.endsswith('glucosa.'): "
	f"{descripcion_muestra.endswith('glucosa.')}"
)

subcadena_buscar = "análisis"
indice_encontrado_find = descripcion_muestra.find(subcadena_buscar)
print(f"{repr(subcadena_buscar)} con find(): {indice_encontrado_find}")  # Si no, devuelve -1

subcadena_no_existe = "proteínas"
indice_no_encontrado_find = descripcion_muestra.find(subcadena_no_existe)
print(
	f"{repr(subcadena_no_existe)} con find(): {indice_no_encontrado_find}"
)  # -1

try:
	indice_encontrado_index = descripcion_muestra.index(subcadena_buscar)
	print(
		f"{repr(subcadena_buscar)} encontrada con index() en índice: "
		f"{indice_encontrado_index}"
		)
	# indice_no_encontrado_index = descripcion_muestra.index(subcadena_no_existe)  # Esto daría ValueError
except ValueError as e:
	print(f"Error con index() al buscar {repr(subcadena_no_existe)}: {e}")

print(
    "Número de veces que aparece 'a' (minúscula:): "
    f"{descripcion_muestra.count('a')}"
    )
print(
    "Número de veces que aparece 'análisis': "
    f"{descripcion_muestra.count('análisis')}"
)
# --- Reemplazo ---
print("\n---Reemplazo (replace ---)")
protocolo_version_antigua = "PNT-QC-001-Rev01"
protocolo_version_nueva = protocolo_version_antigua.replace("Rev01", "Rev02")
print(
    f"Protocolo antiguo: {repr(protocolo_version_antigua)} "
    f"Nuevo: {repr(protocolo_version_nueva)}" 
)

descripcion_efecto_adverso = "El paciente reportó dolor de cabeza leve y mareo leve."
# Reemplazar solo la primera ocurrencia de "leve"
descripcion_modificada_ea = descripcion_efecto_adverso.replace(
    'leve', 'MODERADO', 1
)
print(f"Descipción EA modificada (1er 'leve'): {repr(descripcion_modificada_ea)}")

# --- División (split) y Unión (join) ---
print("\n--- División (split y Unión (join) ---")
lista_excipientes_str = "Lactosa,Almidón de Maíz,Estearato de Magnesio,Dióxido de Silicio"
lista_excipientes_lista = lista_excipientes_str.split(',')
print(f"String de excipientes: {repr(lista_excipientes_str)}")
print(f"Lista de excipientes (después de split): {lista_excipientes_lista}")

# Unir la lista de nuevo con un separador diferente
excipientes_unido_con_guion = "-".join(lista_excipientes_lista)
print(f"Excipientes unidos con '-': {excipientes_unido_con_guion}")

frase_con_espacios = "  Este  es  un  texto  con  muchos  espacios  "
palabras_frase = frase_con_espacios.split()
print(f"Frase original: {repr(frase_con_espacios)}")
print(f"Palabras divididas (split sin argumento): {palabras_frase}")
frase_reconstruida = " ".join(palabras_frase)
print(f"Frase reconstruida: {repr(frase_reconstruida)}")

# --- Compprobación de Tipo de Caracteres ---
print("\n--- Comprobación de Tipo de Caracteres ---")
codigo_numerico_lote = "2025001"
codigo_alafanumerico_lote = "LOTE2025A"
nombre_farmaco_solo_letras = "Aspirina"
string_con_espacios = "   "

print(f"{repr(codigo_numerico_lote)}.isdigit(): {codigo_numerico_lote.isdigit()}")
print(f"{repr(codigo_alafanumerico_lote)}.isdigit: {codigo_alafanumerico_lote.isdigit()}")
print(f"{repr(codigo_alafanumerico_lote)}.isalnum(): {codigo_alafanumerico_lote.isalnum()}")
print(f"{repr(nombre_farmaco_solo_letras)}.isalpha(): {nombre_farmaco_solo_letras.isalpha()}")
print(f"{repr(nombre_farmaco_solo_letras)}.islower(): {nombre_farmaco_solo_letras.islower()}")
print(f"'aspirina'.islower(): {'aspirina'.islower()}")
print(f"'Aspirina'.isupper(): {'ASPIRINA'.isupper()}")
print(f"{repr(string_con_espacios)}.isspace(): {string_con_espacios.isspace()}")
print(f"'Título De Ejemplo'.istitle(): {'Título De Ejemplo'.istitle()}")

# --- Formateo Avanzado con f-strings ---
print("\n--- Formateo Avanzado con f-strings ---")
id_muesta_num_7 = 7
concentración_medida = 12.3456789  # mcg/mL
pureza_porc = 98.7

# Formatear un entero para que tenga un ancho mínimo, rellenado con ceros
# :03d significa entero (d) de 3 digitos, rellenar con 0 si es necesario
id_muestra_formatedo = f"MUESTRA-{id_muesta_num_7:03d}"
print(f"{id_muesta_num_7} formateado: {id_muestra_formatedo}")

# Formatear un float con ancho total y alineación
# :>10.2f significa alinear a la derecha (>) en un campo de 10 caracteres, con 2 decimales

print(
	"Concentración (ancho 10, alin. derecha, 2 dec:):"
	f"{concentración_medida:>7.2f}"
)
# Formatear como porcentaje
# :.1% significa multiplicar por 100, añadir '%' y mostrar 1 decimal
proporcion_activa = 0.987
print(
    "Proporción activa como porcentaje (1 decimal):"
    f"{proporcion_activa:.1%}"
)
# Formateo con notación científica
# :.3e significa notación científica (e) con 3 decimales después del punto
valor_muy_pequeño = 0.00000012345
print(f"Valor muy pequeño (notación científica, 3 dec): { valor_muy_pequeño:.3e}")

print("\n-- Limpieza y Formateado Avanzado ---")

# 1. Normalización de Nombres de Principios Activos:
#    Tienes una lista de nombres de fármacos que vienen de diferentes fuentes, con mayúsculas/minúsculas
#    y espacios inconsistentes. Normalízalos todos a:
#    - Todo en minúsculas.
#    - Sin espacios al principio o al final.
nombres_sucios_pa = ["  paracetamol ", "IBUPROFENO SÓDICO", " Ácido Acetilsalicílico   ", "metformina HCL"]
nombres_limpios_pa = []
for nombre_sucio in nombres_sucios_pa:
    nombre_limpio = nombre_sucio.lower().strip()
    nombres_limpios_pa.append(nombre_limpio)
print(f"1. Nombres de P.A. sucios: {nombres_sucios_pa}")
print(f"    Nombres de P.A. limpios: {nombres_limpios_pa}")

# 2. Extracción de Datos de un Código de Lote Complejo:
#    Un código de lote tiene el formato: "PAIS_PLANTA_PRODUCTOABREV_AÑOMES_SECUENCIAL"
#    Ejemplo: "ESP_MAD_AMOXI500_202505_0017B"
#    Debes extraer: PAIS, PLANTA, PRODUCTOABREV, AÑOMES, SECUENCIAL
#    Usa .split('_') y luego manipula las partes si es necesario.
codigo_lote_complejo_ej2 = "ESP_MAD_AMOXI500_202505_0017B"
partes_lote_ej2 = codigo_lote_complejo_ej2.split('_')
if len(partes_lote_ej2) == 5:
    pais_ej2 = partes_lote_ej2[0]
    planta_ej2 = partes_lote_ej2[1]
    producto_abrev_ej2 = partes_lote_ej2[2]
    aniomes_ej2 = partes_lote_ej2[3]
    secuencial_ej2 = partes_lote_ej2[4]
    print(f"\n2. Desgloce del código de lote {codigo_lote_complejo_ej2}")
    print(f"    País: {pais_ej2}")
    print(f"    Planta: {planta_ej2}")
    print(f"    Producto (Abrev.): {producto_abrev_ej2}")
    print(f"    AñoMes: {aniomes_ej2}")
    print(f"    Secuencial: {secuencial_ej2}")
else:
    print(f"\n2. El código de lote {repr(codigo_lote_complejo_ej2)} no teine el formato esperado")
 
# 3. Crear un Reporte de Resultados Formateado:
#    Tienes los resultados de un análisis:

parametro_analizado_ej3 = "Contenido de API"
valor_obtenido_ej3 = 99.758
limite_inferior_ej3 = 98.5
limite_superior_ej3 = 101.5
unidad_ej3 = "%"

#    Genera un string de reporte de una sola línea formateado así (presta atención al alineamiento y decimales):
#    "Análisis: Contenido de API | Resultado:  99.76 % | Especificación: [ 98.50 % - 101.50 %] | Estado: CUMPLE"
#    (El estado es "CUMPLE" si está dentro de los límites, "NO CUMPLE" si no).
# TU CÓDIGO AQUÍ para generar 'reporte_linea_ej3' e imprimirla.

estado_ej3 = "CUMPLE" if (limite_inferior_ej3 <= valor_obtenido_ej3 <= limite_superior_ej3) else "NO CUMPLE"
reporte_linea_ej3 = (
    f"Análisis: {parametro_analizado_ej3:<20} | "
    f"Resultado: {valor_obtenido_ej3:>7.2f} {unidad_ej3} | "
    f"Especificación: [{limite_inferior_ej3:>6.2f} {unidad_ej3} - {limite_inferior_ej3:>6.2f} {unidad_ej3}] | "
    f"Estado: {estado_ej3}"
)
print(f"\n3. Reporde de Resultados:\n  {reporte_linea_ej3}")

# 4. (Ejercicio para ti) Validación de Formato de ID de Paciente:
#    Un ID de paciente válido debe:
#    a) Empezar con "PAC-"
#    b) Seguido de exactamente 5 dígitos numéricos.
#    c) Ejemplo válido: "PAC-12345", Ejemplo inválido: "PAC-123A5", "PA-12345", "PAC-1234"
#    Escribe una función (o simplemente el código aquí) que tome un string `id_paciente_test`
#    y devuelva/imprima True si es válido, False si no.
#    (Pistas: usa .startswith(), slicing, len(), y .isdigit())

ids_paciente_prueba_ej4 = ["PAC-12345", "PAC-123A5", "PA-12345", "PAC-1234", "PAC-123456", "PAC-ABCDE"]
print("\n4. Validación de IDs de Pacientes:")
for id_pac_test in ids_paciente_prueba_ej4:
    es_valido_ej4 = False  # Asumir que no es válido al inicio
    if id_pac_test.startswith("PAC-"):
        parte_numerica = id_pac_test[4:]  # Obtener la parte después de "PAC-"
        if len(parte_numerica) == 5 and parte_numerica.isdigit():
            es_valido_ej4 = True
    print(f"    ID {id_pac_test}: ¿Válido? {es_valido_ej4}")