import pandas as pd
from datetime import datetime, timedelta
import random

# Leer los torneos desde Torneo-Disciplina.csv


# Función para generar una fecha de inicio y fin aleatoria pero coherente
def generar_fechas():
    inicio = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    duracion = timedelta(days=random.randint(1, 14))
    fin = inicio + duracion
    return inicio.strftime('%Y-%m-%d'), fin.strftime('%Y-%m-%d')

def generar_competicion_fecha():
    torneo_df = pd.read_csv('Competicion-Disciplina.csv')
    torneo_df['Fecha_Inicio'], torneo_df['Fecha_Fin'] = zip(*torneo_df.apply(lambda x: generar_fechas(), axis=1))
    torneo_df_sin_disciplina = torneo_df.drop(columns=['Disciplina'])
    torneo_df_sin_disciplina.to_csv('Competicion-Fecha.csv', index=False)

if  __name__ == 'main':
    generar_competicion_fecha()
