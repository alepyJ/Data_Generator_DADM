# Generaremos una lista de ejemplo de alergias comunes para crear una tabla "Alergia"

import pandas as pd

# Nombres de alergias comunes
alergias_nombres = [
    'Polen',
    'Polvo',
    'Lactosa',
    'Gluten',
    'Frutos secos',
    'Mariscos',
    'Picaduras de insectos',
    'Latex',
    'Medicamentos',
    'Pelo de animales'
]

# Crear DataFrame
alergia_df = pd.DataFrame({'Nombre': alergias_nombres})

# Ruta del archivo CSV a generar para "Alergia"
csv_file_path_alergia ='C://Users//Lenovo//OneDrive//Escritorio//UAB//C3S2//DADM//Proyecto CAR//Alergias.csv'
# Exportar DataFrame a CSV
alergia_df.to_csv(csv_file_path_alergia, index=False)

