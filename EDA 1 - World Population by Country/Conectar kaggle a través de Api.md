# Pasos para conectar Kaggle a través de API

1. Instalar la librería de la API de Kaggle:

Primero, instala la API de Kaggle utilizando pip:

<pre>
pip install kaggle
<pre>

2. Configurar la API de Kaggle:

Para utilizar la API de Kaggle, necesitas un archivo de configuración llamado kaggle.json que contiene tu nombre de usuario y la clave de la API. Este archivo se puede generar desde la página de tu cuenta en Kaggle (https://www.kaggle.com/<nombre_de_usuario>/account), seleccionando "Create New API Token" en la sección "API". Descarga y guarda el archivo kaggle.json en la ruta ~/.kaggle/kaggle.json en tu máquina.

Asegúrate de dar al archivo los permisos de lectura y escritura sólo para el propietario para mantener segura tu clave de la API:

bash
<pre>
chmod 600 ~/.kaggle/kaggle.json
<pre>

El código anterior solo aplica para Linux o MacOS

3. Descargar y cargar el conjunto de datos:

Luego, puedes utilizar la API para descargar conjuntos de datos. Por ejemplo, si quieres descargar el conjunto de datos "titanic" de Kaggle, puedes hacerlo así:

python

<pre>
```
import os
os.system('kaggle datasets download -d <dataset-id> -p /path/to/download/directory')
Reemplaza <dataset-id> con el ID del conjunto de datos que deseas descargar. Esto se puede encontrar en la URL del conjunto de datos en Kaggle. Por ejemplo, para el conjunto de datos de Titanic, la URL es https://www.kaggle.com/c/titanic, por lo que el ID del conjunto de datos sería c/titanic.
```
</pre>

La opción -p especifica la ruta de la carpeta donde se guardará el conjunto de datos descargado.

Una vez que hayas descargado el conjunto de datos, puedes cargarlo en tu entorno de Python con la biblioteca adecuada. Si el conjunto de datos es un archivo CSV, puedes utilizar pandas para hacerlo:

python
import pandas as pd

data = pd.read_csv('/path/to/download/directory/titanic.csv')
Estos pasos deberían permitirte conectar a un conjunto de datos de Kaggle desde Python utilizando la API de Kaggle.

# Conexión final con script de python en power bi:

<pre>

import os
import zipfile
import pandas as pd

# conexión a la api e indicación de la ruta para guardar el archivo:
os.system('kaggle datasets download -d rajkumarpandey02/2023-world-population-by-country -p "G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\EDA 1 - World Population by Country"')

# descomprimir archivo y crear df
with zipfile.ZipFile('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\EDA 1 - World Population by Country\\2023-world-population-by-country.zip', 'r') as zip_ref:
    zip_ref.extractall('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\EDA 1 - World Population by Country')

# df
df = pd.read_csv('G:\\Mi unidad\\Marca Personal - Propósito de vida\\Generación de Contenido\\Portafolio\\EDA 1 - World Population by Country\\countries-table.csv')


<pre>