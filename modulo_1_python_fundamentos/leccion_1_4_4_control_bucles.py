print("--- Lección 1.4.4: Control Avanzado de Bucles ---")

# --- Sentencia break ---
print("\n--- Ejemplo: Sentenci break (Búsqueda de Fármaco Crítico) ---")
lista_farmacos_inventario = ["Amoxicilina", "Ibuprofeno", "Paracetamol", "Fentanilo Citrato", "Omeprazol"]
farmaco_critico_buscado = "Fentanilo Citrato"
encontrado_critico = False

print(f"Buscando {repr(farmaco_critico_buscado)} en el inventario: {lista_farmacos_inventario}")
for farmaco in lista_farmacos_inventario:
    print(f"    Revisando: {farmaco}")
    if farmaco == farmaco_critico_buscado:
        print(f"    ¡ENCONTRADO! {repr(farmaco_critico_buscado)} está en el inventario. Deteniendo Búsqueda.")
        encontrado_critico = True
        break   # Termina el bucle 'for' inmediatamente
    #Este prin no se ejecutará para "Fentanilo Citrato" ni para los que vienen después
    print(f"    {repr(farmaco)} no es el crítico, continuando...")
print(f"¿Se encontró el fármaco crítico? {encontrado_critico}")

print("\n--- Ejemplo: break en un bucle while (Límite de Dosis Acumulada) ---")
dosis_individual_mg = 20
dosis_acumulada_mg = 0
dosis_maxima_permitida_mg = 100
tomas_realizadas = 0

while dosis_acumulada_mg < dosis_maxima_permitida_mg:
    dosis_acumulada_mg += dosis_individual_mg
    tomas_realizadas += 1
    print(f"    Toma {tomas_realizadas}: Dosis acumulada = {dosis_acumulada_mg} mg.")
    if dosis_acumulada_mg >= dosis_maxima_permitida_mg:
        print(f"    Se alcanzó o superó la dosis máxima permitida ({dosis_maxima_permitida_mg})")
        break   # Salir del bucle
print(f"Proceso de dosificación terminado. dosis total administrada: {dosis_acumulada_mg} mg en {tomas_realizadas} tomas.")

# --- Sentencia contine ---
print("\n--- Ejemplo: Sentencia contine (Procesar Solo Lotes Válidos) ---")
lista_codigos_lote = ["L001-OK", "L002-ERR", "L003-OK", "L004-PEND", "L005-OK"]
lotes_procesados_ok = []
print(f"Lotes a procesar: {lista_codigos_lote}")

for codigo_lote in lista_codigos_lote:
    print(f"\n Evaluando lote: {codigo_lote}")
    if "-ERR" in codigo_lote:
        print("     Lote con ERROR. Saltando al siguiente lote.")
        continue    # Omite el resto de esta ireración y va al siguiente lote
    
    if "-PEND" in codigo_lote:
        print("     Lote PENDIENTE de análisis. Saltando al siguiente lote.")
        continue    # Omite el resto y va al siguiente
    
    # Si llegamos aquí, el lote es "-OK" (o no tiene un estado que nos haga saltar)
    print(f"    Procesando lote válido: {codigo_lote}...")
    lotes_procesados_ok.append(codigo_lote)
    # ... (aquí iría la lógica de procesamiento real) ...
print(f"\nLotes procesados exitosamente: {lotes_procesados_ok}")

# --- Cláusula else en Bucles ---
print(f"\n--- Ejemplo: Cláusula else en Bucles ---")
# Caso 1: Bucle for que SÍ encuentra el elemento (y usa break)
print("Buscando 'Paracetamol' en analgésicos (debería encontrarlo y usar break):")
analgesicos = ["Ibuprofeno", "Paracetamol", "Naproxeno"]
for farmaco in analgesicos:
    print(f"    Verificando: {farmaco}")
    if farmaco == "Paracetamol":
        print(" ¡Paracetamol encontrado!")
        break
else:
    # Este bloque NO se ejecutará porque el bucle terminó con 'break'
    print(" Else del for: Paracetamol NO encontrado (esto no debería imprimirse).")
    
# Caso 2: Bucle for que NO encuentra el elemento (termina normalmente)
print("\nBuscando 'Ketorolaco' en analgésicos (no debería encontrarlo):")
for farmaco in analgesicos:     # analgesicos es ahora ['Ibuprofeno', 'Paracetamol', 'Naproxeno']
    print(f"  Verificando: {farmaco}")
    if farmaco == "Ketorolaco":
        print(" ¡Ketorolaco enconetrado! (esto no debería imprimirse)")
        break
    else:
        # Este bloque SÍ se ejecutará porque el bucle terminó normalmente (sin 'break')
        print(" Else del for: Ketorolaco NO encoentrado en la lista de analgésico.")
        
# Caso 3: Bicle while que termina por su condición (no por break)
print("\nSimulado proceso hasta que el contador llegue a 3 (termina por condición):")
contador_while = 0
while contador_while < 3:
    print(f"    Contador  while: {contador_while}")
    contador_while += 1
else:
    # Este bloue SÍ se ejecutará
    print(f"    Else del while: El bucle while terminó normalmente (contador es {contador_while}).")
    
# Caso 4: Bucle while que termina por break
print("\n Simulado proceso con un break (termina por break):")
contador_while_break = 0
while contador_while_break < 5:
    print(f"    Contador while con break: {contador_while_break}")
    if contador_while_break == 2:
        print(" Condición de break alcanzada.")
        break
    contador_while_break += 1
else:
    # Este bloque NO se ejecutará
    print(f"    Else del while con break: (esto de debería imprimirse).")
    
# --- Control Fino en Procesos Farmacéuticos ---
print("\n--- Control Fino en Procesos Farmacéuticos ---")

# 1. Validación de Materias Primas:
#    Tienes una lista de IDs de materias primas:
#    `materias_primas_ids = ["MP-001", "MP-002-CUARENTENA", "MP-003", "MP-004-RECHAZADA", "MP-005"]`
#    Itera sobre la lista. Si una materia prima contiene "CUARENTENA", imprime un mensaje
#    "MP [ID] en cuarentena, no procesar aún." y salta a la siguiente (`continue`).
#    Si contiene "RECHAZADA", imprime "ALERTA CRÍTICA: MP [ID] está rechazada. Detener proceso de validación."
#    y termina el bucle (`break`).
#    Para las demás, imprime "MP [ID] lista para análisis de calidad."
#    Al final, si el bucle completó todas las iteraciones sin un `break` (es decir, no se encontró ninguna rechazada),
#    imprime "Todas las materias primas restantes validadas o en espera de cuarentena."

print("\n1. Validación de Materias Primas:")
materias_primas_ids = ["MP-001", "MP-002-CUARENTENA", "MP-003", "MP-004-RECHAZADA", "MP-005"]
print(f"    Materias primas a validar: {materias_primas_ids}")
for mp_id in materias_primas_ids:
    print(f"    Validando: {mp_id}")
    if "CUARENTENA" in mp_id:
        print(f"    MP {mp_id} en cuarentena, no procesar aún.")
        continue
    if "RECHAZADA" in mp_id:
        print(f"    ALERTA CRÍTICA: MP {mp_id} está rechazada. Detener proceso de validación.")
        break
    print(f"    MP {mp_id} lista para análisis de calidad.")
else:
    print(" Todos las materias primas restantes validadas o en espera de cuarentena.")

# 2. Simulación de un Proceso de Fermentación con Límite de Tiempo:
#    `biomasa_actual_gL = 5.0`
#    `biomasa_objetivo_gL = 50.0`
#    `tasa_crecimiento_por_hora = 1.2` (factor multiplicativo)
#    `horas_proceso = 0`
#    `max_horas_proceso = 10`
#    Usa un bucle `while` para simular el crecimiento de la biomasa.
#    En cada hora, la biomasa se multiplica por `tasa_crecimiento_por_hora`.
#    El bucle debe detenerse si la `biomasa_actual_gL` alcanza o supera el `biomasa_objetivo_gL`,
#    O si `horas_proceso` alcanza `max_horas_proceso`.
#    Imprime la biomasa y las horas en cada paso.
#    Al final, indica si se alcanzó el objetivo o si se detuvo por tiempo.

print("\n2. Simulación de Fermenetación:")
biomasa_actual_gL_ej2 = 5.0
biomasa_objetivo_gl_ej2 = 50.0
tasa_crecimiento_por_ahora_ej2 = 1.2
horas_proceso_ej2 = 0
max_horas_proceso_ej2 = 10

print(f"    Inicio: Biomasa={biomasa_actual_gL_ej2:.2f} g/L, Horas={horas_proceso_ej2}")
while biomasa_actual_gL_ej2 < biomasa_objetivo_gl_ej2:
    if horas_proceso_ej2 >= max_horas_proceso_ej2:
        print(f"    Límite de tiempo ({max_horas_proceso_ej2}) horas alzanzando.")
    
    biomasa_actual_gL_ej2 *= tasa_crecimiento_por_ahora_ej2
    horas_proceso_ej2 += 1
    print(f"    Hora {horas_proceso_ej2}: Biomasa = {biomasa_actual_gL_ej2:.2f} g/L")
else:   # Se ejecuta si el while termina por su condición (biomasa >= objetivo)
    print(f"    Objetivo de biomasa ({biomasa_objetivo_gl_ej2:.2f} g/L) alcanzado o superado.")
    
# Mensaje final basado en cómo terminó el bucle
if biomasa_actual_gL_ej2 >= biomasa_objetivo_gl_ej2:
    print(f"Resultado: Objetivo alcanzado en {horas_proceso_ej2} horas con {biomasa_objetivo_gl_ej2:.2f} g/L.")
elif horas_proceso_ej2 >= max_horas_proceso_ej2:
    print(f"Resultado: Proceso detenido por tiempo a las {horas_proceso_ej2} horas. Biomasa final: {biomasa_actual_gL_ej2:.2f} g/L.")

# 3. Búsqueda de Primer Lote Conforme en una Secuencia de Producción:
#    `resultados_pureza_lotes = [97.5, 98.1, 97.9, 98.7, 99.2, 98.5]`
#    `pureza_minima_conforme = 98.5`
#    Itera sobre `resultados_pureza_lotes`. Imprime la pureza de cada lote que revisas.
#    Cuando encuentres el PRIMER lote que sea >= `pureza_minima_conforme`,
#    imprime "Primer lote conforme encontrado: [pureza] en la posición/índice [índice]." y detén la búsqueda.
#    Si recorres toda la lista y ningún lote cumple, imprime "Ningún lote conforme encontrado en esta secuencia."
#    (Usa `for`, `if`, `break`, y la cláusula `else` del bucle `for`).
#    (Pista: para obtener el índice junto con el valor en un bucle `for`, puedes usar `enumerate()`.
#     Ejemplo: `for indice, valor in enumerate(mi_lista):`)
print("\n3. Búsqueda de Primer Lote Conforme:")
resultados_pureza_lotes_ej3 = [97.5, 98.1, 97.9, 98.7, 99.2, 98.5]
pureza_minima_conforme_ej3 = 98.5
print(f"    Resultados de pureza a revisar: {resultados_pureza_lotes_ej3}")
print(f"    Pureza mínima conforme: {pureza_minima_conforme_ej3}")

lote_conforme_encontrado_ej3 = False
for indice, pureza in enumerate(resultados_pureza_lotes_ej3):
    print(f"    Revisando Lote índice {indice} con pureza: {pureza} %")
    if pureza >= pureza_minima_conforme_ej3:
        print(f"    Primer lote conforme encontrado: {pureza} % en la posición/índice {indice}.")
        lote_conforme_encontrado_ej3 = True
        break
    else: # Se ejecuta si el bicle for termina sin un break
        if not lote_conforme_encontrado_ej3:
            print(" Ningún lote conforme encontrado en esta secuencia.")
