# Lección 1.1.1: Variables y Asignación
# Práctica farmacéutica

print("--- Información de un Fármaco Hipotético ---")

# 1. Nombre del Fármaco (Tipo: string - cadena de texto)
#   - Convención: snake_case
#   - Relevancia: Identificador principal del medicamento.
nombre_farmaco = "Amoxicilina"
# Usamos print() para ver el resultado
print("Nombre del fármaco:", nombre_farmaco)

# 2. Dosis Estándar por Unidad (Tipo: integer - entero)
#   - Relevancia: Cantidad de principio activo en cada comprimido/cápsula.
dosis_estandar_mg = 500
print("Dosis Estándar (ng):", dosis_estandar_mg)

# 3. Forma Farmacéutica (Tipo: string)
#   - Relevancia: Describe la presentación del medicamento.
forma_farmaceutica = "Cápsula"
print("Forma Farmacéutica:", forma_farmaceutica)

# 4. ¿Requiere Receta? (Tipo: boolean - booleano, True o False)
#   - Relevancia: Condición de dispensación.
requiere_receta = True
print("¿Requiere Receta?:", requiere_receta)

# 5. Temperatura de Almacenamiento Recomendada (Tipo: float - número decimal)
#   - Relevancia: Condición crítica para la estabilidad del producto.
#   - Usamos float porque la temperatura puede tener decimales
temp_almacenamiento_celcius = 22.5
print("Temperatura de Almacenamiento (°C):", temp_almacenamiento_celcius)

# 6. Código de Lote (Tipo: string, puede contener letras y números)
#   - Relevancia: Trazabilidad del producto.
codigo_lote_actual = "AMX-2025-05-B001"
print("Código de Lote Actual:", codigo_lote_actual)

print("\n--- Reasignación y Nuevas Variables ---")

# 7. Reasignar la dosis (quizás estamos considerando otra presentación)
print("Dosis Estándar ANTES de reasignar:", dosis_estandar_mg)
dosis_estandar_mg = 875
print("Dosis Estándar DESPUÉS de reasignar:", dosis_estandar_mg)

# 8. Número de Unidades en el Envase(Tipo: integer)
unidades_por_envase = 20
print("Unidades por Envase:", unidades_por_envase)

# 9. Fabricante (Tipo: string)
fabricante = "PharmaGlobal Inc."
print("Fabricante:", fabricante)

# 10. Variable para almacenar el año de caducidad (Tipo: integer)
anio_caducidad = 2027
print("Año de Caducidad:", anio_caducidad)

print("\n--- Variables Adicionales ---")

id_paciente_simulado = "PAC00765"
peso_paciente_kg = 75.5
altura_paciente_metros = 1.78
paciente_en_tratamiento = True
dias_tratamiento = 30

print("ID PAciente Simulado:", id_paciente_simulado)
print("Peso Paciente (kg):", peso_paciente_kg)
print("Altura Paciente (m):", altura_paciente_metros)
print("¿Paciente en Tratamiento?:", paciente_en_tratamiento)
print("Días de Tratamiento:", dias_tratamiento)
