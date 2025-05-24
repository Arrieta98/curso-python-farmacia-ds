# Lección 1.5.3: Sentencia return (Devolver valores)
print("--- Lección 1.5.3: Sentencia retorno ---")

# --- Ejemplo 1: Función que devuelve un valor simple ---
print("\n--- Ejemplo 1: Devolver un Valor Simple ---")
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    if radio < 0:
        print("Error: El radio no puede ser negativo.")
        return None     # Devolver None para indicar un error o valor inválido.
    
    pi = 3.1415926535   # Aproximación
    area = pi * (radio ** 2)
    return area     # Devuelve el valor calculado

# Llamar a la función y usar el valor devuelto
radio1 = 5.0
area1 = calcular_area_circulo(radio1)

if area1 is not None:   # Buena práctica verificar si se devolvió un valor útil
    print(f"El área de un círculo con radio {radio1} es: {area1:.2f}")
    # Podríamos usar area1 para más cálculos, ej. volumen de un ciliendro
else:
    print(f"No se pudo calcular el área para radio {radio1}.")

radio2 = -2.0
area2 = calcular_area_circulo(radio2)   # Esto debería devolver None
if area2 is None:
    print(f"El cálculo del área falló para radio {radio2}, como se esperaba.")

# --- Ejemplo 2: Función que devuelve un Booleano ---
print("\n--- Ejemplo 2: Devolver un Booleano (Validación) ---") 
def es_ph_fisiologico(ph_medido):
    """Verifica si un pH está dentro del rango fisiológico (aprox. 7.35-7.45)."""
    ph_min_fisiologico = 7.35
    ph_max_fisiologico = 7.45
    if ph_min_fisiologico <= ph_medido <= ph_max_fisiologico:
        return True
    else:
        return False
    
# Uso
ph_sangre_paciente = 7.40
if es_ph_fisiologico(ph_sangre_paciente):
    print(f"El pH {ph_sangre_paciente} es considerado fisiológico.")
else:
    print(f"El pH {ph_sangre_paciente} NO es considerado fisiológico.")

ph_orina_paciente = 6.5
if not es_ph_fisiologico(ph_orina_paciente):
    print(f"El pH {ph_orina_paciente} (orina) efectivamente no es fisiológico para sangre.")
    
# --- Ejemplo 3: Función que devuelve Múltiples Valores (como una Tupla) ---
print("\n--- Ejemplo 3: Devolver Múltiples valores ---")
def analizar_resultados_estabilidad(concentracion_inicial, concentracion_final, tiempo_meses):
    """Calcula la degradación y la tasa de degradación (simplificado)."""
    if concentracion_inicial <= 0 or tiempo_meses <= 0:
        print("Error: Concentración inicial y tiempo deben ser positivos.")
        return None, None  # Devolver una tupla de Nones
    
    degradacion_absoluta = concentracion_inicial - concentracion_final
    porcentaje_degradacion = (degradacion_absoluta / concentracion_inicial) * 100
    # Tasa simplificada, asumiendo cinética de orden cero para el ejemplo
    # tasa_degradacion_por_mes = degradacion_absoluta / tiempo_meses 
    # Para cinética de primer orden (más realista, pero más complejo): k = (ln(C0) - ln(Ct)) / t
    # Aquí solo devolvemos el porcentaje para mantenerlo simple por ahora.
    
    return porcentaje_degradacion, degradacion_absoluta     # Python crea una tupla (porc_degrad, abs_degrad)

# Uso y desempaquetado de los múltiples valores devueltos
c_inicial = 100.0  # mg
c_final_6m = 95.5  # mg a los 6 meses
tiempo = 6

# Desempaquetar la tupla devuelta en variables separadas
porc_degrad, abs_degrad = analizar_resultados_estabilidad(c_inicial, c_final_6m, tiempo)

if porc_degrad is not None:  # Verificar si el cálculo fue exitoso
    print(f"Análisis de Estabilidad (C0={c_inicial}mg, C{tiempo}m={c_final_6m}mg, Tiempo={tiempo} meses):")
    print(f"    Porcentaje de Degradación: {porc_degrad:.2f}%")
    print(f"    Degradación Absoluta: {abs_degrad:.2f} mg")
    
# Llamada con error
resultados_error = analizar_resultados_estabilidad(100, 98, 0) # tiempo_meses
if resultados_error == (None, None):    # Comparamos la tupla devuelta
    print("\nEl análisis de estabilidad falló debido a tiempo cero, como se esperaba.")

# --- Práctica Adicional: Funciones Farmacéuticas que Devuelven Valores ---
print("\n--- Práctica Adicional: Funciones que Devuelven Valores ---")

# 1. Modificar `calcular_volumen_final_dilucion` (de la lección anterior)
#    para que DEVUELVA el `v2` calculado (o `None` si hay error), en lugar de imprimirlo.
#    Luego, llama a la función, guarda el resultado en una variable e imprímela.

def calcular_volumen_final_dilucion_return(c1, v1, c2):
    """Calcula y DEVUELVE el volumen final (V2) para una dilución (C1V1 = C2V2)."""
    if not all((isinstance(val, (int, float))) for val in [c1, v1, c2]):
        print("Error: Todas las entradas (c1, v1, c2) deben ser numéricas.")
        return None
    if c2 == 0:
        print("Error: La concentración final (C2) no puede ser cero.")
        return None
    if v1 < 0 or c1 < 0: # Concentraciones y volúmenes no deben ser negativos
        print("Error: Las concentraciones y el volumen inicial no pueden ser negativos.")
        return None
    
    v2 = (c1 * v1) / c2
    return v2

print("\n1. Devolviendo Volumen de Dilución:")
vol_final_calculado = calcular_volumen_final_dilucion_return(10.0, 5.0, 0.5)
if vol_final_calculado is not None:
    print(f"    Volumen final necesario (V2): {vol_final_calculado:.2f} mL")
else:
    print(" Nose pudo calcular el volumen final.")
    
vol_final_error = calcular_volumen_final_dilucion_return(10.0, 5.0, 0)
if vol_final_error is None:
    print(" Cálculo con C2=0 falló y devolvió None, como se esperaba.")
    
# 2. Modificar `generar_id_muestra` (de la lección anterior)
#    para que DEVUELVA el ID de muestra generado como un string, en lugar de imprimirlo.
#    Llama a la función, guarda el ID en una variable e imprímela.

def generar_id_muestra_return(tipo_muestra, anio, secuencial, sitio_estudio="SITIO_CENTRAL"):
    """Genera y DEVUELVE un ID de muestra formateado."""
    if not all(isinstance(val, str) for val in [tipo_muestra, sitio_estudio]):
        return "Error: tipo y sitio deben ser string"  # 0 lanzar excepción
    if not isinstance(anio, int) or not isinstance(secuencial, int):
        return "Error: año y secuencial debe ser int"
    
    secuencial_formateado = f"{secuencial:03d}"
    id_generado = f"{tipo_muestra.upper()}-{anio}-{sitio_estudio.upper()}-{secuencial_formateado}"
    return id_generado

print("\n2. Devolviendo ID de Muestra generado:")
id_muestra_1 = generar_id_muestra_return("API-RAW", 2025, 77)
print(f"    ID generado: {id_muestra_1}")
id_muestra_2 = generar_id_muestra_return("PLASMA", 2024, 8, "LAB_NORTE")
print(f"    ID generado: {id_muestra_2}")

# 3. Función `evaluar_riesgo_estabilidad(degradacion_porc, tiempo_meses)`
#    Define una función que reciba el porcentaje de degradación y el tiempo en meses.
#    Debe devolver una tupla: `(clasificacion_riesgo_str, accion_recomendada_str)`
#    Reglas de decisión (puedes inventar las tuyas o usar estas):
#    - Si degradacion_porc > 10.0 O (degradacion_porc > 5.0 Y tiempo_meses >= 12):
#        clasificacion_riesgo = "Alto"
#        accion_recomendada = "Retirar lote. Investigar causa raíz."
#    - Elif 5.0 < degradacion_porc <= 10.0 O (2.0 < degradacion_porc <= 5.0 Y tiempo_meses >= 12):
#        clasificacion_riesgo = "Medio"
#        accion_recomendada = "Poner en cuarentena. Realizar análisis adicionales."
#    - Elif 0 <= degradacion_porc <= 2.0:
#        clasificacion_riesgo = "Bajo"
#        accion_recomendada = "Lote aceptable. Continuar monitorización."
#    - Else (ej. degradación negativa, o parámetros inválidos):
#        clasificacion_riesgo = "Indeterminado"
#        accion_recomendada = "Datos de entrada inválidos o inconsistentes."
#    Llama a la función con diferentes valores, desempaqueta los resultados e imprímelos.
print("\n3. Evaluación de Riesgo de Estabilidad (Ejercicio para ti):")

def evaluar_riesgo_estabilidad(degradacion_porc, tiempo_meses):
    """Evalúa el riesgo de estabilidad y devuelve clasificación y acción."""
    clasificacion_riesgo = "Indeterminado" # Valor por defecto
    accion_recomedada = "Datos de entrada inválidos o incosistentes." # Valor por defecto
    
    if not(isinstance(degradacion_porc, (int, float)) and isinstance(tiempo_meses, (int, float))):
        return clasificacion_riesgo, accion_recomedada
    if tiempo_meses < 0 or degradacion_porc < 0 :
        return clasificacion_riesgo, accion_recomedada
    
    if degradacion_porc > 10.0 or (degradacion_porc > 5.0 and tiempo_meses >= 12):
        clasificacion_riesgo = "Alto"
    elif 5.0 < degradacion_porc <= 10.0 or (2.0 < degradacion_porc <= 5.0 and tiempo_meses >=12):
        clasificacion_riesgo = "Medio"
    elif 0 <= degradacion_porc <= 2.0:  # Solo si las condiciones anterior no se cumplieron
        # y degradación está en este rango bajo
        clasificacion_riesgo = "Bajo"
        accion_recomedada = "Lote aceptable. Continuar monitorización"
    # Si no cae en ninguna de las anteriores y los datos eran válidos, podría necesitar más lógica.
    # Por ahora, si los datos son válidos pero no encaja, mantendrá "Indeterminado".
    
    return clasificacion_riesgo, accion_recomedada

# Pruebas
casos_estabilidad = [
    {"degradacion": 1.5, "tiempo": 6, "etiqueta": "Bajo Riesgo"},
    {"degradacion": 3.0, "tiempo": 6, "etiqueta": "Bajo Riesgo (pero podría ser Medio si tiempo largo)"}, # Esperado: Bajo
    {"degradacion": 3.0, "tiempo": 12, "etiqueta": "Medio Riesgo"},
    {"degradacion": 6.0, "tiempo": 6, "etiqueta": "Medio Riesgo"},
    {"degradacion": 12.0, "tiempo": 3, "etiqueta": "Alto Riesgo"},
    {"degradacion": 7.0, "tiempo": 12, "etiqueta": "Alto Riesgo"},
    {"degradacion": -1.0, "tiempo": 6, "etiqueta": "Error de Datos"},
    {"degradacion": 5.0, "tiempo": "seis", "etiqueta": "Error de Datos"}
]

for i, caso in enumerate(casos_estabilidad):
    print(f"\nPrueba de Estabilidad Caso {i+1} ({caso['etiqueta']}): Deg={caso['degradacion']}%, Tiempo={caso['tiempo']}m")
    riesgo, accion = evaluar_riesgo_estabilidad(caso["degradacion"], caso["tiempo"])
    print(f" Clasificación de Riesgo: {riesgo}")
    print(f" Acción Recomendada: {accion}")
    
