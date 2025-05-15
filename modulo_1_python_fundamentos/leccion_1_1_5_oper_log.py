print("\n--- Lección 1.1.5.: Operadores de Comparación y Lógicos ---")

# --- Operadores de comparación ---
temperatura_actual_farmaco = 4.5  # °C
temp_max_permitida = 8.0  # °C
temp_min_permitida = 2.0  # °C

print(f"Temperatura actual: {temperatura_actual_farmaco}°C")
print(f"Límites permitidos: [{temp_min_permitida}°C - {temp_max_permitida}°C]")

es_igual_al_maximo = temperatura_actual_farmaco == temp_max_permitida
print(f"¿Temperatura actual IGUAL a máxima permitida? {es_igual_al_maximo}")

diferente_al_min = temperatura_actual_farmaco != temp_min_permitida
print(f"¿Temperatura actual DIFERENTE de mínima permitida? {diferente_al_min}")

supera_max = temperatura_actual_farmaco > temp_max_permitida
print(f"¿Temperatura actual SUPERA la máxima permitida? {supera_max}")

debajo_min = temperatura_actual_farmaco < temp_min_permitida
print(f"¿Temperatura actual por DEBAJO de la mínima permitida? {debajo_min}")

dentro_igual_max = temperatura_actual_farmaco <= temp_max_permitida
print(f"¿Temperatura actual MENOR O IGUAL que la máxima? {dentro_igual_max}")

dentro_igual_min = temperatura_actual_farmaco >= temp_min_permitida
print(f"¿Temperatura actual MAYOR O IGUAL que la mínima? {dentro_igual_min}")

# Comparación de strings (orden lexicográfico/alfabéitco)

farmaco_A = "Amoxicilina"
farmaco_B = "Aspirina"
print(f"\nComparando '{farmaco_A}' y '{farmaco_B}'")
print(f"¿'{farmaco_A}' == '{farmaco_B}'?: {farmaco_A == farmaco_B}")
print(f"¿'{farmaco_A}' < '{farmaco_B}'?: {farmaco_A < farmaco_B}")

# --- Operadores Lógicos ---
# Ejemplo: Validación de un parámetro de calidad (pH)
ph_muestra_actual = 7.1
ph_especif_min = 6.8
ph_especif_max = 7.2

# Usando 'and' para verificar si está dentro del rango
dentro_rango_ph = (ph_muestra_actual) and (ph_especif_min <= ph_especif_max)
print(f"¿pH dentro del rango (usando 'and')? {dentro_rango_ph}")

# Usando 'or' para verificar si está fuera de rango (alternativa)
verificacion_1 = ph_muestra_actual < ph_especif_min
verificacion_2 = ph_muestra_actual > ph_especif_max
fuera_rango_ph = verificacion_1 or verificacion_2
print(f"¿pH fuera del rango (usando 'or')? {fuera_rango_ph}")

# Usando 'not' para invertir una condición
print(f"¿pH está dentro del rango? {not fuera_rango_ph}")

edad_paciente = 45
condicion_x_presente = False
biomarcador_Y_valor = 60

criterio_edad = edad_paciente >= 18
criterio_condicion_x = condicion_x_presente
criterio_biomarcador_Y = biomarcador_Y_valor > 50

paciente_elegible = criterio_edad and \
                    (criterio_condicion_x or criterio_biomarcador_Y)
print("\nCriterios de Elegibilidad del Paciente")
print(f"Edad: {edad_paciente}")
print(f"Cond_x: {condicion_x_presente}")
print(f"Biom_Y: {biomarcador_Y_valor}")
print(f"    Criterio Edad (>=18): {criterio_edad}")
print(f"    Criterio Condicion X: {criterio_condicion_x}")
print(f"    Criterio Biomarcador Y (>50): {criterio_biomarcador_Y}")
print(f"¿Paciente Elegible para el Ensayo? {paciente_elegible}")

print("\n--- Condiciones Farmacéuticas Complejas---")

# 1. Validación de un Lote de Producción
#   Un Lote se aprueba si:
#   a) La pureza >= 99.0 % Y
#   b) El contenido de humedad es <= 1.5 % Y
#   C) NO hay partículas visibles
#   (representar como 'partículas_visibles = False' como aprobado)

pureza_lote = 99.5
humedad_lote = 1.2
particulas_visibles_lote = False

lote_aprobado_ej1 = (pureza_lote >= 99.0) and \
                    (humedad_lote <= 1.5) and \
                    (not particulas_visibles_lote)
print(f"1. Lote (Pureza: {pureza_lote} %)")
print(f"   Humedad: {humedad_lote} %")
print(f"   Partículas: {particulas_visibles_lote}")
print(f"   ¿Lote Aprobado? {lote_aprobado_ej1}")

# 2. Alerta de Estabilidad de un Fármaco:
#   Generar una alerta si:
#   a) La temperatura de almacenamiento supera los 25 °C
#   o la temperatura es inferior a 2 °C
#   b) La humedad relativa supera el 60 %

temp_almace_actual_ej2 = 28.0
hum_rel_actual_ej2 = 55.0
condicion_temp_ej2 = (temp_almace_actual_ej2 > 25.0) or \
                        (temp_almace_actual_ej2 < 2.0)
condicion_hum_ej2 = hum_rel_actual_ej2 > 60
generar_alerta_estabilidad_ej2 = condicion_temp_ej2 or \
                                    condicion_hum_ej2
print(f"\n2. Almacenamiento Temp: {temp_almace_actual_ej2} °C")
print(f"Humedad: {hum_rel_actual_ej2} %")
print(f" ¿Generar Alerta de Estabilidad? {generar_alerta_estabilidad_ej2}")

# 3. Criterio para Retirar un Medicamento del Mercado
#   Un medicamento se considera para retiro si:
#   a) Se reporta un número de eventos adversos graves (EAG) > 5
# EN CUALQUIER país
#   b) El medicamento falla las pruebas de estabilidad acelerada
# (falla_estabilidad_acelerada = True) Y NO existe una alternativa
# terapéutica disponible (alternativa_disponible = False).

eag_pais_A_ej3 = 3
eag_pais_B_ej3 = 6  # Supera el umbral
falla_estabilidad_acelerada_ej3 = True
alternativa_disponibe_ej3 = True

condicion_eag_ej3 = (eag_pais_A_ej3 > 5) or \
                    (eag_pais_B_ej3 > 5)
condicion_estabilidad_alternativa_ej3 = falla_estabilidad_acelerada_ej3 and \
                (not alternativa_disponibe_ej3)
considerar_retiro_ej3 = condicion_eag_ej3 or \
                        condicion_estabilidad_alternativa_ej3
print(f"\n3. Retiro de Medicamento (EAG_A: {eag_pais_A_ej3})")
print(f"¿Considerar Retiro del Mercado? {considerar_retiro_ej3}")

# 4. Asignación de Paciente a Grupo de Dosis en Ensayo:
#   Un paciente se asigna al grupo de "Dosis Alta" si:
# (Su edad es > 60 Y su función renal (medida como eGFR) es >=
# 60 mL/min/1.73m²)
#    (Su enfermedad es clasificada como "Severa" Y NO tiene
#    comorbilidades cardíacas (comorb_cardiaca = False))
#    Define variables: `edad_pac_ej4`, `egfr_pac_ej4`,
#    `enfermedad_severa_ej4`, `comorb_cardiaca_ej4` con valores de prueba.
#    Calcula: `asignar_dosis_alta_ej4` (booleano)
#    Imprime los valores de entrada y el resultado.

edad_pac_ej4 = 65
egfr_pac_ej4 = 70.0
enfermedad_severa_ej4 = False
comorb_cardiaca_ej4 = False

criterio_edad_renal_ej4 = (edad_pac_ej4 > 60) and (egfr_pac_ej4 >= 60)
criterio_enfermedad_comorb_ej4 = enfermedad_severa_ej4 and \
    (not comorb_cardiaca_ej4)
asignar_dosis_alta_ej4 = criterio_edad_renal_ej4 or \
    criterio_enfermedad_comorb_ej4

print("\n4. Asignación a Dosis Alta")
print(f"Edad: {edad_pac_ej4}")
print(f"eGFR: {egfr_pac_ej4}")
print(f"Severa: {enfermedad_severa_ej4}")
print(f"Cardíaca: {comorb_cardiaca_ej4}")
print(f"¿Asignar a Dosis Alta? {asignar_dosis_alta_ej4}")
