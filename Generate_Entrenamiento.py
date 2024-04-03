import pandas as pd
import random

# Datos de ejemplo para entrenamientos, incluyendo IDs de Atletas aleatorios
entrenamientos_data = {
    'ID': [f'Entrenamiento{i:02d}' for i in range(1, 21)],
    'Tipo': [random.choice(['Aerobico', 'Anaerobico']) for _ in range(20)],
    'Duracion(minutos)': [random.randint(30, 120) for _ in range(20)],
    'ID_Atleta': [f'Athlete{random.randint(1,20):02d}' for _ in range(20)],  # Suponiendo que tenemos 20 atletas
    'Kcal Quemadas': []  # Añadiré los cálculos aquí
}

# Función para calcular las kcal quemadas aproximadas
def calcular_kcal_quemadas(tipo, duracion):
    if tipo == 'Aerobico':
        return round(random.uniform(5, 10) * duracion)
    else:  # Anaerobico
        return round(random.uniform(10, 15) * duracion)

# Calcular kcal quemadas para cada entrenamiento
for i in range(len(entrenamientos_data['ID'])):
    tipo = entrenamientos_data['Tipo'][i]
    duracion = entrenamientos_data['Duracion(minutos)'][i]
    entrenamientos_data['Kcal Quemadas'].append(calcular_kcal_quemadas(tipo, duracion))

# Crear DataFrame
entrenamiento_df_actualizado = pd.DataFrame(entrenamientos_data)

# Exportar a CSV
entrenamiento_df_actualizado.to_csv('Entrenamiento.csv', index=False)
