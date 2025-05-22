print("--- Lección 1.4.1: Condicionales ---")

# --- Sentencia if simple ---
print("\n--- Ejemplo: if simple (control de Calidad de pH) ---")
ph_muestra = 6.5
ph_limite_inferior = 6.8
alerta_ph_bajo = False  # Bandera para la alerta

if ph_muestra < ph_limite_inferior:
    print(f"ALERTA: pH de la mmuestra ({ph_muestra} es MENOR que el límite inferior ({ph_limite_inferior}).)")
    alerta_ph_bajo = True
    # Aquí podrían ir más acciones, como registrar el evento.
    
print(f"Estado de la alerta de pH bajo: {alerta_ph_bajo}")

# --- Sentencia if-else ---
print("\n--- Ejemplo: if-else (Aprobación de Lote por Pureza) ---")
pureza_api_porc = 99.2
pureza_minima_aprobacion_porc = 98.5
estado_lote = ""  # Variable para almacenar el estado

if pureza_api_porc >= pureza_minima_aprobacion_porc:
    print(f"Pureza ({pureza_api_porc}%) CUMPLE con em mínimo requerido ({pureza_minima_aprobacion_porc}%).")
    estado_lote = "APROBADO"
else:
    print(f"Pureza ({pureza_api_proc}%) NO CUMPLE con el mínimo requerido ({pureza_minima_aprobacion_porc}%).")
    estado_lote = "RECHAZADO - Requiere Investigación"

print(f"Estado final del lote: {estado_lote}")

# --- Sentencia if-elif-else ---
print("\n--- Ejemplo: if-elif-else (Clasificación de Estabilidad de un Fármaco) ---")
# Basado en el porcentaje de degradación después de X tiempo
porcentaje_degradacion = 2.3  # %
clasificacion_estabilidad = ""

if porcentaje_degradacion < 1.0:
    clasificacion_estabilidad = "Muy Estable"
elif porcentaje_degradacion < 2.5:  # Se evalúa su la condición anterior fue False
    clasificacion_estabilidad = "Estable"
elif porcentaje_degradacion < 5.0:
    clasificacion_estabilidad = "Moderadamente Estable"
else:  # Si ninguna de las anteriores fue True
    clasificacion_estabilidad = "Poco Estable o Inestable - Revisar"

print(f"Porcentaje de degradación: {porcentaje_degradacion}%")
print(f"Clasificación de estabilidad: {clasificacion_estabilidad}")

# --- Condiciones con Operadores Lógicos ---
print("\n--- Ejemplo: Condiciones con Operadores Lógicos (Alerta de Almacenamiento) ---")

temperatura_actual_almace_C = 27.0
humedad_actual_almacen_proc = 75.0

# --- Condiciones con Operadores Lógicos ---
print("\n--- Ejemplo: Condiciones con Operadores Lógicos (Alerta de Almacenamiento) ---")
temperatura_actual_almacen_C = 27.0
humedad_actual_almacen_proc = 75.0

temp_max_ok_C = 25.0
temp_min_ok_C = 15.0
humedad_max_ok_porc = 60.0

alerta_generada = False

# Condición 1: Temperatura fuera de rango
temp_fuera_rango = (temperatura_actual_almacen_C > temp_max_ok_C) or \
    (temperatura_actual_almacen_C < temp_min_ok_C)

# Condición 2: Humedad demasiado alta.
humedad_demasiado_alta = humedad_actual_almacen_proc > humedad_max_ok_porc

if temp_fuera_rango and humedad_demasiado_alta:
    print("ALERTA CRÍTICA: ¡Temperatura Y Humedad fuera de los límites aceptables!")
    alerta_generada = True
elif temp_fuera_rango:
    print(f"ALERTA: Temperatura ({temperatura_actual_almacen_C})°C fuera del rango [{temp_min_ok_C}-{temp_max_ok_C}]°C.")
    alerta_generada = True
elif humedad_demasiado_alta:
    print(f"ALERTA: Humedad ({humedad_actual_almacen_proc}% supera el máximo aceptable ({humedad_max_ok_porc}%).)")
    alerta_generada = True
else:
    print("Condiones de almacenamiento DENTRO de los límites aceptables.")

print(f"Estado final de alerta generada: {alerta_generada}")

print("\n--- Decisiones en Procesos Farmacéuticos ---")

# 1. Decisión de Producción Basada en Disponibilidad de API:
#    `cantidad_api_disponible_kg = 50.5`
#    `cantidad_api_necesaria_lote_kg = 25.0`
#    `pureza_api_aceptable = True` (booleano que indica si la pureza del API disponible es buena)
#    Se puede producir un lote si la cantidad disponible es >= a la necesaria Y la pureza es aceptable.
#    Imprime "Proceder con la producción del lote." o "No se puede producir el lote. Revisar API."

cantidad_api_disponible_kg = 50.5
cantidad_api_necesaria_lote_kg = 25.0
pureza_api_aceptable = True

print(f"\n1. Decisión de Producción")
print(f"    API Disponible: {cantidad_api_disponible_kg} Kg, Necesario: {cantidad_api_necesaria_lote_kg} Kg, PUREZA OK: {pureza_api_aceptable}")
if cantidad_api_disponible_kg >= cantidad_api_disponible_kg and pureza_api_aceptable:
    print("     Resultado: Proceder con la producción del lote.")
else:
    print("     Resultado: No se puede producir el lote. Revisar API.")
    if not (cantidad_api_disponible_kg >= cantidad_api_necesaria_lote_kg):
        print("     Motivo: Cantidad de API insuficiente.")
    if not pureza_api_aceptable:
        print("     Motivo: Pureza de API no aceptable")
        
# 2. Clasificación de Riesgo de un Evento Adverso (EA):
#    `tipo_ea = "Gastrointestinal"` (string)
#    `severidad_ea = "Leve"` (string: "Leve", "Moderado", "Grave")
#    `esperado = False` (booleano: True si el EA es conocido/esperado, False si es inesperado)
#    Clasifica el riesgo:
#    - "RIESGO ALTO": Si severidad es "Grave" O si es inesperado y severidad es "Moderado".
#    - "RIESGO MEDIO": Si severidad es "Moderado" y es esperado, O si severidad es "Leve" y es inesperado.
#    - "RIESGO BAJO": Si severidad es "Leve" y es esperado.
#    - "DATOS INCOMPLETOS": Para cualquier otra combinación (aunque podrías ser más específico).
#    Imprime la clasificación de riesgo.

tipo_ea = "Respiratorio"
severidad_ea = "Moderado"
esperado = False
clasificacion_riesgo_ea = ""

print(f"\n2. Clasificación de Riesgo EA:")
print(f"    Tipo EA: {tipo_ea}, Severidad: {severidad_ea}, Esperado: {esperado}")

if severidad_ea == "GRAVE" or (not esperado and severidad_ea == "Moderado"):
    clasificacion_riesgo_ea = "RIESGO ALTO"
elif (severidad_ea == "Moderado" and esperado) or (severidad_ea == "Leve" and not esperado):
    clasificacion_riesgo_ea = "RIESGO MEDIO"
elif severidad_ea == "Leve" and esperado:
    clasificacion_riesgo_ea = "RIESGO BAJO"
else:
    clasificacion_riesgo_ea = "DATOS INCOMPLETOS o clasificación no definida"

print(f"    Clasificación de Riesgo del EA: {clasificacion_riesgo_ea}")

# 3. (EjercicAjuste de Dosis Pediátrica Simplificado:
#    `edad_paciente_meses = 15`
#    `peso_paciente_kg = 10.5`
#    `dosis_base_mg = 50` (dosis para >24 meses o >12kg)
#    Reglas de ajuste:
#    - Si edad es <= 6 meses, dosis es 25% de la dosis base.
#    - Si edad es > 6 meses Y edad <= 24 meses, dosis es 50% de la dosis base.
#    - PERO, si el peso es <= 5 kg, la dosis NUNCA debe exceder el 30% de la dosis base,
#      independientemente de la edad (esta regla tiene prioridad si el peso es bajo).
#    - Si ninguna de las condiciones anteriores se cumple (ej. edad > 24 meses Y peso > 5kg),
#      se usa la dosis base completa.
#    Calcula `dosis_final_mg_ej3` e imprímela.
#    (Este es un buen ejercicio para practicar `if-elif-else` anidados o con condiciones complejas).
print(f"\n3. Ajuste de Dosis Pediátrica:")
edad_paciente_meses_ej3 = 15
peso_paciente_kg_ej3 = 4.8
dosis_base_mg_ej3 = 50
dosis_final_mg_ej3 = 0.0

print(f"    Edad: {edad_paciente_meses_ej3} meses, Peso: {peso_paciente_kg_ej3} Kg, Dosis Base: {dosis_base_mg_ej3} mg")

if peso_paciente_kg_ej3 <= 5.0:
    dosis_final_mg_ej3 = dosis_base_mg_ej3 * 0.30
    print("     Aplicada regla prioritaria de peso bajo (<= 5Kg).")
elif edad_paciente_meses_ej3 <= 6:
    dosis_final_mg_ej3 = dosis_final_mg_ej3 * 0.25
elif edad_paciente_meses_ej3 >= 24:  # Implícitamente edad > 6 meses debido al orden
    dosis_final_mg_ej3 = dosis_base_mg_ej3 * 0.50
else:  # Edad > 24 meses y peso > 5Kg (por la primera condición)
    dosis_final_mg_ej3 = dosis_base_mg_ej3
    
print(f"    Dosis Final Calculada: {dosis_base_mg_ej3:.2f} mg")