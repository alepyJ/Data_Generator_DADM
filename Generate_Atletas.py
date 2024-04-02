# Generar datos de ejemplo para la tabla Atleta ajustados a las disciplinas específicas
import random
import pandas as pd

atleta_data_especifico = {
    'ID': [f'Athlete{i:02d}' for i in range(1, 21)],
    'Altura': [random.randint(160, 200) for _ in range(20)],
    'Peso': [random.randint(50, 100) for _ in range(20)],
    'Sexo': [random.choice(['M', 'F']) for _ in range(20)],
    'Edad': [random.randint(18, 35) for _ in range(20)],
    'Disciplina': [random.choice(['Atletismo 100m', 'Fútbol 11', 'Halterofilia 2 tiempos']) for _ in range(20)],
    '%Musculo': [random.uniform(10, 20) for _ in range(20)],
    '%Grasa': [random.uniform(5, 25) for _ in range(20)]
}

# Crear el DataFrame con los datos ajustados
atleta_df_especifico = pd.DataFrame(atleta_data_especifico)

# Guardar el DataFrame como CSV
csv_file_path_especifico = 'C://Users//Lenovo//OneDrive//Escritorio//UAB//C3S2//DADM//Proyecto CAR//Atletas.csv'
atleta_df_especifico.to_csv(csv_file_path_especifico, index=False)
