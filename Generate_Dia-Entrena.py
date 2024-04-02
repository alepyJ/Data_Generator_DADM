import pandas as pd
import random
import os

# Leer Atletas.csv
atletas_df = pd.read_csv(os.path.join(os.getcwd(), 'Atletas.csv'))

# Días de la semana
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Generar días de entrenamiento aleatorios para cada atleta
dias_entrena_data = {'Día_S': [], 'IDs_Atletas': []}
for atleta in atletas_df['ID']:
    # Asignar aleatoriamente entre 3 y 7 días de la semana para entrenamiento
    dias_asignados = random.sample(dias_semana, random.randint(3, 7))
    for dia in dias_asignados:
        if dia not in dias_entrena_data['Día_S']:
            dias_entrena_data['Día_S'].append(dia)
            dias_entrena_data['IDs_Atletas'].append(atleta)
        else:
            index = dias_entrena_data['Día_S'].index(dia)
            dias_entrena_data['IDs_Atletas'][index] += ';' + atleta

# Crear DataFrame
dia_entrena_df = pd.DataFrame(dias_entrena_data)

# Reordenar el DataFrame basado en los días de la semana para mantener el orden
dia_entrena_df['Día_S'] = pd.Categorical(dia_entrena_df['Día_S'], categories=dias_semana, ordered=True)
dia_entrena_df = dia_entrena_df.sort_values('Día_S')

# Exportar a CSV
dia_entrena_df.to_csv(os.path.join(os.getcwd(), 'Dia-Entrena.csv'), index=False)
