# Lección 1.5.2: Parámetros y Argumentos en Funciones
print("--- Lección 1.5.2: Parámetros y Argumentos---")

# --- Funciones con Parámetros y Argumentos Posicionales ---
def calcular_dosis_simple(peso_kg, dosis_mg_por_kg):
    """Calcula una dosis simple basada en el peso y la dosis por kg."""
    dosis_total_mg = peso_kg * dosis_mg_por_kg
    print(f"Para un paciente de {peso_kg} y una dosis de {dosis_mg_por_kg} mg/kg:")
    print(f"    La dosis total calculada es: {dosis_total_mg} mg")

# Llamadas con argumentos posicionales
calcular_dosis_simple(70, 10)  # peso_kg=70, dosis_mg_por_kg=10
calcular_dosis_simple(15.5, 5) # peso_kg=15.5, dosis_mg_por_kg=5

# --- Argumentos por Palabra Clave (Keyword Arguments) ---
print("\n--- Ejemplo 2: Argumentos por Palabra Clave ---")
def describir_lote(codigo_lote, producto_nombre, cantidad):
    """Describe un lote de producción."""
    print(f"Información del Lote:")
    print(f"    Código: {codigo_lote}")
    print(f"    Producto: {producto_nombre}")
    print(f"    Cantidad: {cantidad} unidades")
    
# Llamada usando argumentos por palabra clave (el orden no importa)
describir_lote(cantidad=15000, producto_nombre="Amoxicilina 250 mg", codigo_lote="AMX250-001")
describir_lote(codigo_lote="IBP400-005", cantidad=20000, producto_nombre="Ibuprofeno 400mg")

# Mezclando posicionales y keywords (posionales primero)
describir_lote("PCM500-010", cantidad=50000, producto_nombre="Paracetamol 500mg")
# describir_lote(codigo_lote="ERROR-001", 500, producto_nombre="Error") # ERROR si posicional después de keyword

# --- Parámetros con valores por Defecto ---
print("\n--- Ejemplo 3: Parámetros con valores por Defecto ---")
def registrar_parametro_qc(
    nombre_parametro,
    valor_medido,
    unidad="mg/mL",
    estado="PENDIENTE DE REVISIÓN"
):
    """Registra un parámetro de control de calidad con valores po defecto."""
    print(f"Parámetro QC Registrado:")
    print(f"    Nombre: {nombre_parametro}")
    print(f"    Valor Medido: {valor_medido} {unidad}")
    print(f"    Estado: {estado}")
    
# Llamadas unsando valores por defecto
registrar_parametro_qc("Pureza API", 99.85, unidad="%")  #estado usa valor por defecto
registrar_parametro_qc("Contenido Humedad", 0.5, "%", "APROBADO")  # Todos los args provistos
registrar_parametro_qc("pH Solución", 7.02)  # unidad y estado usan valor por defecto
registrar_parametro_qc(valor_medido=15.2, nombre_parametro="Viscocidad", unidad="cp")  # Usando keywords

# --- Funciones Farmacéuticas con Parámetros ---
print("\n--- Funciones Farmacéuticas con Parámetros ---")
# 1. Función para Calcular el Volumen de Dilución:
#    Define una función `calcular_volumen_final_dilucion(c1, v1, c2)` donde:
#    - `c1` = concentración inicial (ej. 10 M)
#    - `v1` = volumen inicial (ej. 5 mL)
#    - `c2` = concentración final deseada (ej. 0.5 M)
#    La función debe calcular `v2` (volumen final) usando `c1*v1 = c2*v2`.
#    Debe imprimir el `v2` calculado con un mensaje descriptivo.
#    Llama a la función con valores de prueba.
def calcular_volumen_final_dilucion(c1, v1, c2):
    """Calcula el volumen final (V2) para una dilución (C1V1 = C2V2)."""
    if c2 == 0:
        print("Error: La concentración final (C2) no puede ser cero para este cálculo.")
        return  # Salir de la función
    
    v2 = (c1 * v1) / c2
    
    print(f"Para diluir una solución de {v1} mL a {c1} M hasta una concentración de {c2} M,")
    print(f"    se necesita un volumen final de: {v2:.2f} mL.")
    
print("\n1 Cálculo de volumen de Dilución:")
calcular_volumen_final_dilucion(c1=10.0, v1=5.0, c2=0.5)  # # 10 M, 5 mL, 0.5 M
calcular_volumen_final_dilucion(1.0, 25.0, 0.1)  # 1 M, 25 mL, 0.1 M
calcular_volumen_final_dilucion(5.0, 10.0, 0)    # Prueba con C2 = 0

# 2. Función para Generar un ID de Muestra:
#    Define una función `generar_id_muestra(tipo_muestra, anio, secuencial, sitio_estudio="SITIO_CENTRAL")`
#    - `tipo_muestra`: string, ej. "SANGRE", "API"
#    - `anio`: int, ej. 2025
#    - `secuencial`: int, ej. 7
#    - `sitio_estudio`: string, con valor por defecto "SITIO_CENTRAL"
#    La función debe construir y luego imprimir un ID de muestra formateado como:
#    "TIPO-AÑO-SITIO-SECUENCIAL_FORMATEADO" (ej. "SANGRE-2025-SITIO_CENTRAL-007")
#    (El secuencial debe tener 3 dígitos, con ceros a la izquierda si es necesario).
#    Llama a la función varias veces:
#      - Una vez con todos los argumentos.
#      - Una vez usando el `sitio_estudio` por defecto.
def generar_id_muestra(tipo_muestra, anio, secuencial, sitio_estudio="SITIO_CENTRAL"):
    """Genera un ID de muestra formateado."""
    # Asegurarse de que el secuencial tenga 3 dígitos
    secuencial_formateado = f"{secuencial:03d}"
    id_generado = f"{tipo_muestra.upper()}-{anio}-{sitio_estudio.upper()}-{secuencial_formateado}"
    print(f"ID de Muestra Generado: {id_generado}")
    
print("\n2. Generación de ID de Muestra:")
generar_id_muestra("PLASMA", 2025, 12, "SITIO-NORTE")
generar_id_muestra(tipo_muestra="API_LOTE_X", anio=2024, secuencial=1)  # Usa sitio por defecto
generar_id_muestra("ORINA", 2025, 123, sitio_estudio="SITIO_SUR")

# 3. Función para Etiquetar un Reactivo:
#    Define una función `etiquetar_reactivo(nombre_reactivo, lote, fecha_apertura, fecha_caducidad="Consultar Certificado")`
#    - `nombre_reactivo`: string
#    - `lote`: string
#    - `fecha_apertura`: string (ej. "2025-05-20")
#    - `fecha_caducidad`: string, con valor por defecto "Consultar Certificado"
#    La función debe imprimir una etiqueta formateada como:
#    "REACTIVO: [Nombre Reactivo]"
#    "LOTE: [Lote]"
#    "FECHA APERTURA: [Fecha Apertura]"
#    "FECHA CADUCIDAD: [Fecha Caducidad]"
#    Llama a la función:
#      - Para "Ácido Clorhídrico 0.1N", lote "ACL0125A", fecha apertura "2025-05-20".
#      - Para "Buffer Fosfato pH 7.0", lote "BUFPH7-003B", fecha apertura "2025-04-10", fecha caducidad "2026-04-09".

def etiquetar_reactivo(nombre_reactivo, lote, fecha_apertura, fecha_caducidad="Consultar Certifiaco"):
    """Imprime una etiqueta formateada para un reactivo."""
    print(f"\n--- ETIQUETA DE REACTIVO ---")
    print(f"REACTIVO: {nombre_reactivo}")
    print(f"LOTE: {lote}")
    print(f"FECHA APERTURA: {fecha_apertura}")
    print(f"Fecha CADUCIDAD: {fecha_caducidad}")
    print(f"---------------------------")
    
etiquetar_reactivo("Ácido Clorhídrico 0.1N", "ACL0125A", "2025-05-20")
etiquetar_reactivo(
    nombre_reactivo="Buffer Fosfato pH 7.0", 
    lote="BUFPH7-003B", 
    fecha_apertura="2025-04-10", 
    fecha_caducidad="2026-04-09"
)