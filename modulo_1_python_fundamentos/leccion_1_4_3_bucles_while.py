print("--- Lección 1.4.3: Bucles while ---")

print("\n--- Ejemplo: Contador Simple co while ---")
contador = 0
limite_contador = 5
while contador < limite_contador:
    print(f"Contador actual: {contador}")
    contador += 1  # ¡MUY IMPORTANTE! Actualizar la variable de la condición
print(f"Bucle while finalizado. Contador final: {contador}")

# --- Ejemplo: Validación de Entrada del Usuario ---
print("\n--- Ejemplo: Validación de Entrada del Usuario (pH) ---")
ph_valido_ingresado = False
ph_muestra_usuario = 0.0    # Inicializar

while not ph_valido_ingresado:
    entrada_usuario_ph = input("Ingrese el pH de la muestra (entre 0.0 y 14.0): ")
    try:
        ph_temporal = float(entrada_usuario_ph)
        if 0.0 <= ph_temporal <= 14.0:
            ph_muestra_usuario = ph_temporal
            ph_valido_ingresado = True  # Condición para salir del bucle
            print(f"pH ingresado válido: {ph_muestra_usuario}")
        else:
            print("Error: El pH debe estar entre 0.0 y 14.0. Inténtalo de nuevo.")
    except ValueError:
        print(f"Error: {repr(entrada_usuario_ph)} no es un número válido. Inténtalo de nuevo")
# Aquí, ph_muestra_usuario contiene un valor válido o el último valor antes de un error si algo falló (aunque no debería por la lógica)

# --- Ejemplo: Simulación de Disolución de Fármaco ---
print("\n--- Ejemplo: Simulación de Disolución de Fármaco ---")
# Queremos simular hasta que al menos el 80% del fármaco se haya disuelto,
# o hasta un máximo de 60 minutos.
porcentaje_disuelto = 0.0
tiempo_transcurrido_min = 0
tasa_disolucion_por_minuto = 2.5    # % disuelto por minuto (simplificado)
limite_disolucion_objetivo_porc = 80.0
tiempo_maximo_estudio_min = 60

print(f"Inicio simulación: {porcentaje_disuelto:.1f} % disuelto a los {tiempo_transcurrido_min} min.")

while porcentaje_disuelto < limite_disolucion_objetivo_porc and tiempo_transcurrido_min < tiempo_maximo_estudio_min:
    # Simular paso de un minuto
    tiempo_transcurrido_min += 1
    disolucion_este_minuto = tasa_disolucion_por_minuto
    # En una simulación real, la tasa podría no ser constante
    porcentaje_disuelto += disolucion_este_minuto
    
    # Asegúrtante de que no exceda el 100% (aunque con esta tasa no pasará antes del objetivo)
    if porcentaje_disuelto > 100.0:
        porcentaje_disuelto = 100.0
        
    print(f"    A los {tiempo_transcurrido_min} min: {porcentaje_disuelto:.1f} % disuelto.")
    
    if porcentaje_disuelto >= limite_disolucion_objetivo_porc:
        print(f"OBJETIVO ALCANZADO: {porcentaje_disuelto:.1f} % disuelto.")
        break # Salimos del bucle porque se alcanzó el objetivo

    if tiempo_transcurrido_min >= tiempo_maximo_estudio_min:
        print(f"TIEMPO MÁXIMO ALCANZADO: {tiempo_maximo_estudio_min} min")
        break  # Salimos del bucle
    
# (La sentencia 'break' hace que no sea estrictamente necesario el 'and' en la condición del while)
# si se maneja la salida dentro del bucle, pero es bueno tener condiciones de guarda en el while)

if porcentaje_disuelto < limite_disolucion_objetivo_porc and tiempo_transcurrido_min >= tiempo_maximo_estudio_min:
    print(f"Resultado final: Solo se disolvió {porcentaje_disuelto:.1f} % en {tiempo_maximo_estudio_min} min.")

print("\n--- Bucles while en Procesos Farmacéuticos ---")
# 1. Ajuste de pH de una Solución:
#    Tienes una solución con `ph_actual_solucion = 5.5`.
#    Quieres ajustarla hasta que el pH esté entre 6.8 y 7.2 (inclusivo).
#    En cada paso de ajuste, simula que añades un reactivo que incrementa el pH en 0.2 unidades.
#    Imprime el pH en cada paso de ajuste.
#    Cuenta cuántos pasos de ajuste fueron necesarios.

print("\n1. Ajuste de pH de una solución:")
ph_actual_solucion_ej1 = 5.5
ph_objetivo_min_ej1 = 6.8
ph_objetivo_max_ej1 = 7.2
incremento_ph_paso_ej1 = 0.2
pasos_ajuste_ej1 = 0

print(f"    pH Inicial: {ph_actual_solucion_ej1:.1f}")
while not (ph_objetivo_min_ej1 <= ph_actual_solucion_ej1 <= ph_objetivo_max_ej1):
    if ph_actual_solucion_ej1 < ph_objetivo_min_ej1:    # Asumimos que solo necesitamos subir el pH.
        ph_actual_solucion_ej1 += incremento_ph_paso_ej1
        # Redondeamos para evitar problemas de precisión con floats
        ph_actual_solucion_ej1 = round(ph_actual_solucion_ej1, 2)
        pasos_ajuste_ej1 += 1
        print(f"    Ajuste {pasos_ajuste_ej1}: pH actual = {ph_actual_solucion_ej1:.2f}")
    else:   # Si es mayor que el max (o algo inesperado), podríamos romper o manejar.
        print(" El pH ya está por encima del objetivo o en un estado inesperado. Deteniendo ajuste.")
        break
    if pasos_ajuste_ej1 > 50:  # Salvaguarda contra bucles infinitos si la lógica es compleja
        print(f"    Demasiados pasos de ajuste, deteniendo.")
        break
if ph_objetivo_min_ej1 <= ph_actual_solucion_ej1 <= ph_objetivo_max_ej1:
    print(f"    Ajuste completado. pH final: {ph_actual_solucion_ej1:.2f} en {pasos_ajuste_ej1} pasos.")
else:
    print(f"    Ajuste detenido antes de alcanzar el objetivo. pH final: {ph_actual_solucion_ej1:.2f}.")
    
# 2. Consumo de Reactivo de un Lote:
#    Un lote de reactivo tiene `cantidad_reactivo_disponible_gramos = 100.0`.
#    Cada análisis consume `consumo_por_analisis_gramos = 7.5`.
#    Simula la realización de análisis hasta que la cantidad de reactivo disponible
#    sea insuficiente para el siguiente análisis.
#    Imprime cuántos análisis completos se pudieron realizar y cuántos gramos de reactivo sobraron.
print("\n2. Consumo de Reactivo de un Lote:")
cantidad_reactivo_disponible_gramos_ej2 = 100.0
consumo_por_analisis_gramos_ej2 = 7.5
analisis_realizados_ej2 = 0

print(f"    Cantidad inicial de reactivo: {cantidad_reactivo_disponible_gramos_ej2} g")
print(f"    Consumo por análisis: {consumo_por_analisis_gramos_ej2} g")

while cantidad_reactivo_disponible_gramos_ej2 >= consumo_por_analisis_gramos_ej2:
    cantidad_reactivo_disponible_gramos_ej2 -= consumo_por_analisis_gramos_ej2
    analisis_realizados_ej2 += 1
    # print(f"  Análisis {analisis_realizados_ej2} realizado. Restante: {cantidad_reactivo_disponible_gramos_ej2:.1f} g")
    
print(f"    Se puedieron realizar {analisis_realizados_ej2} análisis completados.")
print(f"    Cantidad de reactivo sobrante: {cantidad_reactivo_disponible_gramos_ej2:.2f} g")

# 3. Espera de Estabilización de Temperatura en un Baño Termostático:
#    Un baño debe alcanzar `temperatura_objetivo_C_ej3 = 37.0`.
#    Su `temperatura_actual_C_ej3` comienza en `25.0`.
#    En cada "minuto" (iteración), la temperatura aumenta `0.8` grados.
#    Simula el proceso hasta que la temperatura actual sea >= a la temperatura objetivo.
#    Imprime la temperatura en cada minuto y cuántos minutos tardó.
#    (Añade una salvaguarda: si tarda más de 30 minutos, detén la simulación e informa).

print(f"\n3. Estabilización de Temperatura de Baño:")
temperatura_objetivo_C_ej3 = 37.0
temperatura_actual_C_ej3 = 25.0
aumento_por_minuto_ej3 = 0.8
minutos_transcurridos_ej3 = 0
limite_minutos_simulacion_ej3 = 30

print(f"    Temp. Objetivo: {temperatura_objetivo_C_ej3}°C, Temp. Inicial: {temperatura_actual_C_ej3}°C")

while temperatura_actual_C_ej3 < temperatura_objetivo_C_ej3:
    if minutos_transcurridos_ej3 >= limite_minutos_simulacion_ej3:
        print(f"    SIMULACIÓN DETENIDA: Se alcanzó el límite de {limite_minutos_simulacion_ej3} minutos.")
        break
    
    temperatura_actual_C_ej3 += aumento_por_minuto_ej3
    temperatura_actual_C_ej3 = round(temperatura_actual_C_ej3, 2)  # Redondear
    minutos_transcurridos_ej3 += 1
    print(f"    Minuto {minutos_transcurridos_ej3}: Temperatura actual = {temperatura_actual_C_ej3} °C")
else:  # Este 'else' pertenece al 'while' y se ejecuta si el bucle terminó normalmente (no por un 'break')
    print(f"    Temperatura objetivo alcanzada en {minutos_transcurridos_ej3} minutos.")

if temperatura_actual_C_ej3 < temperatura_actual_C_ej3 and minutos_transcurridos_ej3 >= limite_minutos_simulacion_ej3:
    print(f"    La temperatura objetivo no se alcanzó en el tiempo límite. Temp. final: {temperatura_actual_C_ej3} °C")