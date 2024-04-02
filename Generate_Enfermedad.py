import pandas as pd

# Lista de nombres de enfermedades comunes
enfermedades_nombres = [
    'Diabetes',
    'Hipertensión',
    'Asma',
    'Artritis',
    'Esclerosis múltiple',
    'Enfermedad celíaca',
    'Fibrosis quística',
    'Anemia',
    'Hipotiroidismo',
    'Hipertiroidismo'
]

# Crear DataFrame
enfermedad_df = pd.DataFrame({'Nombre': enfermedades_nombres})

# Guardar en un archivo CSV
enfermedad_df.to_csv('Enfermedades.csv', index=False)
