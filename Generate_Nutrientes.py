import pandas as pd
import random
import os

# Leer Comida.csv
comida_df = pd.read_csv(os.path.join(os.getcwd(), 'Comidas.csv'))

# Lista de nutrientes a considerar
nutrientes = [
    'Carbohidratos (g)', 'Proteínas (g)', 'Grasas (g)', 
    'Vitamina D (µg)', 'Vitamina B1 (mg)', 'Vitamina B2 (mg)', 'Vitamina B3 (mg)', 
    'Vitamina B6 (mg)', 'Vitamina B7 (µg)', 'Vitamina B9 (µg)', 'Vitamina B12 (µg)', 
    'Vitamina C (mg)', 'Vitamina E (mg)', 'Minerales (mg)', 'Hierro (mg)', 
    'Calcio (mg)', 'Magnesio (mg)', 'Zinc (mg)', 'Sodio (mg)', 'Potasio (mg)'
]

# Función para generar valores nutricionales aleatorios pero racionales
def generar_valores_nutricionales():
    valores = {
        'Carbohidratos (g)': random.randint(0, 100),
        'Proteínas (g)': random.uniform(0, 30),
        'Grasas (g)': random.uniform(0, 50),
        'Vitamina D (µg)': random.uniform(0, 25),
        'Vitamina B1 (mg)': random.uniform(0, 1.5),
        'Vitamina B2 (mg)': random.uniform(0, 1.7),
        'Vitamina B3 (mg)': random.uniform(0, 20),
        'Vitamina B6 (mg)': random.uniform(0, 2),
        'Vitamina B7 (µg)': random.uniform(0, 300),
        'Vitamina B9 (µg)': random.uniform(0, 400),
        'Vitamina B12 (µg)': random.uniform(0, 6),
        'Vitamina C (mg)': random.randint(0, 95),
        'Vitamina E (mg)': random.uniform(0, 15),
        'Minerales (mg)': random.randint(0, 100),
        'Hierro (mg)': random.uniform(0, 18),
        'Calcio (mg)': random.randint(0, 1300),
        'Magnesio (mg)': random.randint(0, 400),
        'Zinc (mg)': random.uniform(0, 11),
        'Sodio (mg)': random.randint(0, 2300),
        'Potasio (mg)': random.randint(0, 4700)
    }
    return valores

# Inicializar el DataFrame con la columna 'ID_Comida' primero
columnas = ['ID_Comida'] + nutrientes
nutriente_data = {col: [] for col in columnas}

for _, fila in comida_df.iterrows():
    valores_nutricionales = generar_valores_nutricionales()
    nutriente_data['ID_Comida'].append(fila['ID'])
    for nutriente, valor in valores_nutricionales.items():
        nutriente_data[nutriente].append(valor)

# Construir el DataFrame asegurándose de que 'ID_Comida' sea la primera columna
nutriente_df = pd.DataFrame(nutriente_data, columns=columnas)

# Exportar a CSV
nutriente_df.to_csv(os.path.join(os.getcwd(), 'Nutrientes.csv'), index=False)
