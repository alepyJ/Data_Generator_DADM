import os

#elimina todos los CSVs del fichero actual

def eliminar_archivos_csv(directorio):
    # Listar todos los archivos en el directorio
    archivos = os.listdir(directorio)
    
    # Filtrar aquellos que terminan en .csv
    archivos_csv = [archivo for archivo in archivos if archivo.endswith('.csv')]
    
    # Eliminar cada archivo CSV encontrado
    for archivo_csv in archivos_csv:
        os.remove(os.path.join(directorio, archivo_csv))
        print(f"Archivo eliminado: {archivo_csv}")

# Usar la función en el directorio actual
directorio_actual = os.getcwd()
eliminar_archivos_csv(directorio_actual)
