import pandas as pd
import random
import os

# Leer Atletas.csv
atletas_df = pd.read_csv(os.path.join(os.getcwd(), 'Atletas.csv'))

# Semanas de registro
semanas = list(range(1, 13))

# Generar datos de grasa y músculo para cada atleta durante 12 semanas
grasa_data = {'ID_Atleta': [], 'Semana': [], 'Grasa (g)': []}
musculo_data = {'ID_Atleta': [], 'Semana': [], 'Músculo (g)': []}

for atleta in atletas_df['ID']:
    for semana in semanas:
        # Datos aleatorios de grasa y músculo
        grasa = random.randint(-500, 500)  # Ejemplo de cambio en gramos, puede ser positivo o negativo
        musculo = random.randint(-500, 500)  # Igualmente para músculo

        # Añadir a los diccionarios
        grasa_data['ID_Atleta'].append(atleta)
        grasa_data['Semana'].append(semana)
        grasa_data['Grasa (g)'].append(grasa)

        musculo_data['ID_Atleta'].append(atleta)
        musculo_data['Semana'].append(semana)
        musculo_data['Músculo (g)'].append(musculo)

# Crear DataFrames
grasa_df = pd.DataFrame(grasa_data)
musculo_df = pd.DataFrame(musculo_data)

# Exportar a CSV
grasa_df.to_csv(os.path.join(os.getcwd(), 'Grasa.csv'), index=False)
musculo_df.to_csv(os.path.join(os.getcwd(), 'Musculo.csv'), index=False)
