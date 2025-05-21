print(f"--- Leccion 1.2.3: Listas - Métodos adicionales y Operaciones ---")

# --- .sort() y sorted() ---
print("\n--- Ordenamiento: .sor() y sorted () ---")
concentraciones_obtenidas_mg_mL = [10.2, 9.8, 10.5, 10.1, 10.2]
print(f"Concentraciones originales: {concentraciones_obtenidas_mg_mL}")

# Usando sorted para obtener una nueva lista ordenada sin modificar la original
concentraciones_ordenadas_asc = sorted(concentraciones_obtenidas_mg_mL)
print(f"Ordenar ascendente (con sorted()): {concentraciones_ordenadas_asc}")
print(f"Original después de sorted(): {concentraciones_obtenidas_mg_mL}")

concentraciones_ordenadas_desc = sorted(concentraciones_obtenidas_mg_mL, reverse = True)
print(f"Ordenadas descentente: {concentraciones_ordenadas_desc}")

# Usando .sort() para ordenar la lista original in-place
print(f"\nOriginal ANTES de .sort: {concentraciones_obtenidas_mg_mL}")
concentraciones_obtenidas_mg_mL.sort()  # Ordena ascendente por defecto
print(f"Original DESPUÉS DE .sort() ascendente: {concentraciones_obtenidas_mg_mL}")

concentraciones_obtenidas_mg_mL.sort(reverse = True)
print(f"Original DESPUÉS DE .sort() descendente: {concentraciones_obtenidas_mg_mL}")

# Ordenar listas de strings (alfabpeticamente)
nombres_principios_activos = ["Paracetamol", "Ibuprofeno", "Aspirina", "Diclofenaco"]
print(f"\nPrincipios activos originales: {nombres_principios_activos}")
nombres_principios_activos.sort()
print(f"Principios activos ordenados: {nombres_principios_activos}")

# --- .reverese ---
print("\n--- Conteo: .count() ---")
# concentraciones_obtenidas_mg_ml es [10.5, 10.2, 10.2, 10.1, 9.8, 9.5] después del último sort y reverse
# Vamos a redefinirla para un ejemplo claro de count
lecturas_ph_repetidas = [7.0, 7.1, 7.0, 7.2, 7.0, 6.9, 7.1]
print(f"Lecturas de PH: {lecturas_ph_repetidas}")
conteo_ph_7_0 = lecturas_ph_repetidas.count(7.0)
print(f"Número de veces que aparece pH 7.0: {conteo_ph_7_0}")
conteo_ph_7_5 = lecturas_ph_repetidas.count(7.5)
print(f"Número de veces que aparece pH 7.5: {conteo_ph_7_5}")

# --- .index(valor) ---
print("\n--- Búsqueda de índce: .index() ---")
# nombres_principios_activos es ['Paracetamol', 'Ibuprofeno', 'Diclofenaco', 'Aspirina']
print(f"Lista actual de P.A.: {nombres_principios_activos}")
try:
    indice_ibuprofeno = nombres_principios_activos.index("Ibuprofeno")
    print(f"El índice de 'Ibuprofeno' es: {indice_ibuprofeno}")
    
    # Buscando desde un índice específico
    # Añadimos "Ibuprofeno al final para probar la búsqueda desde un punto"
    nombres_principios_activos.append("Ibuprofeno")
    print(f"Lista con 'Ibuprofeno' duplicado: {nombres_principios_activos}")
    # Buscar "Ibuprofeno" empezando después de su primera ocurrencia (índice_ibuprofeno +1)"
    indice_segundo_ibuprofeno = nombres_principios_activos.index("Ibuprofeno", indice_ibuprofeno + 1)
    print(f"El índece del segundo 'Ibuprofeno' es: {indice_segundo_ibuprofeno}")
    
    # indice_omeprazol = nombres_principios_activos.index("Omeprazol")  # Esto daría un ValueError
except ValueError as e:
    print(f"Error al buscar con .index: {e}")
    
# --- Operador "in" ---
print("\n--- Pertenencia: operador 'in' ---")
print(f"Lista de P.A.: {nombres_principios_activos}")
esta_aspirina = "Aspirina" in nombres_principios_activos
print(f"¿'Aspirina' está en la lista?: {esta_aspirina}")
esta_metformina = "Metformina" in nombres_principios_activos
print(f"¿'Metformina' está en la lista?: {esta_metformina}")

# Uso seguro antes de .remove o .index()
farmaco_a_buscar = "Diclofenaco"
if farmaco_a_buscar in nombres_principios_activos:
    print(f"{repr(farmaco_a_buscar)} encontrado en el índice {nombres_principios_activos.index('Diclofenaco')}")
else:
    print(f"{repr(farmaco_a_buscar)} no encontrado.")

# --- .copy o slicing[:] para copiar ---
print("\n--- Copia de Listas .copy() o [:] ---")
lista_protocolo_original = ["Paso A", "Paso B", "Paso C"]
print(f"Protocolo Original: {lista_protocolo_original}")

# Copia usando .copy()
copia_protocolo_1 = lista_protocolo_original.copy()
# Cipia usando slicing
copia_protocolo_2 = lista_protocolo_original[:]

# Modificar una copia no afecta a la otra ni a la original
copia_protocolo_1[0] = "Paso A Modificado"
copia_protocolo_2.append("Paso D en copia 2")

print(f"Protocolo Original (sin cambios): {lista_protocolo_original}")
print(f"Copia 1(modificada): {copia_protocolo_1}")
print(f"Copia 2 (con append): {copia_protocolo_2}")

# --- Concatenación (+) y Multiplicación (*) ---
print("\n--- Concatenación y Multiplicación ---")
excipientes_base = ["Lactosa", "Almidón"]
excipientes_adicionales = ["Estearato de Magnesio", "Talco"]

# Concatenación con + (crea una nueva lista)
formulario_completo = excipientes_base + excipientes_adicionales
print(f"Excipientes base: {excipientes_base}")
print(f"Excipientes adicionales: {excipientes_adicionales}")
print(f"Formulario completos (+): {formulario_completo}")
print(f"Excipientes base (sin cambios por +): {excipientes_base}") # Original

# Multiplicación * (crea una nueva lista)
marcadores_placebo = ["P"] * 5 # Crea una lista con 5 "P"
print(f"Maracadores placebo (*): {marcadores_placebo}")

print("\n--- Análisis de Lotes de Producción ---")
# 1. Tienes una lista de porcentajes de pureza de varios análisis de un lote:
purezas_lote_X = [99.5, 98.9, 99.8, 99.1, 98.7, 99.5, 100.1, 99.0]
print(f"1. Purezas del Lote X (%): {purezas_lote_X}")
#    a) ¿Cuántos análisis se realizaron?
#    b) Ordena las purezas de menor a mayor (modificando la lista original). Imprime la lista ordenada.
#    c) ¿Cuál fue la pureza más baja y la más alta registrada (después de ordenar)?
#    d) ¿Cuántas veces se registró una pureza del 99.5%?

num_analisis_1 = len(purezas_lote_X)
print(f"    a) Número de análisis realizado: {num_analisis_1}")
purezas_lote_X.sort()
print(f"    b) Purezas ordenadas de menor a mayor: {purezas_lote_X}")
pureza_mas_baja_1 = purezas_lote_X[0]
pureza_mas_alta_2 = purezas_lote_X[-1]
print(f"    c) Pureza más baja: {pureza_mas_baja_1} %, Pureza más alta: {pureza_mas_alta_2} %")

conteo_pureza_99_5_1 = purezas_lote_X.count(99.5)
print(f"    d) Número de veces que se registró 99.5 %: {conteo_pureza_99_5_1}")

# 2. Lista de Protocolos de Seguridad Aplicados a un Proceso:
protocolos_aplicados_proceso_Y = ["PS-001", "PS-003", "PS-002", "PS-005"]
protocolo_critico = "PS-004"
print(f"\n2. Protocolos aplicados al proceso Y: {protocolos_aplicados_proceso_Y}")
#    a) Verifica si el `protocolo_critico` "PS-004" ya ha sido aplicado. Imprime un mensaje.
#    b) Si no ha sido aplicado, añádelo a la lista.
#    c) Crea una copia de la lista de protocolos. En la copia, invierte el orden de los protocolos.
#    d) Imprime la lista original y la copia invertida.
if protocolo_critico in protocolos_aplicados_proceso_Y:
    print(f"    a) El producto crítico {repr(protocolo_critico)} YA ha sifo aplicado")
else:
    print(f"    a) El protocolo crítico {repr(protocolo_critico)} NO ha sido aplicado")
    protocolos_aplicados_proceso_Y.append(protocolo_critico)  # b)
    print(f"    {repr(protocolo_critico)} añadido. Lista actual: {protocolos_aplicados_proceso_Y}")

copia_protocolos_2c = protocolos_aplicados_proceso_Y.copy()
copia_protocolos_2c.reverse()
print(f"    d) Lista original de protocolos: {protocolos_aplicados_proceso_Y}")
print(f"    Copia Invertida de protocolos: {copia_protocolos_2c}")


# 3. Concatenar Listas de Eventos Adversos:
#    Tienes dos listas de eventos adversos (EA) reportados para un fármaco en dos estudios diferentes:

ea_estudio_1 = ["Cefalea", "Náuseas", "Mareo"]
ea_estudio_2 = ["Fatiga", "Cefalea", "Diarrea", "Náuseas"]
#    a) Crea una nueva lista `todos_ea_reportados` que combine todos los eventos de ambos estudios.
#    b) Imprime `todos_ea_reportados`.
#    c) ¿Cuántos reportes de "Cefalea" hubo en total en la lista combinada?
#    d) ¿Cuántos reportes de "Vómito" hubo en la lista combinada?
#    e) (Reto opcional) Crea una lista de eventos adversos *únicos* a partir de `todos_ea_reportados`.
#       (Pista: puedes convertir la lista a un conjunto (`set()`) y luego de nuevo a lista, o iterar y añadir si no está ya).
print(f"\n3. Eventos Adversos:")
print(f"    Estudio 1: {ea_estudio_1}")
print(f"    Estudio 2: {ea_estudio_2}")
todos_ea_reportados = ea_estudio_1 + ea_estudio_2
print(f"    a,b) Todos los EA reportados: {todos_ea_reportados}")
conteo_cefalea_3c = todos_ea_reportados.count("Cefalea")
print(f"    c) Reportes totales de 'Cefalea': {conteo_cefalea_3c}")
conteo_vomito_3d = todos_ea_reportados.count("Vómito")
print(f"    d) Reportes totales de 'Vómito': {conteo_vomito_3d}")

# Mpetodo 1: Usando  set
ea_unicos_set = set(todos_ea_reportados)
ea_unicos_lista_3e = list(ea_unicos_set)
# Opcionalmente, ordenarla si se desea una salida consistente, aunque los sets no tienen orden
ea_unicos_lista_3e.sort()
print(f"    Se convierte a conjunto: {ea_unicos_set}")
print(f"    Se conviere a lista: {ea_unicos_lista_3e}")
print(f"    e) Eventos Aversos únicos (ordenados): {ea_unicos_lista_3e}")