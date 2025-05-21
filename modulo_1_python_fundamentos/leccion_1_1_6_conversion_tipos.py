print("--- Lección 1.1.6: Conversión de tipos ---")

# ---Convertir a Entero (int) ---
print("\n--- Conversión a int ---")
valor_float_para_int = 99.999
entero_desde_float = int(valor_float_para_int)
print(f"float {valor_float_para_int} convertido a int: {entero_desde_float}")
print(f"Tipo: {type(entero_desde_float)}")

string_numero_entero = "12345"
entero_desde_string = int(string_numero_entero)
print(f"String '{string_numero_entero}' convertido a {entero_desde_string}")
print(f"Tipo: {type(entero_desde_string)}")

print(f"Booleano True a int: {int(True)}")
print(f"Booleano False a int {int(False)}")

# --- Convertir a Flotante (float) ---
print("\n--- Conversión a float ---")
valor_int_para_float = 77
flotante_desde_int = float(valor_int_para_float)
print(f"int {valor_int_para_float} convertido a {flotante_desde_int}")
print(type(flotante_desde_int))

string_numero_flotante = "25.75"
flotante_desde_string = float(string_numero_flotante)
print(f"String '{string_numero_flotante}'")
print(f"convertido a float: {flotante_desde_string}")

print(f'Booleano True a float: {float(True)}')
print(f"Booleano False a float: {float(False)}")

# --- Convertir a String (str) ---
numero_lote_int = 2025001
string_lote = str(numero_lote_int)
print(f"Entero {numero_lote_int}")
print(f"Convertido a string: '{string_lote}'")
print(f"Tipo: {type(string_lote)}")
# Ahora podemos concatenarlo con otros strings
prefijo_lote = "LOTE-"
codigo_completo_lote = prefijo_lote + string_lote
print(f"Código de lote completo: {codigo_completo_lote}")

ph_valor_float = 7.35
string_ph = str(ph_valor_float)
print(f"Float {ph_valor_float} convertido a string: '{string_ph}'")
print(f"Tipo: {type(string_ph)}")

booleano_valido = True
string_booleano = str(booleano_valido)
print(f"Booleano {booleano_valido} convertido a string: '{string_booleano}'")
print(f"Tipo: {type(string_booleano)}")

# --- Convertir a Booleano (bool) ---
print("\n--- Conversión a bool ---")
# Truthy values (se convierten a True)
print(f"bool(10): {bool(10)}")                  # int diferente de 0
print(f"bool(-5.5): {bool(-5.5)}")              # float diferente de 0.0
print(f"bool('Hola'): {bool('Hola')}")          # string no vacío
print(f"bool('[1, 2]'): {bool([1, 2])}")        # Lista no vacía
print(f"bool({{'a': 1}}): {bool({'a': 1})}")   # diccionario no vacío

# Falsy values (se convierten a False)
print(f"bool(0): {bool(0)}")
print(f"bool(0.0); {bool(0.0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(()): {bool(())}")
print(f"bool({{}}): {bool({})}")
print(f"bool(None): {bool(None)}")

print("\n--- Manejo de Errores en Conversiones (try-except)---")
# Ejemplo: Obtener la edad de un paciente (que viene como input,
# o sea, string)
input_edad_paciente_str_valido = "45"
input_edad_paciente_str_invalido = "cuarenta"
input_edad_paciente_str_decimal = "45.5"


def procesar_edad(edad_str):
    try:
        edad_int = int(edad_str)
        print(f"Edad procesada (int): {edad_int} años")
        print(f"Tipo: {type(edad_int)}")
    except ValueError:
        print(f"Error: '{edad_str}' no es una edad entera válida")
        print("No se pudo convertir.")
        print(f"Tipo: {type(edad_str)}")
    except TypeError:  # Si edad_str fuera, por ejemplo, None
        print("Error de Tipo: Se esperaba un string para la edad")
        print(f"pero se recibió {type(edad_str).__name__}")


print("Intentando procesar edades:")
procesar_edad(input_edad_paciente_str_valido)
procesar_edad(input_edad_paciente_str_invalido)
procesar_edad(input_edad_paciente_str_decimal)
procesar_edad(None)

# Si quisiéramos aceptar "45.5" y truncarlo, lo haríamos float() primero:


def procesar_edad_con_float_primero(edad_str):
    try:
        edad_float = float(edad_str)    # Primero a float
        edad_int = int(edad_float)      # Liuego a int (trunca)
        print(f"Edad(desde string '{edad_str}')")
        print(f"procesada como float ({edad_float})")
        print(f"y luego como int ({edad_int}).")
    except ValueError:
        print(f"Error: '{edad_str}' no es un número válido.")
        print(f"Tipo: {type(edad_str)}")
    except TypeError:
        print("Error de Tipo: Se espera un string para la edad")
        print(f"pero se recibió {type(edad_str).__name__}")


print("\nIntentando procesar edad con float primero")
procesar_edad_con_float_primero(input_edad_paciente_str_decimal)
procesar_edad_con_float_primero("60")

print("\n--- Conversiones Farmacéuticas ---")

# 1. Input de Usuario para Dosis:
#   El usuario ingresa una dosis como texto.
#   Se convertirá a floar para usarla en cálculos
#   Manejo el caso en que el usuario ingrese un texto no numérico.
dosis_ingresado_str = input("Ingrese la dosis en mg (ej. 12.5): ")
dosis_calculo_mg = None  # Inicializa en caso error

try:
    dosis_calculo_mg = float(dosis_ingresado_str)
    print(f"Dosis para cálculo: {dosis_ingresado_str} mg")
    print(f"Cálculo: {dosis_calculo_mg * 2}")
except ValueError:
    print(f"Error '{dosis_ingresado_str}' no es una dosis numérica váida.")

# 2. Generar un ID de Lote Compuesto:
#   Tienes un prefijo de lote (string), un año (int), y un número
#   secuencial (int).
#   Crea un ID de lote completo como string, ej. "PFX-2025-00123".

prefijo_lote_ej2 = "FARMA"
anio_lote_ej2 = 2025
secuencial_lote_ej2 = 77
id_lote_completo_ej2 = prefijo_lote_ej2 + "-" + \
    str(anio_lote_ej2) + "-" + str(secuencial_lote_ej2)
print(f"\nId de Lote Compuesto: {id_lote_completo_ej2}")
print(f"{secuencial_lote_ej2:07d}")

# 3. Verificar si un "Código de Actividad" (que podría ser un número o
# un string vacío) indica actividad.
#    Un código numérico (distinto de 0) o un string no vacío
#    se considera activo.
#    Un string vacío, 0, o None se considera inactivo.
codigo_actividad_prueba = [101, "ACTIVO_XYZ", 0, 0.0, "", None, True, False]
print("\nEvaluando de Códigos de Actividad:")
for codigo in codigo_actividad_prueba:
    es_activo = bool(codigo)
    print(
        f"Código: {repr(codigo):<12} "
        f"(Tipo: {type(codigo).__name__:<8}) -> ¿Activo?: {es_activo}"
    )
    # repr(codigo) muestra el string con comillas, lo que ayuda a distinguir ""
    # de None. :<12 y :<8 son para alinear la salida en columnas

# 4. (Ejercicio para ti) De String a Número para Cálculo de Rendimiento:
#    Obtienes el "peso_teorico_producto_g" y "peso_obtenido_producto_g"
#    como strings desde un formulario o archivo.
#    Debes convertirlos a float, calcular el rendimiento porcentual,
#    y luego convertir el rendimiento a un string para un reporte,
#    formateado a 2 decimales con el símbolo "%".
#    Rendimiento % = (peso_obtenido / peso_teorico) * 100
#    Maneja posibles errores si los strings no son números válidos.

peso_teorico_str_ej4 = "150.75"
peso_obtenido_str_ej4 = "145.5"

print("\nCálculo de Rendimiento Porcentual:")
rendimiento_reporte_str_ej4 = "Error en cálculo"  # Valor por defecto
try:
    peso_teorico_g_ej4 = float(peso_teorico_str_ej4)
    peso_obtenido_g_ej4 = float(peso_obtenido_str_ej4)

    if peso_teorico_g_ej4 == 0:
        print("Error: El peso teórico no puede ser cero.")
    else:
        rendimiento_porcentual_ej4 = (
            peso_obtenido_g_ej4 / peso_teorico_g_ej4
        ) * 100
        rendimiento_reporte_str_ej4 = f"{rendimiento_porcentual_ej4:.2f} % "
        print(
            f"Peso Teórico: {peso_teorico_g_ej4} g, "
            f"Peso Obtenido: {peso_obtenido_g_ej4} g"
        )

except ValueError:
    print(
        f"Error: Uno o ambos pesos ('{peso_teorico_str_ej4}', "
        f"'{peso_obtenido_str_ej4}') "
        "no son numéricos válidos"
    )
except Exception as e:  # Otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")

print(f"Rendimiento para reporte: {rendimiento_reporte_str_ej4}")
