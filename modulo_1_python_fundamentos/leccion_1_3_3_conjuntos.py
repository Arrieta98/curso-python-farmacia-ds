print("--- Lección 1.3.3: Conjuntos ---")

# --- Creación de Conjuntos ---
print("\n--- Creación de Conjuntos ---")
# Desde una lista con duplicados
lista_principios_activos_duplicados = ["Amoxicilina", "Ibuprofeno", "Amoxicilina", "Paracetamol", "Ibuprofeno", "Omeprazol"]
conjunto_pa_unicos = set(lista_principios_activos_duplicados)
print(f"Lista original con duplicados: {lista_principios_activos_duplicados}")
print(f"Conjunto de P.A. únicos (el orden puede variar): {conjunto_pa_unicos}")
print(f"Tipo de 'conjunto_pa_unicos': {type(conjunto_pa_unicos).__name__}")

# Creación directa con {}
numero_lotes_revisados = {101, 102, 103, 101, 104}  # El 101 duplicado se ignora
print(f"Número de lotes revisados (únicos): {numero_lotes_revisados}")

# Conjunto vacío (¡IMPORTANTE!)
conjunto_vacio_ok = set()
diccionario_vacio_error_si_esperas_set = {}
print(f"Conjunto vacío creado con set(): {conjunto_vacio_ok}, Tipo: {type(conjunto_vacio_ok).__name__}")
print(f"Diccionario vacío creado con {{}}: {diccionario_vacio_error_si_esperas_set}, Tipo: {type(diccionario_vacio_error_si_esperas_set).__name__}")

# --- Modificación de Conjuntos (.add, .remove, .discar, .pop, .clear) ---
print("\n--- Modificación de Conjuntos ---")
protocolos_seguridad_activos = {"PS-001", "PS-003", "PS-007"}
print(f"Protocolos de seguridad iniciales: {protocolos_seguridad_activos}")

# .add()
protocolos_seguridad_activos.add("PS-005")  # Añade un nuevo protocolo
print(f"Después de .add('PS-005'): {protocolos_seguridad_activos}")
protocolos_seguridad_activos.add('PS-001')  # Intentar añadir uno existente no cambia el conjunto
print(f"Despúes de .add('PS-001') de nuevo: {protocolos_seguridad_activos}")

# .discard() (seguro si el elemento no existe)
protocolos_seguridad_activos.discard('PS-009')  # PS-009 no existe, no hace nada, no da error
print(f"Despúes de .discard('PS-009) (no existía): {protocolos_seguridad_activos}")
protocolos_seguridad_activos.discard('PS-003')  # PS-003 sí existe
print(f"Después de .discard('PS-003'): {protocolos_seguridad_activos}")

# .remove() (da KeyError si el elemento no existe)
try:
    protocolos_seguridad_activos.remove("PS-007") # PS-007 sí existe
    print(f"Despúes de .remove('PS-007'): {protocolos_seguridad_activos}")
    # protocolo_seguridad_activos.remove("PS-007-OLD")  # Esto daría KeyError
except KeyError as e:
    print(f"Error esperado al usar .remove() para un elemento inexistente: {e}")

# .pop() elimina y devuelve un elemento arbitrario)
if protocolos_seguridad_activos:  # Solo si no está vacío
    elemento_eliminado_pop = protocolos_seguridad_activos.pop()
    print(f"Elemento eliminado con .pop(): {elemento_eliminado_pop}")
else:
    print("El conjunto está vacío, no se puede hacer .pop()")

# .clear()
protocolos_seguridad_activos.add("PS-TEMP")  # Añadir algo para limpiar
print(f"Antes de. clear(): {protocolos_seguridad_activos}")
protocolos_seguridad_activos.clear()
print(f"Después de .clear(): {protocolos_seguridad_activos}")

# --- Operaciones Matemáticas de Conjuntos ---
print("\n--- Operaciones Matemáticas de Conjuntos ---")
excipientes_formulacion_A = {"Lactosa", "Almidón", "Estearato de Magnesio", "Talco"}
excipientes_formulacion_B = {"Celulosa Microcristalina", "Almidón", "Dióxido de Silicio", "Talco"}
print(f"Exicpientes Formulación A: {excipientes_formulacion_A}")
print(f"Excipientes Formulacióm B: {excipientes_formulacion_B}")

# Unión (todos los excipientes únicos usados en A o B o ambos)
todos_excipientes_usados = excipientes_formulacion_A.union(excipientes_formulacion_B)
# o: excipientes_comunes_AB = excipientes_formulacion_A | excipientes_formulacion_B
print(f"Unión (todos los excipientes únicos): {todos_excipientes_usados}")

# Intersección (excipientes comunes a AMBAS formulaciones)
excipientes_comunes_AB = excipientes_formulacion_A.intersection(excipientes_formulacion_B)
# o: excipientes_comunes_AB = excipientes_formulacion_A & excipientes_formulacion_B
print(f"Intersección (excipientes comunes en A y B): {excipientes_comunes_AB}")

# Diferencia (excipientes que están en A PERO NO en B)
excipientes_solo_en_A = excipientes_formulacion_A.difference(excipientes_formulacion_B)
# o: excipientes_solo_en_A = excipientes_formulacion_A - excipientes_formulacion_B
print(f"Diferencia (excipientes solo en A, no en B): {excipientes_solo_en_A}")

# Diferencia (excipientes que están en B PERO NO en A)
excipientes_formulacion_B = excipientes_formulacion_B.difference(excipientes_formulacion_A)
# o excipientes_solo_en_B = excipientes_formulacion_B - excipientes_formulacion_B

# Diferencia Simétrica (excipientes que están en A o en B, PERO NO EN AMBOS)
excipientes_no_comunes_simetrica = excipientes_formulacion_A.symmetric_difference(excipientes_formulacion_B)
# o: excipientes_no_comunes_simetrica = excipientes_formulacion_A ^ excipientes_formulacion_B
print(f"Diferencia Simétrica(excipientes en A o B, pero no en ambos): {excipientes_no_comunes_simetrica}")

print("\n--- Otros Métodos y Operaciones ---")
# Usando excipientes_comunes_AB = {'Talco', 'Almidón'} (el orden puede variar)
# Usando excipientes_formulacion_A = {'Lactosa', 'Estearato de Magnesio', 'Talco', 'Almidón'}
print(f"Excipientes Comunes AB: {excipientes_comunes_AB}")
print(f"Excipientes Formulación A: {excipientes_formulacion_A}")

print(f"Longitud de excipientes_comunes_AB: {len(excipientes_comunes_AB)}")
print(f"¿'Lactosa' in excipientes_comunes_AB?: {'Lactosa' in excipientes_comunes_AB}")
print(f"¿'Talco' in excipientes_comunes_AB? {'Talco' in excipientes_comunes_AB}")

# .issubset() y .issperset()
print(f"¿ExcipientesComunesAB es subconjunto de FormulciónA? {excipientes_comunes_AB.issubset(excipientes_formulacion_A)}")
print(f"¿FormulaciónA es subconjunto de ExcipientesComunesAB? {excipientes_formulacion_A.issubset(excipientes_comunes_AB)}")

# . isdisjoint()
conjunto_X = {1, 2, 3}
conjunto_Y = {4, 5, 6}
conjunto_Z = {3, 7, 8}
print(f"Conjunto X: {conjunto_X}, Conjunto Y {conjunto_Y}, Conjunto Z: {conjunto_Z}")
print(f"¿X e Y son disjuntos (sin elementos comunes)? {conjunto_X.isdisjoint(conjunto_Y)}")  # True
print(f"X y Z son disjuntos? {conjunto_X.isdisjoint(conjunto_Z)}")  # False (comparten el 3)

print("\n--- Conjunto en Farmacovigilancia y Ensayos ---")

# 1. Efectos Adversos Únicos:
#    Tienes una lista de efectos adversos (EA) reportados en un estudio, con posibles duplicados.
#    `ea_reportados_estudio_X = ["Cefalea", "Náuseas", "Vértigo", "Cefalea", "Fatiga", "Náuseas", "Cefalea"]`
#    a) Obtén un conjunto de los EA únicos reportados.
#    b) Imprime el conjunto de EA únicos y cuántos tipos diferentes de EA se reportaron.

ea_reportados_estudio_X = ["Cefalea", "Náuseas", "Vértigo", "Cefalea", "Fatiga", "Náuseas", "Cefalea"]
print(f"\n1. EA Reportados (con duplicados): {ea_reportados_estudio_X}")
ea_unicos_estudio_X = set(ea_reportados_estudio_X)
print(f"    a) EA únicos reportados: {ea_unicos_estudio_X}")
print(f"    b) Números de tipos diferentes EA: {len(ea_unicos_estudio_X)}")

# 2. Comparación de Síntomas entre Pacientes:
#    Paciente A reporta los siguientes síntomas (como un conjunto):
#    `sintomas_pac_A = {"Fiebre", "Tos seca", "Dolor de garganta", "Cansancio"}`
#    Paciente B reporta:
#    `sintomas_pac_B = {"Tos seca", "Congestión nasal", "Cansancio", "Dolor muscular"}`
#    a) ¿Qué síntomas tienen en común ambos pacientes (intersección)?
#    b) ¿Qué síntomas tiene el Paciente A que no tiene el Paciente B (diferencia)?
#    c) ¿Qué síntomas tiene el Paciente B que no tiene el Paciente A (diferencia)?
#    d) ¿Cuáles son todos los síntomas únicos reportados entre ambos pacientes (unión)?

sintomas_pac_A = {"Fiebre", "Tos seca", "Dolor de garganta", "Cansancio"}
sintomas_pac_B = {"Tos seca", "Congestión nasal", "Cansancio", "Dolor muscular"}
print(f"\n2. Comparación de Síntomas:")
print(f"    Síntomas Paciente A: {sintomas_pac_A}")
print(f"    Síntomas Paciente B: {sintomas_pac_B}")

sintomas_comunes_AB = sintomas_pac_A.intersection(sintomas_pac_B)
print(f"    a) Síntomas comunes a A y B: {sintomas_comunes_AB}")

sintomas_solo_A = sintomas_pac_A.difference(sintomas_pac_B)
print(f"    b) Síntomas solo en Paciente A: {sintomas_solo_A}")

sintomas_solo_B = sintomas_pac_B.difference(sintomas_pac_A)
print(f"    c) Síntomas solo en Paciente B: {sintomas_solo_B}")

todos_sintomas_unicos_AB = sintomas_pac_A.union(sintomas_pac_B)
print(f"    d) Todos los síntomas únicos entre A y B: {todos_sintomas_unicos_AB}")

# 3. Gestión de Protocolos de Calidad Obligatorios:
#    Un producto farmacéutico debe cumplir con un conjunto base de protocolos de calidad:
#    `protocolos_base_obligatorios = {"PQC-01", "PQC-02", "PQC-03", "PQC-05"}`
#    Un lote específico, Lote Z, ha pasado los siguientes protocolos:
#    `protocolos_pasados_lote_Z = {"PQC-01", "PQC-03", "PQC-05", "PQC-07A"}`
#    a) ¿Cumple el Lote Z con todos los protocolos base obligatorios? (Usa `.issuperset()` o `.issubset()`).
#       Imprime un mensaje claro.
#    b) ¿Qué protocolos base obligatorios le faltan al Lote Z (si alguno)? (Usa diferencia).
#    c) ¿Qué protocolos adicionales (no base) ha pasado el Lote Z? (Usa diferencia).

print("\n3. Protocolos de Calidad:")
protocolos_base_obligatorios = {"PQC-01", "PQC-02", "PQC-03", "PQC-05"}
protocolos_pasados_lote_Z = {"PQC-01", "PQC-03", "PQC-05", "PQC-07A"}
print(f"    Protocolos base Obligatorios: {protocolos_base_obligatorios}")
print(f"    Protocolos Pasados por Lote Z: {protocolos_pasados_lote_Z}")

cumple_todos_base_3a = protocolos_pasados_lote_Z.issuperset(protocolos_base_obligatorios)
# Alternativamente: protocolos_base_obligatorios.issubset(protocolos_pasados_lote_Z)
if cumple_todos_base_3a:
    print(" a) El Lote Z CUMPLE con todos los protocolos obligatorios.")
else:
    print(" a) El Lote Z NO CUMPLE con todos los protocolos base obligatiorios.")

protocolos_faltantes_3b = protocolos_base_obligatorios.difference(protocolos_pasados_lote_Z)
if protocolos_faltantes_3b:
    print(f"    b) Protodolos base obligatorios que le faltan al Lote Z: {protocolos_faltantes_3b}")
else:
    print(f" b) Al Lote Z no le falta ningún protocolo base obligatorio (o ya los cumple todos si el mensaje de 'a' fue afirmativo).")
    if not cumple_todos_base_3a and not protocolos_faltantes_3b:  # Caso borde, si los pasados son un superconjunto estricto pero no igual
        print("     (Nota: El lote Z pasó otros protocolos además de los bases, pero no todos los base si 'a' fue negativo)")

protocolos_adicionales_pesados_3c = protocolos_pasados_lote_Z.difference(protocolos_base_obligatorios)
if protocolos_adicionales_pesados_3c:
    print(f"    c) Protocolos adicionales (no base) pasados por el Lote Z: {protocolos_adicionales_pesados_3c}")
else:
    print(f"    C) El Lote Z no ha pasado protocolos adicionales más allá de los base (o no ha pasado todos los base).")
