import pandas as pd

# Lista extendida de nombres de comidas con más variedad
comidas_nombres_extendida = [
    'Manzana', 'Pollo', 'Arroz', 'Salmón', 'Espinaca',
    'Almendra', 'Yogur', 'Quinoa', 'Huevo', 'Avena',
    'Tofu', 'Lentejas', 'Pavo', 'Brócoli', 'Patata',
    'Nueces', 'Plátano', 'Zanahoria', 'Tomate', 'Lechuga'
]

# Generar IDs para las comidas
comidas_ids = [f'Comida{i:03d}' for i in range(1, 21)]

# Crear DataFrame
comida_df_extendida = pd.DataFrame({
    'ID': comidas_ids,
    'Nombre': comidas_nombres_extendida
})

# Guardar en un archivo CSV
comida_df_extendida.to_csv('Comidas.csv', index=False)
