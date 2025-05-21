print("\n--- Lección 1.3.2: Diccionarios_ Modificación y Métodos Útiles ---")

# Diccionario de ejemplo: información de un lote de producción

info_lote_produccion = {
    "codigo_lote" : "AMX-CAPS-20250519-001",
    "producto_nombre" : "Amoxicilina 500mg Cápsulas",
    "cantidad_fabricacion_unidades" : 150000,
    "estado_qc" : "Pendiente de Análisis"
}
print(f"Información Inicial del Lote:\n{info_lote_produccion}")

# --- Añadir o Actualizar Pares Clave-Valor ---
print("\n--- Añadir/Actualizar Pares ---")
# Actualizar el estado de QC
info_lote_produccion["estado_qc"] = "En Análisis"
print(f"Después de añadir 'fecha_caducidad_estimada':\n{info_lote_produccion}")

# --- Eliminar Pares Clave-Valor ---
print("\n--- Eliminar Pares ---")
# Eliminar con 'del'
# Supongamos que 'analista_asignado_qc' fue un error temporal
if "analista_asignado_qc" in info_lote_produccion:     # Buena práctica verificar antes de 'del'
    del info_lote_produccion["analista_asignado_qc"]
    print(f"Después de 'del info_lote_produccion[\"analista_asignado_qc\"]':\n{info_lote_produccion}")
    
# Eliminar con .pop() (y obtener el valor)
# Supongamos que queremos procesar y luego eliminar la cantidad fabricada
if "cantidad_fabricada_unidades" in info_lote_produccion:
    cantidad_procesada = info_lote_produccion.pop("cantidad_fabricada_unidades")
    print(f"Cantidad procesada y eliminada con .pop(): {cantidad_procesada}")
    print(f"Diccionario después de .pop('cantidad_fabricada_unidades'):\n{info_lote_produccion}")
else:
    print("La clave 'cantidad_fabricada_unidades' no existe para .pop().")

# .popitem() (elimina y desvuelve el último par insertado en Python 3.7+)
if info_lote_produccion:  # solo si no está vacío
    ultimo_par_eliminado = info_lote_produccion.popitem()
    print(f"Último par clave-valor eliminado con .popitem(): {ultimo_par_eliminado}")
    print(f"Diccionario despúes de .popitem()\n{info_lote_produccion}")
else:
    print("El diccionario está vacío, no se puede usar .popitem().")
    
# Re-poblar un poco para los siguientes ejemplos
info_lote_produccion["estado_qc"] = "APROBADO"
info_lote_produccion["observaciones_qc"] = "Cumple especificaciones"

# --- Métodos .keys(), .values(), .items() ---
print("\n--- Métodos .keys(), .values(), .items() ---")
print(f"Diccionario actual:\n{info_lote_produccion}")

claves_lote = info_lote_produccion.keys()
print(f"Claves del lote (.keys()): {claves_lote}")  # Es un objeto vista
print(f"Claves como lista: {list(claves_lote)}")

valores_lote = info_lote_produccion.values()
print(f"Valores del lote (.values()): {valores_lote}")
print(f"Valores como lista: {list(valores_lote)}")

# --- Iteración sobre Diccionarios ---
print("\n--- Iteración sobre Diccionarios ---")
print("Iterando sobre claves (por defecto):")
for k in info_lote_produccion:
    print(f"    Clave: {k}, Valor: {info_lote_produccion[k]}")  #Accedemos al valor usando la clave
    
print("\nIterando sobre .items() (forma recomendada para clave y valor):")
for clave_item, valor_item in info_lote_produccion.items():
    clave_formateada = clave_item.replace("_", " ").capitalize()
    print(f"    {clave_formateada}: {valor_item}")

# --- Método .update() ---
print("\n--- Método .update() ---")
datos_adicionales_qc = {
    "fecha_aprobacion_qc" : "2025-05-20",
    "analista_qc_final" : " Dr. C. Arrieta",
    "estado_qc" : "LIBERADO"  # Esto actualizará el valor existente de "estado_qc"
}
print(f"Diccionario ANTES de .update:\n{info_lote_produccion}")
info_lote_produccion.update(datos_adicionales_qc)
print(f"Diccionario DESPUÉS de .update():\n{info_lote_produccion}")

# --- Método .clear() ---
print("\n--- Método .clear() ---")
copia_lote_para_limpiar = info_lote_produccion.copy()
print(f"Copia del diccionario ANTES de .clear(): {len(copia_lote_para_limpiar)} items")
copia_lote_para_limpiar.clear()
print(f"Copia del diccionario DESPÚES de .clear(): {len(copia_lote_para_limpiar)} items, Contenido: {copia_lote_para_limpiar}")

print("\n--- Gestión de Ficha Técnica de API ---")
ficha_tecnica_api = {
    "nombre_api" : "Ketoprofeno",
    "codigo_interno_api" : "API-KTP-003",
    "masa_molecular_g_mol" : 254.28,
    "punto_fusion_C" : "94-97 °C",
    "soluble_en" : ["Etanol", "Acetona", "Cloroformo", "Éter"],
    "requiere_condiciones_especiales_almacenamiento" : True
}
print("Ficha Técnica Inicial del API:")
for k, v in ficha_tecnica_api.items(): print(f" {k.replace('_', ' ').capitalize()}: {v}")

# 2. Eliminación de Información y Adición con .update():
#    a) Se considera que el `punto_fusion_C` ya no es un parámetro crítico para esta ficha simplificada.
#       Elimina esta clave y su valor del diccionario (usa `.pop()` y muestra el valor eliminado).
#    b) Tienes un nuevo conjunto de datos de solubilidad en un diccionario aparte:
#       `solubilidad_adicional = {"soluble_en_agua": "Muy poco soluble", "soluble_en_metanol": "Fácilmente soluble"}`
#       Usa `.update()` para añadir esta información a `ficha_tecnica_api`.
#       (Nota: esto no reemplazará la lista "soluble_en" original, sino que añadirá nuevas claves).
#    Imprime la ficha después de estas modificaciones.
print("\n2. Eliminado y Actulizando Ficha Técnica:")
if "punto_fusion_C" in ficha_tecnica_api:
    pf_eliminado = ficha_tecnica_api.pop("punto_fusion_C")
    print(f"    a) Punto de fusión eliminado: {repr(pf_eliminado)}")
else:
    print(" a) Clave 'punto_fusion_C' no encontrada para eliminar.")
    
solubilidad_adicional ={
    "soluble_en_agua" : "Muy poco soluble",
    "soluble_en_metanol" : "Fácilmente soluble"
}
ficha_tecnica_api.update(solubilidad_adicional)
print("Ficha Técnica Tras Eliminació y Update:")
for k, v in ficha_tecnica_api.items(): print(f" {k.replace('_', ' ').capitalize()}: {v}")

# 3. Listado de Propiedades y Conteo:
#    Para la `ficha_tecnica_api` actual:
#    a) Obtén e imprime una lista de todas las claves (nombres de las propiedades).
#    b) Obtén e imprime una lista de todos los valores.
#    c) Imprime el número total de propiedades (pares clave-valor) en la ficha.
#    d) Verifica si la clave "nombre_api" está presente en la ficha e imprime un mensaje.
#    e) Verifica si la clave "CAS_number" está presente e imprime un mensaje (debería ser que no).

print("\n3. Listado de Propiedades y Conteo:")
lista_claves_api = list(ficha_tecnica_api.keys())
print(f"    a) Claves de la Ficha API: {lista_claves_api}")

lista_valores_api = list(ficha_tecnica_api.values())
print(f"    b) Valores de la ficha API: {lista_valores_api}")  # # Nota: el orden de valores coincidirá con el de claves en Python 3.7+

num_propiedades_api = len(ficha_tecnica_api)
print(f"    c) Número total de propiedades en la ficha: {num_propiedades_api}")

clave_nombre_presente = "nombre_api" in ficha_tecnica_api
print(f"    d) ¿La clave 'nombre_api' está presente?: {clave_nombre_presente}")

clave_cas_presente = "CAS_number" in ficha_tecnica_api
print(f"    e) ¿La clave 'CAS_number' está presente? {clave_cas_presente}")