import csv
import os
import json
from datetime import datetime
from collections import defaultdict, Counter

# Leo el archivo csv con los datos
with open('actividad_2.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Saco el dia de la semana de cada registro
for row in data:
    dt = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M')
    row['dia_semana'] = dt.strftime('%A')

# Veo que dia tuvo mas sesiones
dias_contador = Counter(row['dia_semana'] for row in data)
max_sesiones = max(dias_contador.values())
dias_mas_activos = [dia for dia,
                    count in dias_contador.items() if count == max_sesiones]

# Calculo cuantos dias pasaron entre el primer y ultimo entrenamiento
fechas = [datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M')
          for row in data]
dias_diferencia = (max(fechas) - min(fechas)).days

# Veo cual campeon entreno mas veces
campeones_contador = Counter(row['campeon'] for row in data)
campeon_top = campeones_contador.most_common(1)[0]

# Calculo promedio de entrenamientos por dia de semana
promedio_por_dia = {
    dia: count / len(set(f.strftime('%Y-%m-%d') for f in fechas))
    for dia, count in dias_contador.items()
}

# Me fijo cual campeon entrena mas los fines de semana
fines_de_semana = ['Saturday', 'Sunday']
data_finde = [row for row in data if row['dia_semana'] in fines_de_semana]
campeon_finde = Counter(row['campeon'] for row in data_finde).most_common(1)[0]

# Creo carpeta "salida" y guardo un csv con la cantidad de entrenamientos por campeon
os.makedirs('salida', exist_ok=True)
with open('salida/campeones_entrenamientos.csv', 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['campeon', 'cantidad'])
    for campeon, cantidad in campeones_contador.items():
        writer.writerow([campeon, cantidad])

# Armo un json con el resumen por dia
resumen_dias = defaultdict(lambda: defaultdict(int))
for row in data:
    fecha = datetime.strptime(
        row['timestamp'], '%Y-%m-%d %H:%M').strftime('%Y-%m-%d')
    resumen_dias[fecha][row['campeon']] += 1

json_data = {
    'total_registros': len(data),
    'resumen_por_dia': resumen_dias
}

with open('salida/resumen_dias.json', 'w', encoding='utf-8') as f_json:
    json.dump(json_data, f_json, indent=2, ensure_ascii=False)

# Muestro los resultados mas importantes
print(f"Dia(s) con mas sesiones: {dias_mas_activos}")
print(f"Dias entre primer y ultimo entrenamiento: {dias_diferencia}")
print(f"Campeon que mas entreno: {campeon_top}")
print(f"Promedio por dia: {promedio_por_dia}")
print(f"Campeon mas activo en fines de semana: {campeon_finde}")
