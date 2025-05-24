# Lección 1.5.1: Definición y Llamada de Funciones
print("--- Lección 1.5.1: Definición y Llamada de Funciones ---")

# --- Ejemplo 1: Una función simple sin entrada ni salida (solo acción):
def mostrar_mensaje_bienvenida_laboratorio():
    """Esta función imprime un mensaje de bienvenida estándar del laboratorio."""
    print("**********************************************")
    print("* Bienvenid@ al Sistema de Gestión de Calidad *")
    print("* Laboratorios PharmaData Solutions      *")
    print("**********************************************")
    # Este es un docstring (cadena de documentación), lo veremos mejor después.

# Llamada (o invocación) de la función
print("Llamando a la función por primera vez:")
mostrar_mensaje_bienvenida_laboratorio()

print("\nLlamado a la función de nuevo en otro punto del programa:")
mostrar_mensaje_bienvenida_laboratorio()

# --- Ejemplo 2: Otra función simple para una tarea específica ---
print("\n--- Ejemplo 2: Función para Imprimir Encabezado de Reporte ---")

def imprimir_encabezado_reporte_simple():
    """Imprime un encabezado genérico para un reporte de análisis."""
    print("\n=============================================")
    print("       REPORTE DE ANÁLISIS FARMACÉUTICO")
    print("=============================================")
    # (Aquí podrían ir más detalles como nombre del laboratorio, fecha, etc.)
    
# Usar la función
imprimir_encabezado_reporte_simple()
print("Contenido del reporte iría aquí...")
print("... más contenido ...")
imprimir_encabezado_reporte_simple() # Quizás para un segundo reporte o sección
print("Otro contenido de reporte...")

# 1. Función `mostrar_instrucciones_almacenamiento_estandar()`:
#    Define una función que imprima las siguientes instrucciones de almacenamiento:
#    "Almacenar en un lugar fresco y seco."
#    "Proteger de la luz directa."
#    "Mantener fuera del alcance de los niños."
#    Luego, llama a esta función dos veces.

def mostrar_instrucciones_almacenamiento_estandar():
    """Imprime las instrucciones estándar de alamacenamiento."""
    print("\nInstrucciones de Almacenamiento Estándar:")
    print("- Almazenar en un lugar fresco y seco.")
    print("- Proteger de la luz directa.")
    print("- Mantener fuera del alcance de los niños.")

print("Llamada 1 a instrucciones de almacenamiento:")
mostrar_instrucciones_almacenamiento_estandar()
print("Llamada 2 a instrucciones de almacenamiento:")
mostrar_instrucciones_almacenamiento_estandar()

# 2. Función `imprimir_separador_seccion()`:
#    Define una función que imprima una línea separadora hecha de 40 guiones (`-`).
#    Llama a esta función varias veces entre diferentes "secciones" de print statements
#    para ver cómo ayuda a organizar la salida.

def imprimir_separador_seccion():
    """Imprime una línea separadora de 40 guiones."""
    print("-" * 40)

print("\nInicio de una nnueva sección de análisis.")
imprimir_separador_seccion()
print("Datos de lote A...")
imprimir_separador_seccion()
print("Resultados del Lote A...")
imprimir_separador_seccion()
print("Conclusiones del Lote A.")

# 3. Función `mostrar_advertencia_manipulacion_api()`:
#    API significa "Active Pharmaceutical Ingredient" (Principio Activo Farmacéutico).
#    Define una función que imprima una advertencia estándar para la manipulación de APIs:
#    "ADVERTENCIA: Manipular este API con equipo de protección personal adecuado."
#    "Consultar la Hoja de Datos de Seguridad del Material (MSDS) antes de usar."
#    "Evitar inhalación y contacto con la piel."
#    a) Define la función.
#    b) Llama a la función.
#    c) (Opcional) Imagina que esta advertencia es para un API muy potente, crea otra función
#       `mostrar_advertencia_api_potente()` que imprima la advertencia anterior Y ADEMÁS
#       una línea extra como "RIESGO ALTO: Utilizar cabina de extracción y doble guante."
#       Llama a esta nueva función.
print("\n3. Advertencias de Manipulación de API:")
def mostrar_advertencia_manipulacion_api():
    """Imprime una advertencia estándar para la manipulación de APIs."""
    print("\nADVERTENCIA: Manipular este API con equipo de protección personal adecuado.")
    print("Consultar la Hoja de Datos de Seguridad del Material (MSDS) antes de usar.")
    print("Evitar inhalación y contacto con la piel.")
# b)
print("Llamando a la advertencia estándar:")
mostrar_advertencia_manipulacion_api()

# c)
def mostrar_advertencia_api_potente():
    """Imprime una advertencia para APIs potentes, incluyendo la estándar."""
    mostrar_advertencia_manipulacion_api() # Reutilizamos la función anterior
    print("RIESGO ALTO: Utilizar cabina de extracción y doble guante.")

print("\nLlamando a la advertencia para API potente:")
mostrar_advertencia_api_potente()