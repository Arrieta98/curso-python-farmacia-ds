print("\n--- Lección 1.1.2: Tipos de Datos Numéricos y Booleanods ---")

# --- Enteros (int) ---
ensayos_clinicos_fase_3 = 12
print(f'Número de Ensayos Clínicos Fase III: {ensayos_clinicos_fase_3}')
print(f"Tipo de variable: {type(ensayos_clinicos_fase_3)}")

cantidad_comprimidos_lote = 100000
print(f'Cantidad de Comprimidos por Lote: {cantidad_comprimidos_lote}')
print(f"Tipo de variable: {type(cantidad_comprimidos_lote)}")

# --- Flotantes (float) ---
ph_solucion_tampon = 7.41
print(f'pH de la Solución Tampón: {ph_solucion_tampon}')
print(f'Tipo de variable: {type(ph_solucion_tampon)}')

concentracion_principio_activo_mg_ml = 2.55
print(f'Concentración de PA: {concentracion_principio_activo_mg_ml}')
print(f'Tipo de variable:{type(concentracion_principio_activo_mg_ml)}')

constante_velocidad_reaccion_k = 0.00015
print(f'Constante de Velocidad de Reacción: {constante_velocidad_reaccion_k}')
print(f'Tipo de variable: {type(constante_velocidad_reaccion_k)}')

temperatura_critica = -20.0  # Es un float
print(f'Temperatura Crítica: {temperatura_critica}')
print(f'Tipo de variable: {type(temperatura_critica)}')

# --- Booleanos (bool) ---
lote_aprobado_para_liberación = True
print(f'¿Lote Aprobado para Liberación?: {lote_aprobado_para_liberación}')
print(f'Tipo de variable: {type(lote_aprobado_para_liberación)}')

requiere_analisis_adicional = False
print(f'¿Requiere Análisis Adicional?: {requiere_analisis_adicional}')
print(f'Tipo de variable: {type(requiere_analisis_adicional)}')

# Los booleanos son el resultado de comparaciones
pureza_actual = 99.5
pureza_minima_requerida = 98.0
suficientemente_puro = pureza_actual >= pureza_minima_requerida
print(f'Pureza actual: {pureza_actual}%')
print(f'Mínima requerida: {pureza_minima_requerida}%')
print(f'¿Suficientemente puro?: {suficientemente_puro}')
print(f'Tipo de variable: {type(suficientemente_puro)}')

print("\n--- Identificando y Creando ---")

# Para cada uno de los siguientes datos farmacéuticos,
# decide qué tipo de dato (int, float o bool) sería más apropiado
# y crea una variable para almacenarlo. Luego imprime la variable y su tipo.

# 1. Número de pacientes reclutados para un ensayo: 257
numero_pacientes_reclutados = 257
print(f'Número de Pacientes Reclutados: {numero_pacientes_reclutados}')
print(f'Tipo de variable: {type(numero_pacientes_reclutados)}')

# 2. El p-valor obtenido de una prueba estadística: 0.045
p_valor_prueba = 0.045
print(f'P-valor obtenido: {p_valor_prueba}, Tipo: {type(p_valor_prueba)}')

# 3. Indicación si un efecto adverso es considerado "serio":
# Sí (representar como boolenano)
efecto_adverso_serio = True
print(f'¿Efecto Adverso Serio?: {efecto_adverso_serio}')
print(f'Tipo de variable: {type(efecto_adverso_serio)}')

# 4. Dosis administrada de un fármaco inyectable en mL: 1.5
dosis_administrada_ml = 1.5
print(f'Dosis Administrada: {dosis_administrada_ml} mL')
print(f'Tipo de variable: {type(dosis_administrada_ml)}')

# 5. Número de desviaciones de calidad reportadas en el mes: 3
numero_desviaciones_calidad = 3
print(f'Número de Desviaciones de Calidad: {numero_desviaciones_calidad}')
print(f'Tipo de variable: {type(numero_desviaciones_calidad)}')

# 6. Si un protocolo de análisis ha sido validado:
# No (representar como booleano)
protocolo_validado = False
print(f'¿Protocolo Validado?: {protocolo_validado}')
print(f'Tipo de variable: {type(protocolo_validado)}')

# 7. La masa molar de la Lidocaína HCl: 270.798 g/mol
masa_molar_lidocaina = 270.798
print(f'Masa Molar de la Lidocaína HCl: {masa_molar_lidocaina} g/mol')
print(f'Tipo de variable: {type(masa_molar_lidocaina)}')

# 8. Vida media de un fármaco en horas: 4.75
vida_media_farmaco = 4.75
print(f'Vida Media del Fármaco: {vida_media_farmaco} horas')
print(f'Tipo de variable: {type(vida_media_farmaco)}')

# 9. Número de lotes inspeccionados
numeros_lotes_inspeccionados = 102305
print(f'Número de Lotes Inspeccionados: {numeros_lotes_inspeccionados}')
print(f'Tipo de variable: {type(numeros_lotes_inspeccionados)}')

# 10. Si cumple con la normativa de calidad:
# Sí (representar como booleano)
cumple_normativa_gmp = True
print(f'¿Cumple Normativa GMP?: {cumple_normativa_gmp}')
print(f'Tipo de variable: {type(cumple_normativa_gmp)}')

numero_grande = 12345678901234567890
print(f'Número Grande: {numero_grande}')
print(f'Tipo de variable: {type(numero_grande)}')

resultado = 10 + 5.5
print(f'Resultado: {resultado}')
print(f'Tipo de variable: {type(resultado)}')
