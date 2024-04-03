import pandas as pd
import random
import os

# Leer Atletas.csv
atletas_df = pd.read_csv(os.path.join(os.getcwd(), 'Atletas.csv'))

# Lista de nutrientes a considerar
nutrientes = [
    'Carbohidratos (g)', 'Proteínas (g)', 'Grasas (g)', 
    'Vitamina D (µg)', 'Vitamina B1 (mg)', 'Vitamina B2 (mg)', 'Vitamina B3 (mg)', 
    'Vitamina B6 (mg)', 'Vitamina B7 (µg)', 'Vitamina B9 (µg)', 'Vitamina B12 (µg)', 
    'Vitamina C (mg)', 'Vitamina E (mg)', 'Minerales (mg)', 'Hierro (mg)', 
    'Calcio (mg)', 'Magnesio (mg)', 'Zinc (mg)', 'Sodio (mg)', 'Potasio (mg)'
]

# Función para generar valores nutricionales aleatorios pero racionales
def generar_valores_nutricionales(dia_entrenamiento):
    if dia_entrenamiento:
        # Aumentar carbohidratos y proteínas en un 20% para días de entrenamiento
        factor = 1.2
    else:
        # Mantener requerimientos estándar en días de descanso
        factor = 1.0

    valores = {
        'Carbohidratos (g)': round(300 * factor),
        'Proteínas (g)': round(150 * factor),
        'Grasas (g)': round(70 * factor),
        'Vitamina D (µg)': 15, 'Vitamina B1 (mg)': 1.2, 'Vitamina B2 (mg)': 1.3,
        'Vitamina B3 (mg)': 16, 'Vitamina B6 (mg)': 1.3, 'Vitamina B7 (µg)': 30,
        'Vitamina B9 (µg)': 400, 'Vitamina B12 (µg)': 2.4, 'Vitamina C (mg)': 90,
        'Vitamina E (mg)': 15, 'Minerales (mg)': 100, 'Hierro (mg)': 18,
        'Calcio (mg)': 1000, 'Magnesio (mg)': 400, 'Zinc (mg)': 11,
        'Sodio (mg)': 2300, 'Potasio (mg)': 4700
    }
    return [round(valor) for valor in valores.values()]

# Preparar datos para ambos archivos CSV
nutrients_trainday = []
nutrients_offday = []

for _, atleta in atletas_df.iterrows():
    nutrients_trainday.append([atleta['ID']] + generar_valores_nutricionales(True))
    nutrients_offday.append([atleta['ID']] + generar_valores_nutricionales(False))

# Convertir a DataFrame
df_trainday = pd.DataFrame(nutrients_trainday, columns=['Deportista'] + nutrientes)
df_offday = pd.DataFrame(nutrients_offday, columns=['Deportista'] + nutrientes)

# Exportar a CSV
df_trainday.to_csv(os.path.join(os.getcwd(), 'Nutrients_trainday.csv'), index=False)
df_offday.to_csv(os.path.join(os.getcwd(), 'Nutrients_offday.csv'), index=False)
