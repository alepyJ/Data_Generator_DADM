import pandas as pd
import os
import random

def generate_atleta_condicion():
    # Cargar los DataFrames
    atletas_df = pd.read_csv(os.path.join(os.getcwd(), 'Atletas.csv'))
    alergia_df = pd.read_csv(os.path.join(os.getcwd(), 'Alergias.csv')).rename(columns={'Nombre': 'Alergia/Enfermedad'})
    enfermedad_df = pd.read_csv(os.path.join(os.getcwd(), 'Enfermedades.csv')).rename(columns={'Nombre': 'Alergia/Enfermedad'})

    # Concatenar los DataFrames de alergias y enfermedades
    condiciones_df = pd.concat([alergia_df, enfermedad_df], ignore_index=True)

    # Lista para almacenar la asignación de atletas a condiciones
    atleta_condicion_data = {'ID_Atleta': [], 'Condicion': []}

    # Probabilidad de que un atleta tenga una condición
    probabilidad_condicion = 0.2  # 20% de probabilidad

    # Asignar condiciones a atletas basado en la probabilidad
    for _, atleta in atletas_df.iterrows():
        if random.random() < probabilidad_condicion:
            # Elegir aleatoriamente una condición para el atleta
            condicion_aleatoria = condiciones_df.sample(n=1)['Alergia/Enfermedad'].iloc[0]
            atleta_condicion_data['ID_Atleta'].append(atleta['ID'])
            atleta_condicion_data['Condicion'].append(condicion_aleatoria)

    # Crear DataFrame de Atleta-Condicion
    atleta_condicion_df = pd.DataFrame(atleta_condicion_data)

    # Exportar a CSV
    atleta_condicion_df.to_csv(os.path.join(os.getcwd(), 'Atleta-Condicion.csv'), index=False)

if __name__ == 'main':
    generate_atleta_condicion()