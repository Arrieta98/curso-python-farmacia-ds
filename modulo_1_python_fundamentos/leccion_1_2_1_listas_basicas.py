print("--- Lección 1.21.: Listas - Creación y Acceso ---")

print("\n--- Creación de Listas ---")

# Lista de nombres de disolventes comunes en laboratorio
disolventes_comunes = [
	"Agua purificada",
	"Etanol",
	"Metanol",
	"Acetona",
	"Isopropanol"
]
print(f"Disolventes comunes: {disolventes_comunes}")
print(f"Tipo de disolvente_comunes: {type(disolventes_comunes).__name__}")

# Lista de mediciones de PH de varias muestras de un lote
mediciones_ph_lote_actual = [7.02, 6.98, 7.05, 7.01, 6.99, 7.03, 7.00]
print(f"Mediciones de ph del lote: {mediciones_ph_lote_actual}")

# Lista de número de comprimidos por envase para diferentes presentaciones
unidades_por_preparacion = [10, 20, 30, 50, 100]
print(f"Unidades por presentación: {unidades_por_preparacion}")

# Lista vacía para almacenar resultados de pruebas de estabilidad
resultados_estabilidad_farmaco_x = []
print(f"Resultados de estabilidad (inicialmente vacía): {resultados_estabilidad_farmaco_x}")

# Lista con tipos de datos mixtos (menos común para análisis directos, pero posible)
info_muestra_analitica = ["ID-MUESTRA-007A", 25.3, "C", True, "Analizar pureza"]  # ID, Temp, Unidad, Analizada?, Notas
print(f"Información mixta de muestra: {info_muestra_analitica}")

print("\n--- Acceso a Elementos (Indexación) ---")
# Usando la lista 'disolventes_comunes'
# Índices:                0                 1        2          3          4
# disolventes_comunes = ["Agua Purificada", "Etanol", "Metanol", "Acetona", "Isopropanol"]
# Índices negativos:     -5                -4       -3         -2         -1

primer_disolvente = disolventes_comunes[0]
segundo_disolvente = disolventes_comunes[1]
tercer_disolvente = disolventes_comunes[2]
ultimo_disolvente = disolventes_comunes[-1]
penultimo_disolvente = disolventes_comunes[-2]

print(f"Primer disolvente: {primer_disolvente}")
print(f"Segundo disolvente: {segundo_disolvente}")
print(f"Tercer disolvente: {tercer_disolvente}")
print(f"Último disolvente: {ultimo_disolvente}")
print(f"Penúltimo disolvente: {penultimo_disolvente}")

# Acceder a un elemento de la lista pH
segunda_medicion_ph = mediciones_ph_lote_actual[1]
print(f"Segunda medición de pH: {segunda_medicion_ph}")

print("\n--- Slicing de Listas ---")
# Usando 'mediciones_ph_lote_actual' = [7.02, 6.98, 7.05, 7.01, 6.99, 7.03, 7.00]
# Índices:                               0     1     2     3     4     5     6

# Primeras tes mediciones (índices 0, 1, 2)
primeras_tres_mediciones = mediciones_ph_lote_actual[:3]
print(f"Primeras tres mediciones de pH: {primeras_tres_mediciones}")

# Mediciones desde el índice 3 hasta el final
mediciones_tardias = mediciones_ph_lote_actual[3:]
print(f"Mediciones tardias: {mediciones_tardias}")

# Mediciones entre el índice 1 (incluido) y el 5 (excluido -> índices 1, 2, 3, 4)
mediciones_intermedias = mediciones_ph_lote_actual[1:5]
print(f"Mediciones de pH intermedias (índices 1 a 4): {mediciones_intermedias}")

# Todas las mediciones con un paso de 2 (elemtos en índices 0, 2, 4, 6)
mediciones_alternas_ph = mediciones_ph_lote_actual[::2]
print(f"Mediciones de pH alternas: {mediciones_alternas_ph}")

# Crear una copia de la lista usando slicing
copia_mediciones_ph = mediciones_ph_lote_actual[:]
print(f"Copia de las mediciones de pH: {copia_mediciones_ph}")
# Modificamos la copia para ver que la original no cambia (lo veremos más en mutabilidad)
copia_mediciones_ph[0] = 9.99
print(f"Copia modificada: {copia_mediciones_ph}")
print(f"Original SIN modificar: {mediciones_ph_lote_actual}")

# --- Longitud de una Lista (len()) ---
print("\n--- Longitud de una Lista (len()) ---")
numero_de_disolventes = len(disolventes_comunes)
print(f"Hay {numero_de_disolventes} disolventes comunes en la lista.")

numero_mediciones_ph = len(mediciones_ph_lote_actual)
print(f"Hay {numero_mediciones_ph} mediciones de pH para el lote.")

print("\n--- Listas Farmacéuticas ---")

fases_ensayo_clinico = [
    "Descubrimiento", "Preclínica", "Fase I" , "Fase II",
    "Fase III", "Aprobación Regulatoria", "Fase IV (Post-comercialización)"
]
print(f"\na) Etapas del Ensayo Clínico: {fases_ensayo_clinico}")
print(f"b) Número total de etapas: {len(fases_ensayo_clinico)}")
print(f"c) Primera etapa: {fases_ensayo_clinico[0]}")
print(f"d) Última etapa: {fases_ensayo_clinico[-1]}")
# Fase I es índice 2, Fase II es 3, Fase III es 4. Queremos slice hasta el índice 5 (excluido)
etapas_desarrollo_clinico_principal = fases_ensayo_clinico[2:5]
print(f"e) Etapas de desarrollo clínico principal: {etapas_desarrollo_clinico_principal}")

# 2. Resultados de un Test de Disolución:
#    Un fármaco se prueba en 6 vasos de disolución. Los porcentajes de fármaco disuelto a los 30 minutos son:
#    [85.2, 88.1, 83.5, 90.3, 86.7, 84.9]
#    Crea una lista `resultados_disolucion_30min` con estos valores.
#    a) Imprime la lista.
#    b) Imprime el resultado del primer vaso.
#    c) Imprime los resultados de los vasos 2, 3 y 4 (usando slicing).
#    d) Imprime el resultado del último vaso.

resultados_dilucion_30min = [85.2, 88.1, 83.5, 90.3, 86.7, 84.9]
print(f"\na) Resultado de Disolución a 30 min (%): {resultados_dilucion_30min}")
print(f"b) Resultado del primer vaso: {resultados_dilucion_30min[0]}")
# Vaso 2 es índice 1, Vaso 3 es índice 2, Vaso 4 es índice 3. Slice hasta índice 4 (excluido)
print(f"c) Resultado de los vasos 2, 3 y 4: {resultados_dilucion_30min[1:4]}")
print(f"d) Resultado del último vaso: {resultados_dilucion_30min[-1]} %")

# 3. Lista de Temperaturas de Almacenamiento Registradas:
#    Durante 5 días se registraron las siguientes temperaturas máximas en un almacén de medicamentos:
#    [22.5, 23.1, 21.9, 22.8, 24.0] (grados Celsius)
#    Crea una lista `temperaturas_max_almacen`.
#    a) Imprime la lista y cuántas mediciones se hicieron.
#    b) Imprime la temperatura del primer día y del tercer día.
#    c) Usando slicing, crea e imprime una nueva lista `ultimas_dos_temperaturas` que contenga las
#       temperaturas de los dos últimos días.

temperaturas_max_almacen = [22.5, 23.1, 21.9, 22.8, 24.0]
print(f"\na) Temperaturas máximas registradas (°C): {temperaturas_max_almacen}")
print(f"    Número de mediciones de temperaturas: {len(temperaturas_max_almacen)}")
print(f"b) Temperatura del primer días: {temperaturas_max_almacen[0]} °C")
print(f"    Temperatura del tercer día {temperaturas_max_almacen[2]} °C")
print(f"c) Últimas dos temperaturas registradas: {temperaturas_max_almacen[-2:]}")

