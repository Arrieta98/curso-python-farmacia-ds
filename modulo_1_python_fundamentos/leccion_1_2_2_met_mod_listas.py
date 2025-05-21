print("\n--- Lección 1.2.2: Listas - Métodos de Modificación ---")

#--- .append(item): Añadir al final ---
print("\n--- Método .append ---")
farmacos_antihipertensivos = ["Enalapril", "Losartán", "Amlodipino"]
print(f"Antihipertensivos iniciales: {farmacos_antihipertensivos}")

farmacos_antihipertensivos.append("Hidroclorotiazida")  # Añade al final
print(f"Después de append('Hidroclorotiazida'): {farmacos_antihipertensivos}")

farmacos_antihipertensivos.append("Candesartán")
print(f"Después de append('Candesartán'): {farmacos_antihipertensivos}")

# --- .insert(indice, item): Insertar en una posición ---
print("\n--- Método .insert() ---")
# Queremos insertar "Valsartán" después de "Losartán" (que está en índice 1)
# Entonces, lo insertaremos en el índice 2
farmacos_antihipertensivos.insert(2, "Valsartán")
print(f"Despues de inset (2, 'Valsartán'): {farmacos_antihipertensivos}")

# Insetar al principio (índice 0)
farmacos_antihipertensivos.insert(0, "Lisinopril")
print(f"Después de insert(0, 'Lisinopril'): {farmacos_antihipertensivos}")

# --- .extend(iterable): Añadir múltiples elementos de otro inetrable ---
print("\n--- Método .extende() ---")
nuevos_diureticos = ["Furosemida", "Espironolactona"]
# farmacos_antihipertensivos ya contiene "Hidroclorotiazida"
# Vamos a añadir más diuréticos a una lista separada primero
lista_diureticos = ["Clortalidona"]
lista_diureticos.extend(nuevos_diureticos)
print(f"Lista de diuréticos despúes de extend: {lista_diureticos}")

# Añadir la lista_direticos a farmacos_antihipertensivos
# Esto es de diferente de append:
farmacos_antihipertensivos.extend(lista_diureticos) # Esto añade los ELEMENTOS de lista_diureticos
print(f"Anitihipertensivos después de extend(lista_diuréticos): {farmacos_antihipertensivos}")

# --- Modificación de un Elemento por Índice ---
print("\n--- Modificación por Índice ---")
# Supongamos que 'Lisinopril debe ser 'Ramipril'
print(f"Lista antes de cambiar 'Lisinopril': {farmacos_antihipertensivos}")
if "Lisinopril" in farmacos_antihipertensivos:
    indice_lisinopril = farmacos_antihipertensivos.index("Lisinopril")
    farmacos_antihipertensivos[indice_lisinopril] = "Ramipril"
    print(f"Lista después de cambiar 'Lisinopril' a 'Ramipril': {farmacos_antihipertensivos}")
else:
    print("'Lisinopril' no encontrado para cambiar")
    
# ---- .pop(indice_opcional): Elimianr y devolver elemento ---
print("\n--- Método .pop() ---")
print(f"Lista actual para pop: {farmacos_antihipertensivos}")
ultimo_farmaco_añadido = farmacos_antihipertensivos.pop()  # Elimina y devuelve el último ("Espironolactona")
print(f"Se eliminó (pop sin índice): '{ultimo_farmaco_añadido}'")
print(f"Lista después de pop(): {farmacos_antihipertensivos}")


# Eliminar el fármaco en el índice 1 ("Enalapril")
farmaco_indice_1 = farmacos_antihipertensivos.pop(1)
print(f"Se eliminó (pop de índice 1): '{farmaco_indice_1}'")
print(f"Lista despúes de pop(1): {farmacos_antihipertensivos}")

# --- .remove(valor): Eliminar la primera ocurrencia de un valor ---
print("\n --- Método .remove() ---")
# Supongomas que queremos eliminar "Furosemidad"
print(f"Lista actual para remove: {farmacos_antihipertensivos}")
if "Furosemida" in farmacos_antihipertensivos:
    farmacos_antihipertensivos.remove("Furosemida")
    print(f"Después de remove('Furosemida'): {farmacos_antihipertensivos}")
else:
    print("'Furosemina' no encontrado para eliminar.")
    
# Si el valor no existe, .remove() da un ValueError
try:
    farmacos_antihipertensivos.remove("MedicamentosInexistente")
except ValueError as e:
    print(f"Error esperado al intentar remove('MedicamentoInexistente'): {e}")
    
# --- del lista[indice] y del lista [slice]: Eliminar por índice o slice ---
print("\n--- Sentencia del ---")
# Lista de códigos de muestras, algunos son erróneos
codigos_muestra_lab = ["M01-OK", "M02-ERR", "M03-OK", "M04-OK", "M05-ERR"]
print(f"Códigos de muestra iniciales: {codigos_muestra_lab}")

# Eliminar la muestra erónea en el índice 1 ("M02-ERR")
if len(codigos_muestra_lab) > 1:
    del codigos_muestra_lab[1]
    print(f"Después de 'del codigos_muestra_lab[1]': {codigos_muestra_lab}")
    
# Ahora "M05-ERR" está en el índice -1 (o 3)
# Vamos a eliminarla
if "M05-ERR" in codigos_muestra_lab:
    indice_m05_err = codigos_muestra_lab.index("M05-ERR")
    del codigos_muestra_lab[indice_m05_err]
    print(f"Despúes de eliminar 'M05-ERR' por índice: {codigos_muestra_lab}")

print("\n--- Gestión de un Formulario de Medicamentos ---")

# 1. Formulario Inicial:
#   Comienzas con una lista de medicamentos esenciales para un kit de emergencia.
kit_emergencia = ["Adrenalina Inyectable", "Salbutamol Inhalador", "Nitroglicerina Sublingual"]
print(f"1. Kit de mergencia inicial: {kit_emergencia}")

# 2. Añadir Medicamentos:
#    a) Se decide añadir "Diazepam Inyectable" al final de la lista.
#    b) Luego, se considera que "Glucosa Hipertónica" es muy importante y debe ir
#       justo después de "Adrenalina Inyectable" (que está en el índice 0).
kit_emergencia.append("Diazepam Inyectable")
print(f"2a. Kit tras añadir Diazepam: {kit_emergencia}")
kit_emergencia.insert(1, "Glucosa Hipertónica")

# 3. Reemplazar un Medicamento:
#    Se descubre que "Nitroglicerina Sublingual" está próxima a caducar y se
#    reemplaza por "Isosorbide Dinitrato Sublingual".
#    Encuentra el índice de "Nitroglicerina Sublingual" y reemplázalo.

medicamento_a_reemplazar = "Nitroglicerina Sublingual"
medicamento_nuevo = "Isosorbide Dinitrato Sublingual"
if medicamento_a_reemplazar in kit_emergencia:
    indice_reemplazo = kit_emergencia.index(medicamento_a_reemplazar)
    kit_emergencia[indice_reemplazo] = medicamento_nuevo
    print(f"3a. Kit tras reemplazar {medicamento_a_reemplazar}: {kit_emergencia}")
else:
    print(f"3a. {medicamento_a_reemplazar} no encontrado para reemplazar")

# 4. Eliminar Medicamentos:
#    a) Se decide que "Salbutamol Inhalador" se manejará en un kit respiratorio separado.
#       Elimina "Salbutamol Inhalador" de la lista usando su valor.
#    b) El primer medicamento de la lista actual (después de las modificaciones anteriores)
#       se traslada a otro compartimento. Elimina el primer medicamento de la lista
#       y guarda el nombre del medicamento eliminado en una variable.

medicamento_a_eliminar_valor = "Salbutamol Inhalador"
if medicamento_a_eliminar_valor in kit_emergencia:
    kit_emergencia.remove(medicamento_a_eliminar_valor)
    print(f"4a. Kit tras eliminar {medicamento_a_eliminar_valor}: {kit_emergencia}")
else:
    print(f"4a. {medicamento_a_eliminar_valor} no encontrado para eliminar.")

if kit_emergencia:  # Verigicar que la lista no esté vacía
    primer_medicamento_trasladado = kit_emergencia.pop(0)
    print(f"4b. Medicamento trasladado (era el primero): {primer_medicamento_trasladado}")
    print(f"    Kit final: {kit_emergencia}")
else:
    print(f"4b. El kit de emergencia está vacío, no se puede trasladar el prier medicamento")

# Lista de Tareas Pendientes de Validación de Lote:
#    `tareas_validacion_lote = ["Verificar Documentación", "Muestreo", "Análisis Físico-Químico", "Análisis Microbiológico", "Elaborar Reporte"]`
#    a) Has completado el "Muestreo". Elimina esta tarea de la lista.
#    b) Te das cuenta de que olvidaste un paso: "Revisión de Protocolo" debe ir justo antes de "Verificar Documentación". Insértalo.
#    c) Al final de todo, debes "Archivar Documentación". Añade esta tarea.
#    d) Imprime la lista final de tareas.}
tareas_validacion_lote = [
    "Verificar Documentación", "Muestreo", "Análisis Físico-Químico",
    "Análisis Microbiológico", "Elaborar Reporte"
]
print(f"\n5. Tareas de validación iniciales: {tareas_validacion_lote}")
# a) Completar Muestreo
if "Muestreo" in tareas_validacion_lote:
    tareas_validacion_lote.remove("Muestreo")
    print(f"    a) Tras completar Muestreo {tareas_validacion_lote}")
    
# b) Insertar Revisión de Protocolo
tareas_validacion_lote.insert(0, "Revisión de Protocolo")
print(f"    b) Tras insertar Revisión de Protocolo: {tareas_validacion_lote}")

# c) Añadir Archivar Documentación
tareas_validacion_lote.append("Archivar Documentación")
print(f"    c) Tras añadir Archivar Documentación: {tareas_validacion_lote}")

print(f"    d) Lista final de tareas de validación {tareas_validacion_lote}")