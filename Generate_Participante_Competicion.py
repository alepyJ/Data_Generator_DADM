import pandas as pd
import random
import os

def generate_participante_competicion():
    
    torneos_df = pd.read_csv(os.path.join(os.getcwd(), 'Competicion-Disciplina.csv'))

    # Leer Atletas.csv
    atletas_df = pd.read_csv(os.path.join(os.getcwd(), 'Atletas.csv'))

    # Preparar los datos para el archivo Participante-Torneo.csv
    participante_torneo_data = {'Torneo': [], 'Participante': []}

    # Asignar atletas a torneos basándose en la disciplina
    for _, torneo in torneos_df.iterrows():
        # Filtrar atletas que coincidan con la disciplina del torneo
        atletas_compatibles = atletas_df[atletas_df['Disciplina'] == torneo['Disciplina']]
        
        # Seleccionar aleatoriamente un subconjunto de atletas compatibles para participar en el torneo
        # Asumiendo que quieres entre 1 y 5 atletas por torneo para este ejemplo
        num_participantes = random.randint(1, min(5, len(atletas_compatibles)))
        atletas_seleccionados = atletas_compatibles.sample(n=num_participantes)
        
        for _, atleta in atletas_seleccionados.iterrows():
            participante_torneo_data['Torneo'].append(torneo['Competicion'])
            participante_torneo_data['Participante'].append(atleta['ID'])

    # Convertir a DataFrame
    participante_torneo_df = pd.DataFrame(participante_torneo_data)

    # Exportar a CSV
    participante_torneo_df.to_csv(os.path.join(os.getcwd(), 'Participante-Torneo.csv'), index=False)

if __name__ == 'main':
    generate_participante_competicion()
