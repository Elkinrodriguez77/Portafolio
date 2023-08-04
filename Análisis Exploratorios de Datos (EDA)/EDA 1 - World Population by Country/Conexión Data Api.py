# conexión a la api e indicación de la ruta para guardar el archivo:

import os
os.system('kaggle datasets download -d rajkumarpandey02/2023-world-population-by-country -p "G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\Análisis Exploratorios de Datos (EDA)\\EDA 1 - World Population by Country"')

# descomprimir archivo y crear df

import zipfile

with zipfile.ZipFile('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\Análisis Exploratorios de Datos (EDA)\\EDA 1 - World Population by Country\\2023-world-population-by-country.zip', 'r') as zip_ref:
    zip_ref.extractall('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\Análisis Exploratorios de Datos (EDA)\\EDA 1 - World Population by Country')

# df

import pandas as pd

df = pd.read_csv('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\Análisis Exploratorios de Datos (EDA)\\EDA 1 - World Population by Country\\countries-table.csv')







