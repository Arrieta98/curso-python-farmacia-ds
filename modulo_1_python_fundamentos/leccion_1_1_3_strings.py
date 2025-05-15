print("\n--- Lección 1.1.3: Cadenas de Texto (strings) - Parte 1 ---")

# --- Creación de Strings ---
nombre_principio_activo = "Sildenafil Citrato"
forma_comercial = 'Viagra'  # Usando comillas simples
protocolo_estudio = """PROTOCOLO DE INVESTIGACIÓN FARMACOLÓGICA: EF-2025
Título: Evaluación de la eficacia y seguridad del compuesto X en
pacientes con Y.
Versión: 3.1
Fecha: 2025-05-14"""  # String multilínea con comillas triples

print(f'Principio Activo: {nombre_principio_activo}')
print(f'Forma Comercial: {forma_comercial}')
# Imprime los primeros 80 caracteres del protocolo
print(f'Extracto del Protocolo:\n {protocolo_estudio[:80]}...')

# --- Concatenación de Strings (+) ---
nombre_completo_farmaco = nombre_principio_activo + " ("+forma_comercial+")"
print(f'Nombre Completo del Fármaco: {nombre_completo_farmaco}')

unidad_dosis = "mg"
dosis_str = "50"  # Dosis como string
descripcion_dosis = dosis_str + " " + unidad_dosis
print(f'Dosis: {descripcion_dosis}')

# --- Repetición de Strings (*) ---
linea_separadora = "-" * 20
print(linea_separadora)
mensaje_alerta = "ALERTA! " * 3
print(mensaje_alerta)

# --- Longitud de un string (len) ---
nombre_laboratorio = "PharmaNova Investigaciones S.A.S."
longitud_nombre_lab = len(nombre_laboratorio)
print(f"\n'{nombre_laboratorio}' tiene {longitud_nombre_lab} caracteres.")

# --- Indexación de Strings ---
# Recortar: el primer carácter están en el índice 0
codigo_lote_ejemplo = "LOTE2024X001B"
# L  O  T  E  2  0  2  4  X  0  0  1  B
# 0  1  2  3  4  5  6  7  8  9 10 11 12 (índices positivos)
#                                    -1 (índice negativo)
print(f'\nCódigo de Lote: {codigo_lote_ejemplo}')
primer_caracter = codigo_lote_ejemplo[0]
segundo_caracter = codigo_lote_ejemplo[1]
tercer_caracter = codigo_lote_ejemplo[2]
cuarto_caracter = codigo_lote_ejemplo[3]
quinto_caracter = codigo_lote_ejemplo[4]
ultimo_caracter = codigo_lote_ejemplo[-1]
penultimo_caracter = codigo_lote_ejemplo[-2]

print(f'Primer Carácter: {primer_caracter}')
print(f'Segundo Carácter: {segundo_caracter}')
print(f'Tercer Carácter: {tercer_caracter}')
print(f'Cuarto Carácter: {cuarto_caracter}')
print(f'Quinto Carácter: {quinto_caracter}')
print(f'Último Carácter: {ultimo_caracter}')
print(f'Penúltimo Carácter: {penultimo_caracter}')

# Si intentas acceder a un índice fuera de rango, obtendrás un IndexError
# caracter_invalido = codigo_lote_ejemplo[20]  # Esto daría error

# --- Slicing (Rebanado) string[inicio:fin:paso] ---
# 'fin' es exlusivo
print(f"\nSlicing en '{codigo_lote_ejemplo}':")

# Obtener la parte "Lote"
parte_lote = codigo_lote_ejemplo[:4]
print(f'Parte "Lote": {parte_lote}')

# Obtener el año "2024" (índices 4, 5, 6, 7)
parte_anio = codigo_lote_ejemplo[4:8]
print(f'Parte "Año": {parte_anio}')

# Obtener el identificador "X001" (índices 8, 9, 10, 11, 12)
parte_identificador = codigo_lote_ejemplo[8:13]
print(f'Parte "Identificador": {parte_identificador}')

# Desde el carácter en índice 8 hasta el final
desde_indice_8 = codigo_lote_ejemplo[8:]
print(f'Desde el índice 8: {desde_indice_8}')

# Cada segundo carácter del código completo
cada_segundo_char = codigo_lote_ejemplo[::2]
print(f'Cada segundo carácter: {cada_segundo_char}')

# Invertir el string con slicing
código_invertido = codigo_lote_ejemplo[::-1]
print(f'Código Invertido: {código_invertido}')

# --- Manipulación de Strings Farmacéuticos ---
print("\n--- Strings Farmacéuticos ---")

# 1. Tienes los siguientes datos para un medicamento:
nombre_base = "Metformina"
forma = "Comprimidos de Liberación Prolongada"
dosis_valor = 850
unidad = "mg"

nombre_completo_medicamento = f'{nombre_base} en ' + forma
print(f'Nombre Completo del Medicamento: {nombre_completo_medicamento}')

descripcion_dosis_medicamento = str(dosis_valor) + " " + unidad
print(f'{nombre_base} de {descripcion_dosis_medicamento}')

tag = f'{nombre_completo_medicamento} de {descripcion_dosis_medicamento}'
print(f'Etiqueta Completa: {tag}')

codigo_muestra = "SANGRE-PACIENTE007-VISITA03-HORA=10:30"
print(f'\nCódigo de Muestra Original: {codigo_muestra}')

# Extraer parte del código de muestra (SANGRE)
parte_sangre = codigo_muestra[:6]
print(f'Parte "SANGRE": {parte_sangre}')

# Extraer parte del código de muestra (PACIENTE007)
parte_paciente = codigo_muestra[7:18]
print(f'Parte "PACIENTE007": {parte_paciente}')

# Extraer parte del código de muestra (VISITA03)
parte_visita = codigo_muestra[19:27]
print(f'Parte "VISITA03": {parte_visita}')

# Extraer parte del código de muestra (HORA=10:30)
parte_hora = codigo_muestra[28:]
print(f'Parte "HORA": {parte_hora}')

id_lote = "COL-BOG-2025-00345"
print(f'\nID de Lote: {id_lote}')
codigo_pais = id_lote[:3]
print(f'Código de País: {codigo_pais}')
codigo_ciudad = id_lote[4:7]
print(f'Código de Ciudad: {codigo_ciudad}')
codigo_anio = id_lote[8:12]
print(f'Código de Año: {codigo_anio}')
codigo_lote = id_lote[13:]
print(f'Código de Lote: {codigo_lote}')
codigo_invertido = id_lote[::-1]
print(f'ID de Lote Invertido: {codigo_invertido}')
