# Actualizaremos el generador de la tabla de Entrenamientos para incluir IDs de Atletas aleatorios.

import pandas as pd
import random

# Datos de ejemplo para entrenamientos, incluyendo IDs de Atletas aleatorios
entrenamientos_data_actualizado = {
    'ID': [f'Entrenamiento{i:02d}' for i in range(1, 21)],
    'Tipo': [random.choice(['Aerobico', 'Anaerobico']) for _ in range(20)],
    'Duracion(minutos)': [random.randint(30, 120) for _ in range(20)],
    'ID_Atleta': [f'Athlete{random.randint(1,20):02d}' for _ in range(20)]  # Suponiendo que tenemos 20 atletas
}

# Crear DataFrame
entrenamiento_df_actualizado = pd.DataFrame(entrenamientos_data_actualizado)

# Visualizaremos las primeras filas del DataFrame para revisar los datos
entrenamiento_df_actualizado.to_csv('Entrenamiento.csv', index=False)

