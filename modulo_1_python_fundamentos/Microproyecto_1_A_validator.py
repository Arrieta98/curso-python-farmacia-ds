# Micro-Proyecto Sección 1.A: Validador y Formateador Básico de Datos de Lotes
# Este script solicita al usuario datos de un lote farmacéutico,
# realiza validaciones básicas y genera un resumen si los datos son válidos.

print("--- Validador de Datos de Lotes Farmacéuticos ---")
print("Por favor, ingrese la información solicitada para el nuevo lote.\n")

codigo_lote_ingresado = ""
nombre_producto_ingresado = ""
cantidad_producidad_ingresada_str = ""
ph_medido_ingresado_str = ""
fecha_fabricacion_ingresada = ""

# Variables para almacenar convertidos y validados
cantidad_producidad_validada = None
ph_medido_valido = None

# Bandera para el estado general de validación
todos_los_datos_validos = True

# --- 1. Entrada y Validación: Código de Lote ---
print("\n--- Validación: Código de Lote ---")
codigo_lote_ingresado = input(
    "Ingrese el Código de Lote (ej: LFM-2025-007): "
).strip()

# Validación a: Longitud entre 10 y 20 caracteres
if not (10 <= len(codigo_lote_ingresado) <= 20):
    print("INVÁLIDO: El código de lote debe tener entre 10 y 20 caracteres.")
else:
    print(
        "VÁLIDO: Longitud correcta."
    )

# Validación b: Debe empezar con "L" (insensible a mayúsculas/minúsculas para la comprobación)
# Guardamos el original, pero para la comprobación lo pasamos a mayúsculas.
if todos_los_datos_validos:  # Solo continuar si la validación anterior pasó (o si quiere validar todo independientemente):
    if not codigo_lote_ingresado.upper().startswith("L"):
        print("INVÁLIDO: El código de lote debe comenzar con la letra 'L'.")
        todos_los_datos_validos = False
    else:
        print("VÁLIDO: Comienza con 'L'.")
# Validación c: Debe contener al menos un gion "-"
if todos_los_datos_validos is True:  # Continuar si las validaciones anteriores pasaron
    if "-" not in codigo_lote_ingresado:
        print("INVÁLIDO: El código de lote debe contener al menos un guion '-'.")
        todos_los_datos_validos = False
    else:
        print("VÁLIDO: Contiene al menos un guion.")

if not todos_los_datos_validos:
    print("NOTA: Como el código de lote tiene errores, algunas validaciones posteriores podrían no ser precisas o no ejecutarse.")
    
# --- 2. Entrada y Validación: Nombre del Producto
print("\n--- Validación: Nombre del Producto ---")
nombre_producto_ingresado = input("Ingrese el Nombre del Producto (ej. Amoxicilina 500mg Comprimidos): ").strip()

if not nombre_producto_ingresado:  # Verifica si el string está vacío después de strip ()
    print("INVÁLIDOS: El nombre del producto no puede estar vacío")
    todos_los_datos_validos = False  # Actualiza la bandera general
else:
    print("VÁLIDO: Nombre del producto ingresado.")

# --- 3. Entrada y Validación: Cantidad Producida ---
print("\n--- Validación: Cantidad Producidad ---")
cantidad_producida_ingresada_str = input("Ingrese la Cantidad Producida (unidades, ej:. 150000: ").strip()

# Intentamos la conversión a entero y luego validamos
try:
    cantidad_producida_valida = int(cantidad_producida_ingresada_str)  # Intentar convertir a entero
    
    # Validación: Debe ser un número positivo
    if cantidad_producida_valida > 0:
        print(f"VÁLIDO: Cantidad producidad es {cantidad_producida_valida}")
    else:
        print("INVÁLIDO: La cantidad producida debe ser un número entero positivo (mayor que cero).")
        todos_los_datos_validos = False
        cantidad_producida_valida = None  # Aseguramos que no use un valor inválido

except ValueError:
     # Esto se ejecuta si int() falla (ej. el usuario ingresó "muchas" o "150.50")
    print(f"INVÁLIDO: La cantidad producida {repr(cantidad_producida_ingresada_str)} no es un número válido")
    todos_los_datos_validos = False
    cantidad_producida_validad = None  # Aseguramos que no use un valor inválido.
# --- 4. Entrada y Validación: pH Medido ---
print("\n--- Validación: pH Medido ---")
ph_medido_ingresado_str = input("Ingrese el pH Medido (ej. 6.85): ").strip()

# Definir límites de especificación para el pH
ph_limite_inferior = 5.0
ph_limite_superior = 8.0

try:
    ph_medido_valido = float(ph_medido_ingresado_str)  # Intentar convertir a flotante
    
    # Validación: Debe estar dentro del rango [ph_limite_inferior, ph_limite_superior]
    if ph_limite_inferior <= ph_medido_valido <= ph_limite_superior:
        print(f"VÁLIDO: pH medido es {ph_medido_valido:.2f}.") # Formateamos a 2 decimales para mostrar
        # ph_medido_valido ya tiene el valor float correcto para usar después
    else:
        print(f"INVÁLIDO: El pH medido ({ph_medido_valido:.2f}) está fuera del rango aceptable [{ph_limite_inferior} - {ph_limite_superior}].")
except ValueError:
     # Esto se ejecuta si float() falla (ej. el usuario ingresó "siete" o "6,8" con coma)
     print(f"INVÁLIDO: El pH medido {repr(ph_medido_ingresado_str)} no es un número decimal válido.")
     todos_los_datos_validos = False
     ph_medido_valido = None # Aseguramos que no use un valor inválido
     
# --- 5. Entrada y Validación: Fecha de Fabricación ---
print("\n--- Validación: Fecha de Fabricación ---")
fecha_fabricacion_ingresada = input("Ingrese la Fecha de Fabricación (YYYY-MM-DD): ").strip()

# Validación de formato simple: YYYY-MM-DD
# a) Longitud debe ser 10
# b) Debe tener guiones en las posiciones 4 y 7
# c) Las partes entre guiones (año, mes, día) deben ser dígitos

formato_fecha_valido = False # Suponemos inválido hasta que pase todas las pruebas
if len(fecha_fabricacion_ingresada) == 10:
    if fecha_fabricacion_ingresada[4] == '-' and fecha_fabricacion_ingresada[7] == '-':
        partes_fecha = fecha_fabricacion_ingresada.split('-')  # Divide por el guion: ['YYYY', 'MM', 'DD']
        if len(partes_fecha) == 3:
            anio_str, mes_str, dia_str = partes_fecha  # Desempaquetamos
            if anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit():
                formato_fecha_valido = True
            
if formato_fecha_valido:
    print(f"VÁLIDO: Formato de fecha {repr(fecha_fabricacion_ingresada)} es correcto.")
    # fecha_fabricacion_ingresada ya tiene el string correcto para usar después
else:
    print(f"INVÁLIDO: El formato de fecha {repr(fecha_fabricacion_ingresada)} no es YYYY-MM-DD o contiene caracteres no numéricos en las partes.")
    todos_los_datos_validos = False
    # No necesitamos 'fecha_fabricacion_valida' ya que el string original es lo que usaremos si es válido