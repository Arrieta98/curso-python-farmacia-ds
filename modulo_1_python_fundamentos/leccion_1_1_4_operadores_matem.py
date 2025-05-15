print("\n --- Lección 1.1.4: Operadores Matemáticos ---\n")

# --- Suma (+) y Resta (-) ---
cant_inicial_reactivo = 50.75  # gramos
cant_usada_reactivo = 12.5  # gramos
cant_restante_reactivo = cant_inicial_reactivo - cant_usada_reactivo
print(f'Cantidad Restante de Reactivo: {cant_restante_reactivo} g')
print(f'Cantidad Usada de Reactivo: {cant_usada_reactivo} g')
print(f'Cantidad restante de Reactivo: {cant_restante_reactivo} g')

peso_paciente_1_kg = 75.2  # Kg
peso_paciente_2_kg = 68.9  # Kg
peso_total_pacientes_kg = peso_paciente_1_kg + peso_paciente_2_kg
print(f'Peso Total de Pacientes: {peso_total_pacientes_kg} Kg')

# --- Multiplicación (*)
dosis_por_comprimido_mg = 20.0  # mg
numero_comprimidos_por_dia = 3
dosis_diaria_total_mg = dosis_por_comprimido_mg * numero_comprimidos_por_dia
print(f'\nDosis Diaria Total: {dosis_diaria_total_mg} mg')

# --- División (/)
# Recuerda: siempre devuelve un float
cantidad_total_principio_activo = 500000  # mg
numero_unidades_a_producir = 10000  # unidades (ej. comprimidos)
mg_por_unidad = cantidad_total_principio_activo / numero_unidades_a_producir
print(f'\nMiligramos de PA por unidad: {mg_por_unidad} mg')

# --- División Entera (//) ---
tabletas_disponibles = 100
dosis_diarias_tabletas = 3  # El paciente toma 3 tabletas al día
dias_tratamientos = tabletas_disponibles // dosis_diarias_tabletas
print(f'\nCon {tabletas_disponibles} tabletas')
print(f'y tomando {dosis_diarias_tabletas} tabletas al día')
print(f'El paciente puede completar {dias_tratamientos} días de tratamiento.')

# --- Módulo (%) ---
tabletas_sobrantes = tabletas_disponibles % dosis_diarias_tabletas
print(f'\nDespués de {dias_tratamientos} días de tratamiento')
print(f'El paciente tendrá {tabletas_sobrantes} tableta sobrante.')

# Ejemplo de módulo: ¿Es un número de lote par o impar?
numero_lote = 2025007
if numero_lote % 2 == 0:
    print(f'El lote {numero_lote} es PAR.')
else:
    print(f'El lote {numero_lote} es impar.')

# ---Exponencianción (**) ---
# Calcular el volumen de una esfera (V = 4/3 * pi * r^3)
radio_nanoparticula_nm = 50.0
pi_aprox = 3.14159
volumen_nanoparticula_nm3 = (4/3) * pi_aprox * (radio_nanoparticula_nm ** 3)
print(f'\nVolumen de una nanopartícula {volumen_nanoparticula_nm3}')
print(f'\nnm: {volumen_nanoparticula_nm3:.2e} nm^3')

# Raíz cuadraa (elevar a la potencia 0.5)
area_superficial_cm2 = 25.0
lado_cuadrado_cm = area_superficial_cm2 ** 0.5
print(f'Si el área de un cuadrado es {area_superficial_cm2} cm²')
print(f'su lado es: {lado_cuadrado_cm} cm')

# --- Orden de Operaciones y Uso de Paréntesis ---
# Ejemplo: Calcular la dosis ajustada por superficie corporal
# Fórmula de Mosteller para BSA (m^2) = sqrt((altura_cm * peso_kg) / 3600)
# Dosis = Dosis_estandar_por_m2 * BSA

altura_paciente_cm = 170
peso_paciente_kilos = 70
dosis_estandar_por_m2 = 300  # mg/m^2

producto_altura_peso = altura_paciente_cm * peso_paciente_kilos
bsa_calculada = (producto_altura_peso / 3600) ** 0.5
print(f"\nBSA calculada (Monsteller) para {altura_paciente_cm} cm")
print(f"y {peso_paciente_kilos} kg: {bsa_calculada:.2f} m²")

dosis_ajustada_bsa_mg = dosis_estandar_por_m2 * bsa_calculada
print(f"Dosis ajustada por BSA: {dosis_ajustada_bsa_mg:.2f} mg")

print("\n--- Cálculos Farmacéuticos ---")

# 1. Cálculo de Concentración (Porcentaje Peso/Volumen % p/v)
#   Una solución contiene 20 gramos de soluto en 250 mL de solución.
#   Calcula la [] en % p/v. (%p/v = (gramos de soluto / mL de solución) * 100)
gramos_soluto_1 = 20.0
ml_solucion_1 = 250.

concentracion_p_v = (gramos_soluto_1 / ml_solucion_1) * 100
print(f'1. Concentración %p/v: {concentracion_p_v:.2f} %p/v')

# 2. Calculo de Dilución (Factor de Dilución)
#   Se toman 2 mL de una solución madre y se llvan a un volumen final de 100 mL
#   Calcula el factor de dilución. (Factor = Volumen Final / Volumen Inicial)
volumen_inicial_dil_2 = 2.0
volumen_final_dil_2 = 100.0
factor_dilucion_2 = volumen_final_dil_2 / volumen_inicial_dil_2
print(f"2. Factor de Dilución: {factor_dilucion_2}")

# 3. Dosis por Peso Corporal
#   Un fármaco se administra a 15 mg/Kg. El paciente pesa 67 Kg.
#   Calcula la dosis total para el paciente.
dosis_mg_por_kg = 15.0
peso_paciente_kg_3 = 67.0
dosis_total_paciente_3 = dosis_mg_por_kg * peso_paciente_kg_3
print(f"3. Dosis Total para el paciente: {dosis_mg_por_kg} mg")

# 4. Unidades de Fármaco Restantes despúes de un Tratamiento
#   Un vase contien 28 comprimidos. El paciente toma 2 comprimidos al día
# durante 10 días.
#   ¿Cuántos comprimidos sobrarán? (Usa // y %)
compri_envase_4 = 28
compri_por_dia_4 = 2
dias_trat_4 = 10

comprimidos_tomados_4 = compri_envase_4 * dias_trat_4
comprimidos_sobrantes_4 = compri_envase_4 - comprimidos_tomados_4
compri_sobrantes_trat = compri_envase_4 % (compri_por_dia_4 * dias_trat_4)
print(f"4. Comprimidos tomados: {comprimidos_tomados_4}")
print(f"   Comprimidos sobrantes: {compri_sobrantes_trat}")

# 5. Preparación de una solución por Porcentaje Peso/Peso
#   Se prepará 500 g de una pomada al 2.5 % p/p de un principio activo.
#   ¿Cuántos gramos de principio activo necesitas?
#   ¿Cuántos gramos de excipiente (base de la pomada) necesitas?
#   (%p/p = (gramos de PA / gramos totales de pomada) * 100)
#   Por lo tanto: gramos de PA = (%p/p / 100) * gramos totales de pomada
#   Define variables: "gramos_totales_pomadas_5", "porcentaje_activo_pp_5"
#   Calcula: "gramos_principio_activo_5", "gramos_excipientes_5"
gr_tot_pomada_5 = 500.0
por_activo_pp_5 = 2.5
gramos_principio_activo_5 = (por_activo_pp_5 / 100) * gr_tot_pomada_5
gramos_exp_5 = gr_tot_pomada_5 - gramos_principio_activo_5
print(f"\n5. Preparar {gr_tot_pomada_5} g de pomada al {por_activo_pp_5} %p/p")
print(f"Gramos de Principio Activo necesario: {gramos_principio_activo_5} gr")
print(f"Gramos de Excipientes necesarios: {gramos_exp_5} g")
