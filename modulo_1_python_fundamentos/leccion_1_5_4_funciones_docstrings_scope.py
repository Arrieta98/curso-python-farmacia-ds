# Lección 1.5.4: Docstrings y Ámbito de Variables
print("--- Lección 1.5.4: Docstrings y Ámbito de Variables ---")

# --- Docstrings ---
print("\n--- Ejemplo: Docstrings ---")

def calcular_concentracion_porcentual(gramos_soluto, ml_solucion, tipo_porcentaje="p/v"):
    """
    Calcula la concentración porcentual de una solución.

    Args:
        gramos_soluto (float): La masa del soluto en gramos.
        ml_solucion (float): El volumen total de la solución en mililitros
                             o la masa total de la solución en gramos si tipo_porcentaje es "p/p".
        tipo_porcentaje (str, optional): El tipo de porcentaje a calcular.
                                         Puede ser "p/v" (peso/volumen) o "p/p" (peso/peso).
                                         Por defecto es "p/v".

    Returns:
        float: La concentración porcentual calculada.
        None: Si las entradas son inválidas (ej. ml_solucion es 0, tipo_porcentaje no reconocido).
    
    Raises:
        TypeError: Si gramos_soluto o ml_solucion no son numéricos.
    """
    if not isinstance(gramos_soluto, (int, float)) or not isinstance(ml_solucion, (int, float)):
        raise TypeError("Tanto gramos_soluto como ml_solucion deben ser numéricos.")
    
    if ml_solucion == 0:
        print("Error: El volumen/masa de la solución no puede ser cero.")
        return None

    if tipo_porcentaje.lower() == "p/v" or tipo_porcentaje.lower() == "p/p":
        concentracion = (gramos_soluto / ml_solucion) * 100
        return concentracion
    else:
        print(f"Error: Tipo de porcentaje '{tipo_porcentaje}' no reconocido. Use 'p/v' o 'p/p'.")
        return None

# Usar la función y ver su docstring
help(calcular_concentracion_porcentual) # Muestra el docstring

print("\nLlamando a la función con docstring:")
conc_pv = calcular_concentracion_porcentual(10, 200) # Usa p/v por defecto
if conc_pv is not None:
    print(f"Concentración % p/v: {conc_pv:.2f}%")

conc_pp = calcular_concentracion_porcentual(5, 50, tipo_porcentaje="p/p")
if conc_pp is not None:
    print(f"Concentración % p/p: {conc_pp:.2f}%")

try:
    calcular_concentracion_porcentual("diez", 200)
except TypeError as e:
    print(f"Error de tipo capturado: {e}")


# --- Ámbito de Variables (Scope) ---
print("\n--- Ejemplo: Ámbito de Variables ---")

variable_global_modulo = "Soy una constante a nivel de módulo (ej. PI_VALOR = 3.14)"

def funcion_scope_ejemplo(parametro_local_func):
    variable_local_interna = "Soy local dentro de funcion_scope_ejemplo"
    print(f"  Dentro de la función:")
    print(f"    Puedo ver el parámetro local: '{parametro_local_func}'")
    print(f"    Puedo ver mi variable local interna: '{variable_local_interna}'")
    print(f"    Puedo leer la variable global del módulo: '{variable_global_modulo}'")
    
    # Intentar modificar la global SIN la palabra clave 'global' crea una local
    # variable_global_modulo = "Intenté modificarla localmente" # Esto crea una nueva variable_global_modulo local
    # print(f"    Variable 'variable_global_modulo' dentro de la func (sombreada): {variable_global_modulo}")

print(f"\nFuera de la función, antes de llamarla:")
print(f"  Variable global del módulo: '{variable_global_modulo}'")
# print(f"  Intentando acceder a parametro_local_func: {parametro_local_func}") # NameError
# print(f"  Intentando acceder a variable_local_interna: {variable_local_interna}") # NameError

print("\nLlamando a funcion_scope_ejemplo('argumento para parámetro'):")
funcion_scope_ejemplo("argumento para parámetro")

print(f"\nFuera de la función, después de llamarla:")
print(f"  Variable global del módulo (no debería haber cambiado si no se usó 'global'): '{variable_global_modulo}'")


# Ejemplo de modificación de global con la palabra clave 'global'
contador_procesos_global = 0 # Variable global

def simular_proceso_farmaceutico(nombre_proceso):
    global contador_procesos_global # Indicar que usaremos la variable global
    
    print(f"  Iniciando proceso: {nombre_proceso}")
    # ... lógica del proceso ...
    contador_procesos_global += 1 # Modificamos la variable global
    print(f"  Proceso {nombre_proceso} completado. (Total procesos hasta ahora: {contador_procesos_global})")

print("\nSimulando procesos y modificando contador global:")
simular_proceso_farmaceutico("Mezclado API con Excipientes")
simular_proceso_farmaceutico("Granulación")
simular_proceso_farmaceutico("Compresión Tabletas")
print(f"Valor final del contador_procesos_global fuera de la función: {contador_procesos_global}")


# --- Práctica Adicional: Docstrings y Scope ---
print("\n--- Práctica Adicional: Docstrings y Scope ---")

# 1. Documentar una Función Existente:
#    Toma una de las funciones que creaste en la Lección 1.5.3 (ej. `evaluar_riesgo_estabilidad`)
#    y añádele un docstring completo que describa:
#    - Su propósito (resumen en una línea).
#    - Sus parámetros (nombre, tipo esperado, descripción).
#    - Lo que devuelve (tipo y descripción).
#    Luego, usa `help()` para mostrar el docstring de tu función.
# TU CÓDIGO EJERCICIO 1 AQUÍ
def evaluar_riesgo_estabilidad_doc(degradacion_porc, tiempo_meses):
    """
    Evalúa el riesgo de estabilidad de un producto farmacéutico.

    Basándose en el porcentaje de degradación y el tiempo en estudio,
    clasifica el riesgo y sugiere una acción.

    Args:
        degradacion_porc (float or int): El porcentaje de degradación observado.
        tiempo_meses (float or int): El tiempo en meses que duró el estudio de estabilidad.

    Returns:
        tuple: Una tupla conteniendo dos strings: (clasificacion_riesgo, accion_recomendada).
               Retorna ("Indeterminado", "Datos de entrada inválidos o inconsistentes.") si
               las entradas no son numéricas o son negativas.
    """
    clasificacion_riesgo = "Indeterminado"
    accion_recomendada = "Datos de entrada inválidos o inconsistentes."

    if not (isinstance(degradacion_porc, (int, float)) and isinstance(tiempo_meses, (int, float))):
        return clasificacion_riesgo, accion_recomendada
    if tiempo_meses < 0 or degradacion_porc < 0 :
        return clasificacion_riesgo, accion_recomendada

    if degradacion_porc > 10.0 or (degradacion_porc > 5.0 and tiempo_meses >= 12):
        clasificacion_riesgo = "Alto"
        accion_recomendada = "Retirar lote. Investigar causa raíz."
    elif 5.0 < degradacion_porc <= 10.0 or (2.0 < degradacion_porc <= 5.0 and tiempo_meses >= 12):
        clasificacion_riesgo = "Medio"
        accion_recomendada = "Poner en cuarentena. Realizar análisis adicionales."
    elif 0 <= degradacion_porc <= 2.0 :
        clasificacion_riesgo = "Bajo"
        accion_recomendada = "Lote aceptable. Continuar monitorización."
    
    return clasificacion_riesgo, accion_recomendada

print("\n1. Docstring de 'evaluar_riesgo_estabilidad_doc':")
help(evaluar_riesgo_estabilidad_doc)
riesgo_test, accion_test = evaluar_riesgo_estabilidad_doc(3.5, 12)
print(f"   Prueba de función documentada: Riesgo='{riesgo_test}', Acción='{accion_test}'")


# 2. Juego de Scope:
#    `umbral_aprobacion_global = 98.0` (definida globalmente)
#    Define una función `verificar_pureza_lote(id_lote, pureza_medida)`:
#    - Dentro de esta función, define una variable local `mensaje_resultado = ""`.
#    - La función debe LEER `umbral_aprobacion_global`.
#    - Si `pureza_medida` >= `umbral_aprobacion_global`, asigna a `mensaje_resultado`
#      "Lote [id_lote] APROBADO (Pureza: [pureza_medida]%)".
#    - Si no, asigna "Lote [id_lote] RECHAZADO (Pureza: [pureza_medida]%) - Umbral: [umbral_aprobacion_global]%".
#    - La función debe DEVOLVER `mensaje_resultado`.
#    Llama a la función con algunos datos de prueba e imprime el mensaje devuelto.
#    Después de la llamada, imprime el valor de `umbral_aprobacion_global` para verificar que no cambió.
#    Intenta imprimir `mensaje_resultado` fuera de la función (debería dar NameError).
# TU CÓDIGO EJERCICIO 2 AQUÍ
umbral_aprobacion_global = 98.0
print(f"\n2. Juego de Scope:")
print(f"   Umbral de aprobación global (antes de función): {umbral_aprobacion_global}%")

def verificar_pureza_lote(id_lote, pureza_medida):
    """Verifica la pureza de un lote contra un umbral global y devuelve un mensaje."""
    mensaje_resultado = "" # Variable local
    # Leemos umbral_aprobacion_global (no la modificamos)
    if pureza_medida >= umbral_aprobacion_global:
        mensaje_resultado = f"Lote {id_lote} APROBADO (Pureza: {pureza_medida}%)"
    else:
        mensaje_resultado = (f"Lote {id_lote} RECHAZADO (Pureza: {pureza_medida}%) - "
                             f"Umbral: {umbral_aprobacion_global}%")
    return mensaje_resultado

resultado_lote1 = verificar_pureza_lote("LOTE-001A", 99.2)
print(f"   {resultado_lote1}")
resultado_lote2 = verificar_pureza_lote("LOTE-002B", 97.5)
print(f"   {resultado_lote2}")

print(f"   Umbral de aprobación global (después de función): {umbral_aprobacion_global}% (no debió cambiar)")

try:
    # print(mensaje_resultado) # Descomentar para ver el NameError
    print("   Intentar acceder a 'mensaje_resultado' fuera de la función (comentado para evitar NameError).")
except NameError as e:
    print(f"   Error esperado al acceder a variable local fuera de su scope: {e}")


# 3. Contador Global de Muestras Procesadas:
#    Define una variable global `total_muestras_analizadas = 0`.
#    Crea una función `analizar_muestra_bio(id_muestra, tipo_analisis)`:
#    - Esta función debe usar la palabra clave `global` para poder modificar `total_muestras_analizadas`.
#    - Debe imprimir "Analizando [id_muestra] para [tipo_analisis]..."
#    - Debe incrementar `total_muestras_analizadas` en 1.
#    - Debe devolver un string "Análisis de [id_muestra] completado."
#    Llama a la función 3 veces con diferentes datos de muestra.
#    Después de todas las llamadas, imprime el valor final de `total_muestras_analizadas`.
print("\n3. Contador Global de Muestras Procesadas (Ejercicio para ti):")
total_muestras_analizadas = 0

def analizar_muestra_bio(id_muestra, tipo_analisis):
    """Simula el análisis de una muestra e incrementa un contador global."""
    global total_muestras_analizadas # Declarar que queremos modificar la global
    
    print(f"   Analizando {id_muestra} para {tipo_analisis}...")
    # Simular algún trabajo
    total_muestras_analizadas += 1
    return f"Análisis de {id_muestra} completado."

print(f"   Contador inicial de muestras analizadas: {total_muestras_analizadas}")
resultado_analisis1 = analizar_muestra_bio("S-001-PLASMA", "Glucosa")
print(f"   {resultado_analisis1}")
resultado_analisis2 = analizar_muestra_bio("S-002-SUERO", "Electrolitos")
print(f"   {resultado_analisis2}")
resultado_analisis3 = analizar_muestra_bio("T-001-API", "Pureza HPLC")
print(f"   {resultado_analisis3}")

print(f"   Valor final del contador global 'total_muestras_analizadas': {total_muestras_analizadas}")