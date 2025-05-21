print("--- Lección 1.2.4: Tuplas ---")

print("\n--- Creación de Tuplas ---")
# Coordenadas de un punto de muestreo fijo (x, y, profundidad_cm)
punto_muestreo_A1 = (10.5, 22.3, 15.0)
print(f"Punto de muestreo A1 (coordenadas): {punto_muestreo_A1}")
print(f"Tipo de 'punto_muestreo_A1': {type(punto_muestreo_A1).__name__}")

# Información de un fármaco de referencia (Nombre, Lote Referencia, Pureza Nominal %)
farmaco_referencia_ibu = ("Ibuprofeno Base", "REF-IBU-001", 99.8)
print(f"Fármaco de Referencia: {farmaco_referencia_ibu}")

# Tupla vacía
config_vacia = ()
print(f"Configuración Vacía: {config_vacia}, Longitud: {len(config_vacia)}")

# Tuplac con un solo elemento (¡la coma escrucial!)
parametro_critico_temp = (25.0,)
print(f"Parámetro Crítico (Temperatura): {parametro_critico_temp}, Tipo {type(parametro_critico_temp).__name__}")

no_es_una_tupla = (25.0)  # Esto es simplemente un float entre paréntesis
print(f"Valor entre paréntesis (no tupla): {no_es_una_tupla}, Tipo {type(no_es_una_tupla).__name__}")

# Creación sin paréntesis (menos explícito, pero funciona)
constantes_fisicas = 3.14159, 9.81 # (pi, gravedad)
print(f"Constantes Físicas: {constantes_fisicas}, Tipo: {type(constantes_fisicas)}")

# --- Acceso a Elementos (Indexación y Slicing) ---
print("\n--- Acceso (Indexación y Slicing) ---")
# Usando farmaco_referencia_ibu = ("Ibuprofeno Base", "REF-IBU-001", 99.8)
# Índices:                               0                1            2
nombre_ref = farmaco_referencia_ibu[0]
pureza_ref = farmaco_referencia_ibu[2]
print(f"Nombre del Fármaco de Referencia: {nombre_ref}")
print(f"Pureza Nominal del Fármaco de Referencia: {pureza_ref}%")

# Slicing (devuelve una nueva tupla)
info_identificacion_ref = farmaco_referencia_ibu[:2]  # Nombres y lote
print(f"Información de Identificación (slice): {info_identificacion_ref}")

# --- Inmutabilidad (¡La Característica Clave!) ---
print("\n--- Inmutabilidad ---")
# Si intentamos modificar un elemento de la tupla, dará error:
try:
    punto_muestreo_A1[0] = 11.0 # Descomenta esta línea para ver el TypeError
    print("Este mensaje no se imprimirá si la línea anterior está descomentada")
except TypeError as e:
    print(f"Error al intenrar modificar una tupla: {e}")
# Si necesitas "modificar" una tupla, debes crear una nueva.
# Ej: "Actualizar" la pureza del fármaco de referencia (creando una nueva tupla)
farmaco_referencia_ibu_actualizado = (
    farmaco_referencia_ibu[0],  # Nombre (sin cambios)
    farmaco_referencia_ibu[1],  # Lote (sin cambios)
    99.9   # Nueva pureza
)
print(f"Fármaco de Referencia Original: {farmaco_referencia_ibu}")
print(f"Farmaco de referencia 'Actualizado' (nuva tupla): {farmaco_referencia_ibu_actualizado}")

# --- Operaicones Comunes (len, in, +, *) ---
print("\n--- Operaciones Comunes ---")
rgb_color_alerta_rojo = (255, 0, 0)
print(f"Color RGB para alerta roja: {rgb_color_alerta_rojo}")
print(f"Número de componentes en el color RGB: {len(rgb_color_alerta_rojo)}")

if 0 in rgb_color_alerta_rojo:
    print("El comoponente '0' (ausencia de verde/azul) está en el color rojo.")
    
# Concatenación (crea una nueva tupla)
coordenas_xy = (10.5, 22.3)
coordenas_z = (15.0,) # ¡No olvidar la coma para que sea una tupla!
coordenadas_xyz = coordenas_xy + coordenas_z
print(f"Coordenadas XYZ (concatenadas): {coordenadas_xyz}")

# Repetición (crea una nueva tupla)
patron_repetido_qc = ("PASO", "FALLO") * 3
print(f"Patrón de QC repetido: {patron_repetido_qc}")

# --- Métodos .count() y .index() ---
conteo_paso = patron_repetido_qc.count("PASO")
print(f"Número de ocurrencias de 'PASO': {conteo_paso}")

try:
    primer_indice_fallo = patron_repetido_qc.index("FALLO")
    print(f"Primera ocurrencia de 'Fallo' está en el índice: {primer_indice_fallo}")
except ValueError:
    print("'Fallo' no encontrado (esto no debería pasar aquí).")
    
# --- Desempaquetado de Tuplas (Tuple Unpacking) ---
print("\n--- Desempaquetado de Tuplas ---")
# Usando farmaco_referencia_ibu_actualizado = ('Ibuprofeno Base', 'REF-IBU-001', 99.9)
nombre, lote, pureza = farmaco_referencia_ibu_actualizado  # Desempaquetando

print(f"Nombre (desempaquetado): {nombre}")
print(f"Lote (desempaquetado): {lote}")
print(f"Pureza (desempaquetada): {pureza}")

# Útil para devolver múltiples valores de una función (visto en Lección 1.5.3)
def obtener_limites_especificacion_ph():
    """Devuelve los límies inferior y superior para el pH."""
    lim_inf = 6.8
    lim_sup = 7.2
    return lim_inf, lim_sup  # Python empaqueta esto como una tupla (6.8, 7.2)

ph_min, ph_max = obtener_limites_especificacion_ph()  # Desempaquetado al recibir
print(f"Límites de especificación de Ph obtenidos de función: Min = {ph_min}, Max = {ph_max}")

print("\n--- Tuplas Farmacéuticas ---")

# 1. Parámetros Fijos de un Método Analítico:
#    Un método HPLC tiene parámetros fijos: ("Columna C18", "Fase Móvil ACN:Buffer (60:40)", 1.0, 30)
#    Representando (Tipo de Columna, Composición Fase Móvil, Flujo (mL/min), Temperatura Columna (°C))
#    a) Crea una tupla `params_hplc_metodo1` con estos valores.
#    b) Imprime la tupla.
#    c) Accede e imprime el tipo de columna y el flujo.
#    d) Intenta cambiar la temperatura a 35 (debería dar error, pero ponlo en un try-except para demostrar inmutabilidad).

params_hplc_metod1 = ("Columna C18", "Fase Móvil ACN:Buffer (60:40)", 1.0, 30)
print(f"\na) Párametros HPLC Método 1: {params_hplc_metod1}")
print(f"b) (Ya impreso arriba)")
print(f"c) Tipo de Columna: {params_hplc_metod1[0]}, Flujo: {params_hplc_metod1[2]} mL/min")

try:
    # params_hplc_metodo1[3] = 35  # Esto daría error
    print("d) (Línea de modificación comentada para evitar que el script se detenga)")
    # Para demostrar, podríamos intentar crear una nueva tupla si quisiéramos "cambiarla"
    # params_hplc_metodo1_mod = params_hplc_metodo1[:3] + (35,)
    # print(f"   Tupla 'modificada' (nueva tupla): {params_hplc_metodo1_mod}")
except TypeError as e:
    print(f"d) Error esperado al intentar modificar la tupla: {e}")
    
# 2. Devolver Resultados Múltiples de una "Validación":
#    Crea una función `validar_temperatura_almacen(temp_actual, temp_min, temp_max)` que:
#    - Reciba la temperatura actual, un mínimo y un máximo.
#    - Devuelva una tupla: (booleano_validez, mensaje_string).
#      - `booleano_validez` es True si temp_actual está entre min y max (inclusive), False si no.
#      - `mensaje_string` es "Temperatura OK" o "ALERTA: Temperatura fuera de rango".
#    a) Define la función.
#    b) Llama a la función con algunos valores de prueba (ej. temp_actual=4.5, min=2, max=8) y
#       desempaqueta los resultados en dos variables.
#    c) Imprime las dos variables desempaquetadas.
#    d) Llama a la función con una temperatura fuera de rango (ej. temp_actual=1.5) y haz lo mismo.

def validar_temperatura_almacen(temp_actual, tem_min, temp_max):
    """Valida si la temperatura actual está dentro del rango min/max."""
    if tem_min <= temp_actual <= temp_max:
        validez = True
        mensaje = "Tempeeratura OK"
    else:
        validez = False
        mensaje = "ALERTA: Temperatura fuera de rango"
    return validez, mensaje  # Devuelve una tupla

print("\n2. Validación de Temperatura Almacén:")
# b) y c) - Caso OK
valida_1, msg_1 = validar_temperatura_almacen(4.5, 2.0, 8.0)
print(f"    Prueba 1 (4.5°C, Rango [2-8]): ¿Válida? {valida_1}, Mensaje '{msg_1}'")

# d) - Caso Fuera de Rango
valida_2, msg_2 = validar_temperatura_almacen(1.5, 2.0, 8.0)
print(f"    Prueba 2 (1.5°C, Rango [2-8]: ¿Válida? {valida_2}, Mensaje: {repr(msg_2)})")

# 3. Información Fija de un Lote Estándar de Referencia:
#    Los datos de un lote estándar de referencia son:
#    ID_Lote: "REF-API-007-2024"
#    Principio_Activo: "Dexketoprofeno Trometamol"
#    Pureza_Certificada: 99.92 (%)
#    Fecha_Certificacion: "2024-01-15"
#    a) Crea una tupla `estandar_ref_dexketo` que contenga estos cuatro valores.
#    b) Imprime la tupla.
#    c) Usando desempaquetado, asigna cada valor de la tupla a variables separadas
#       (`id_std`, `pa_std`, `pureza_std`, `fecha_cert_std`).
#    d) Imprime cada una de estas variables con una etiqueta descriptiva.

print("\n3. Lote Estándar de Referencia:")

estandar_ref_dexketo = (
    "REF-API-007-2024", 
    "Dexketoprofeno Trometamol",
    99.92,
    "2024-01-15"
)
print(f"    a,b) Datos del Estándar: {estandar_ref_dexketo}")

# c)
id_std, pa_std, pureza_std, fecha_cert_std = estandar_ref_dexketo

# d)
print(f"    d) ID Estándar: {id_std}")
print(f"    Principio Activo: {pa_std}")
print(f"    Pureza Certificada: {pureza_std}%")
print(f"    Fecha de Certificación: {fecha_cert_std}")