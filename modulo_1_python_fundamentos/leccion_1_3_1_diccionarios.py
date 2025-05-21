print("--- Lección 1.3.1: Diccionarios - Creación y Acceso ---")

# --- Creación de Diccionarios
print("\n--- Creación de Dccionarios ---")

# Diccionario vacío
parametros_metodo_analitico = {}
print(f"Parámetros del método (inicialmente vacío): {parametros_metodo_analitico}")
print(f"Tipo de 'parametros_metodo_analitico': {type(parametros_metodo_analitico).__name__}")

# Dccionario con información de un excipiente
info_lactosa ={
    "nombre_comun" : "Lactosa Monohidrato",
    "funcion_principal" : "Diluyente, Aglutinante",
    "tipo_excipiente" : "Carbohidrato",
    "grado_farmaceutico" : True,
    "proveedores_aprobados" : ["PharmaExcipients Inc.", "ChemSupply Con"]  # Un valor puede ser una lista
}
print(f"\nInformación de la Lactosa:\n{info_lactosa}")

# Diccionario para almacenar resultados de estabilidad de un lote
# Clave: Tiempo (meses), Valor: Pureza (%)
estabilidad_lote_ABC = {
    0: 99.8,    # Tiempo 0 (inicial)
    3: 99.7,    # A los 3 meses
    6: 99.5,    # A los 6 meses
    12: 99.1    # A los 12 meses
}
print(f"\nResultados de Estabilidad del Lote ABC (Tiempo: Pureza %):\n{estabilidad_lote_ABC}")

# --- Acceso a valores usando Clavaes ---
print("\n--- Acceso a Valores (usando claves con []) ---")
# Usando info_lactosa
nombre_comun_lactosa = info_lactosa["nombre_comun"]
funcion_lactosa = info_lactosa["funcion_principal"]
print(f"Nombre común de la lactosa: {nombre_comun_lactosa}")
print(f"Función principal de la lactosa: {funcion_lactosa}")

# Acceder a un elemento de la lista dentro del diccionario
primer_proveedor_lactosa = info_lactosa["proveedores_aprobados"][0]  # Accede a la lista y luego al primer elemento
print(f"Primer proveedor aprobado de la lactosa: {primer_proveedor_lactosa}")

# Usando estabilidad_lote_ABC
pureza_a_los_6_meses = estabilidad_lote_ABC[6]
print(f"Pureza del Lote ABC a los 6 meses: {pureza_a_los_6_meses}")

# ¿Qué pasa si intentamos acceder a una clave que no existe con[]?
try:
    # solubilidad_lactosa = info_lactosa["solubilidad_agua"]    # Esta clave no existes
    print("Línea no alzanzada si la anterior da KeyError")
except KeyError as e:
    print(f"Error esperado al acceder a una clave inexistente con []: {e}")
    
# --- Acceso Seguro a Valores con el Método .get() ---
print("\n--- Acceso Seguro a Valores (con .get()) ---")
# Usando info_lactosa
solubilidad_lactosa_get = info_lactosa.get("solubilidad_agua")  # Clave no existe
print(f"Solubilidad en agua de la lactosa (con .get()): {solubilidad_lactosa_get}")

# Con un valor por defecto si la clave no existe
solubilidad_lactosa_get_defecto = info_lactosa.get("solubilidad_agua", "No_especificada")
print(f"Solubilidad en agua (con .get() y valor por defecto): {solubilidad_lactosa_get_defecto}")

# Accediendo a una clave que sí existe con .get

print("\n--- Diccionarios Farmacéuticos ---")

# 1. Información de un Paciente Simulado:
#    Crea un diccionario llamado `paciente_demo` con la siguiente información:
#    - "id_paciente": "PAC-ENSAYO-075"
#    - "edad_anios": 58
#    - "tratamiento_asignado": "Fármaco Experimental B"
#    - "presion_sistolica_basal": 145
#    - "alergias_conocidas": ["Penicilina", "Sulfamidas"] (una lista)
#    a) Imprime el diccionario completo.
#    b) Imprime la edad del paciente.
#    c) Imprime el tratamiento asignado.
#    d) Imprime la segunda alergia conocida del paciente (Sulfamidas).
#    e) Intenta imprimir el "peso_kg" del paciente usando `[]`. Maneja el `KeyError` con `try-except`.
#    f) Intenta imprimir el "peso_kg" del paciente usando `.get()` y proporciona "Dato no disponible" como valor por defecto.

paciente_demo = {
    "id_paciente" : "PAC-ENSAYO-075",
    "edad_anios" : 58,
    "tratamiento_asignado" : "Fármaco Experimental B",
    "presion_sistolica_basal" : 145,
    "alergias_conocida" : ["Penicilina", "Sulfamidas"]
}
print(f"\na) Información del Paciente Demo:\n{paciente_demo}")
print(f"b) Edad del paciente: {paciente_demo['edad_anios']} años")
print(f"c) Tratamiento asignado: {paciente_demo['tratamiento_asignado']}")
print(f"d) Segunda alergia concoida: {paciente_demo['alergias_conocida'][1]}")

try:
    peso_pac_ej1e = paciente_demo["peso_kg"]
    print(f"e) Peso del paciente (con[]): {peso_pac_ej1e}")
except KeyError:
    print(f"e) Error: La clave 'peso_kg' no existe en el dicionario del paciente")
    
peso_pac_ej1e = paciente_demo.get("peso_kg", "Dato no disponible")
print(f"f) Peso del paciente (con .get()): {peso_pac_ej1e}")

# 2. Parámetros de un Protocolo de Disolución:
#    Un protocolo tiene los siguientes parámetros:
#    - "medio_disolucion": "Buffer Fosfato pH 6.8"
#    - "volumen_medio_ml": 900
#    - "velocidad_agitacion_rpm": 75
#    - "tiempo_muestreo_min": [5, 10, 15, 30, 45, 60] (lista de minutos)
#    - "aparato_disolucion": "USP Aparato 2 (Paletas)"
#    a) Crea un diccionario `protocolo_disolucion_std` con estos datos.
#    b) Imprime el diccionario.
#    c) Accede e imprime el volumen del medio.
#    d) Accede e imprime el tercer tiempo de muestreo.
#    e) Usa `.get()` para intentar acceder a "temperatura_C" y si no existe, imprime "Temperatura no especificada".

protocolo_disolucion_std = {
    "medio_disolucion" : "Buffer Fosfato pH 6.8",
    "volumen_medio_mL" : 900,
    "velocidad_agitacion_rpm" : 75,
    "tiempo_muestreo_min" : [5, 10, 15, 30, 45, 60],
    "aparato_disolucion" : "USP Aparato 2 (Paletas)"
}
print(f"\na) Protocolo de Disolución Estándar:\n{protocolo_disolucion_std}")
print(f"b) (Ya impreso arriba)")
print(f"c) Volumen del Medio {protocolo_disolucion_std['volumen_medio_mL']} mL")
print(f"d) Tercer Tiempo de Muestreo: {protocolo_disolucion_std['tiempo_muestreo_min'][2]} min")

temperatura_protocolo_ej2e = protocolo_disolucion_std.get("temperatura_C", "Temperatura no especificada")
print(f"e) Temperatura del Protocolo: {temperatura_protocolo_ej2e}")

# 3. Define un diccionario `ficha_tecnica_api` para un Principio Activo Farmacéutico.
#    Debe incluir al menos las siguientes claves (con valores inventados por ti):
#    - "nombre_api" (string)
#    - "codigo_interno_api" (string, ej. "API-00XW")
#    - "masa_molecular_g_mol" (float)
#    - "punto_fusion_C" (float o string como "150-152 °C")
#    - "soluble_en" (lista de strings, ej. ["Agua", "Etanol"])
#    - "requiere_condiciones_especiales_almacenamiento" (booleano)
#    a) Crea el diccionario.
#    b) Imprime el diccionario completo.
#    c) Imprime solo el nombre del API y su masa molecular.
#    d) Imprime si requiere condiciones especiales de almacenamiento.
#    e) Imprime el primer solvente en el que es soluble.

ficha_tecnica_api = {
    "nombre_api" : "Paracetamol",
    "codigo_interno_api" : "API-PCM-001",
    "masa_molecular_g_mol" : 151.163,
    "punto_fusion_C" : "169-170 °C",
    "soluble_en" : ["Etanol", "Metanol", "Agua (parcialmente)"],
    "requiere_condiciones_especiales_almacenamiento" : False
}
print(f" a,b) Ficha Técnica Completa:\n{ficha_tecnica_api}")
print(f"c) Nombre API: {ficha_tecnica_api['nombre_api']}, Masa Molecular: {ficha_tecnica_api['masa_molecular_g_mol']} g/mol")
print(f"d) ¿Requiere Alm. Especial?: {ficha_tecnica_api['requiere_condiciones_especiales_almacenamiento']}")
print(f"e) Primer solvente de solubilidad: {ficha_tecnica_api['soluble_en'][0]}")

