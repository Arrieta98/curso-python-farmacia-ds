print("--- Lección 1.4.2: Bucles for ---")

# --- Iterar sobre una Lista ---
print("\n--- Iterar sobre una Lista (Principios Activos) ---")
principios_activos_analgesicos = ["Paracetamol", "Ibuprofeno", "Aspirina", "Naproxeno"]
for farmaco in principios_activos_analgesicos:
    # 'faarmaco' tomará el valor de cada elemento de la lista en cada iteración
    print(f"Principio activo actual: {farmaco}")
    print(f"    Longitud del nombre: {len(farmaco)}")
    if farmaco == "Aspirina":
        print("     (Nota: Considerar precauciones gástricas con Aspirina)")
print("Fin de la lista de analgésicos")

# --- Iterar sobre una Tupla ---
print("\n--- Iterar sobre una Tupla (Parámetros de Calibración) ---")
parametros_calibracion_hplc = ("Flujo (mL/min)", 1.0, "Temperatura Columna (°C)", 30, "Longitud Onda (nm)", 254)
# No podemos iterar directamente como clave-valor, pero sí sobre los elementos
print("Elementos de la tupla de calibración")
for elemento in parametros_calibracion_hplc:
    print(f"- {elemento} (Tipo: {type(elemento).__name__})")

# --- Iterar sobre un String ---
print("\n--- Iterar sobre un String (Código de Fórmula) ---")
codigo_formula_magistral = "FM-007B"
print(f"Caracteres en el código '{codigo_formula_magistral}':")
for caracter in codigo_formula_magistral:
    print(f"    '{caracter}'")
    
# --- Iterar usando la función range() ---
print("\n--- Iterar con range () ---")
#range(fin) -> 0 gasta fin-1
print("Procesando 5 muestras (usando(5)):")
for i in range(5):  # i tomará valores 0, 1, 2, 3, 4
    print(f"    Procesando Muestra ID: M-{i+1:03d}")    # i+1 para mostrar 1-5, :03d para formatear a 3 dígitos 

# range(inicio, fin) -> inicio hasta fin-1
print("\nAños de validez de un certificado (2025 a 2028):")
for anio_validez in range(2025, 2029):  # Genera 2025, 2026, 2027, 2028
    print(f"    Certificado válido durante el año: {anio_validez}")
    
# range(inicio, fin, paso)
print("\nPuntos de muestreo en un estudio de estabilidad (cada 3 meses durante 1 año):")
# Mes 0, 3, 6, 9. El 12 no se incluye con range (0,12,3). Si queremos incluir el mes 12,  sería range(0, 13, 3)
for mes_muestreo in range(0, 12, 3):
    print(f" Muestreo programado para el mes: {mes_muestreo}")

# --- Iterar sobre las claves, valores o ítems de un Diccionario ---
print("\n--- Iterar sobre Diccionarios ---")
resultados_control_calidad_loteX = {
    "pH" : 7.05,
    "Pureza (%)" : 99.8,
    "Disolución (%)" : 85.2,
    "Contenido Humedad (%)" : 0.45
}
print(f"Resultado QC Lote X: {resultados_control_calidad_loteX}")

print("\nIterando sobre claves (por defecto o con .keys())")
for parametro in resultados_control_calidad_loteX:  # O resultados_control_calidad_loteX.keys()
    valor_parametro = resultados_control_calidad_loteX[parametro]
    print(f"    Parámetro: {parametro}, Valor: {valor_parametro}")

print(f"\nIterando sobre valores (con. values()):")
for valor in resultados_control_calidad_loteX.values():   
    print(f"    Valor de un parámetro: {valor}")

print("\nIterando sobre ítems (pares clave-valor con .item() - la forma más común):")
for parametro, valor in resultados_control_calidad_loteX.items():
    print(f"    Parámetro: {parametro.ljust(25)} | Valor: {valor}")     # .ljust() para alinear
    
# -- Bucles for anidados (un bucle dentro de otro) ---
print("\n--- Bucles for Anidados (Simulación de Combinaciones de Dosis) ---")
# Supongamos que queremos probar combinaciones de dosis para dos fármacos A y B
dosis_farmaco_A_mg = [10, 20, 30]
dosis_farmaco_B_mg = [50, 100]

print("Combinaciones de dosis a probar (Fármaco A + Fármaco B):")
for dosis_A in dosis_farmaco_A_mg:
    for dosis_B in dosis_farmaco_B_mg:  #Este bucle interno se ejecuta completamente por cada iteración externo
        print(f"    Probar: {dosis_A} mg de Fármaco A + {dosis_B} mg de Fármaco B")

print("\n--- Procesamiento con Bucles for ---")

# 1. Lista de Temperaturas Registradas:
#    `temperaturas_horarias_estufa_C = [37.0, 37.1, 36.9, 37.2, 38.0, 37.1, 36.8]`
#    a) Itera sobre la lista e imprime cada temperatura.
#    b) Dentro del bucle, si una temperatura es > 37.5 °C, imprime un mensaje de "ALERTA: Temperatura alta!".
#    c) Calcula la temperatura promedio iterando sobre la lista y sumando los valores.

temperaturas_horarias_estufa_C = [37.0, 37.1, 36.9, 37.2, 38.0, 37.1, 36.8]
print(f"\n1. Temperatura Horarias Estufa (°C): {temperaturas_horarias_estufa_C}")
suma_temperaturas_1c = 0.0
print("     a,b) Registros y Alertas:")
for temp in temperaturas_horarias_estufa_C:
    print(f"    Temperatura registrada: {temp}°C")
    if temp > 37.5:
        print("     ALERTA: Temperatura alta!")
    suma_temperaturas_1c += temp
    
if temperaturas_horarias_estufa_C:  # Evitar división por cero si la lista está vacía
    promedio_temperaturas_1c = suma_temperaturas_1c / len(temperaturas_horarias_estufa_C)
    print(f"    c) Temperatura promedio: {promedio_temperaturas_1c:.2f}°C")
else:
    print("     c) No hay temperaturas para calcular el promedio.")

# 2. Generar Códigos de Muestras Secuenciales:
#    Quieres generar códigos para 8 muestras que sigan el formato "MUESTRA-LAB-2025-XXX",
#    donde XXX es un número secuencial de 001 a 008.
#    Usa un bucle `for` con `range()` e f-strings para imprimir estos códigos.

print("\n2. Genereación de Códigos de Muestras:")
for i in range (1, 9):  # i irá de 1 a 8
    codigo_muestra_2 = f"MUESTRA-LAB-2025-{i:03d}"
    print(f"    {codigo_muestra_2}")
    
# 3. Reporte de Control de Calidad de Excipientes:
#    Tienes un diccionario con excipientes y su estado de aprobación (True si aprobado, False si no).
#    `estado_excipientes_loteY = {"Lactosa": True, "Almidón": True, "Estearato Mg": False, "Talco": True}`
#    a) Itera sobre los ítems del diccionario.
#    b) Para cada excipiente, imprime su nombre y si está "APROBADO" o "RECHAZADO".
#    c) Cuenta cuántos excipientes están aprobados.
print("\n3. Reporte de Estado de Excipientes (Ejercicios para ti):")
estado_excipientes_loteY = {"Lactosa": True, "Almidón": True, "Estearato Mg": False, "Talco": True}
print(f"    Estado de Excipientes Lote Y: {estado_excipientes_loteY}")
excipientes_aprobados_count_3c = 0
print("     a,b) Estado Detallado:")
for excipiente, aprobado in estado_excipientes_loteY.items():
    estado_str = "APROBADO" if aprobado else "RECHAZADO"
    print(f"    Excipientes: {excipiente.ljust(15)} | Estado: {estado_str}")
    if aprobado:
        excipientes_aprobados_count_3c += 1
print(f"    c) Número de excipientes aprobados: {excipientes_aprobados_count_3c}")