import pandas as pd
import random
import os

# Cargar y renombrar columnas de Alergias y Enfermedades
alergia_df = pd.read_csv(os.path.join(os.getcwd(), 'Alergias.csv')).rename(columns={'Nombre': 'Alergia/Enfermedad'})
enfermedad_df = pd.read_csv(os.path.join(os.getcwd(), 'Enfermedades.csv')).rename(columns={'Nombre': 'Alergia/Enfermedad'})

# Concatenar los DataFrames ya renombrados
condiciones_df = pd.concat([alergia_df, enfermedad_df], ignore_index=True)

# Leer Comidas.csv
comida_df = pd.read_csv(os.path.join(os.getcwd(), 'Comidas.csv'))

# Generar incompatibilidades aleatorias utilizando el ID de la comida
incompatibilidades = []
for _, condicion in condiciones_df.iterrows():
    # Seleccionar entre 1 y 3 IDs de comidas aleatorias para cada condición
    comidas_incompatibles_ids = random.sample(list(comida_df['ID']), random.randint(1, 3))
    incompatibilidades.append({
        'Alergia/Enfermedad': condicion['Alergia/Enfermedad'], 
        'Comidas': ';'.join(comidas_incompatibles_ids)
    })

# Crear DataFrame de incompatibilidades
incompatibilidad_df = pd.DataFrame(incompatibilidades)

# Exportar a CSV
incompatibilidad_df.to_csv(os.path.join(os.getcwd(), 'Incompatibilidades.csv'), index=False)
