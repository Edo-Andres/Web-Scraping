import requests
from bs4 import BeautifulSoup
import json

from decouple import config

url = config('URL')

# Creamos una lista vacía para almacenar los datos de todas las páginas
datos_totales = []

# Iteramos sobre las primeras 10 páginas
for i in range(1, 11):

    # Pasamos el número de página como parámetro en la URL
    params = {'_paginador_fila_actual': i}
    response = requests.get(url, params=params)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    # Obtenemos la tabla que contiene los datos
    tabla = soup.find('table', class_='tabla_datos')

    # Creamos una lista vacía para almacenar los datos de la tabla
    datos = []

    # obtener todas las filas de la tabla
    filas = tabla.find_all('tr')
    # recorrer todas las filas de la tabla
    for fila in filas:
        # obtener todas las celdas de la fila
        celdas = fila.find_all('td')
        # si hay celdas
        if celdas:
            # guardar los datos de cada celda
            datos.append([celda.text for celda in celdas])

    # Agregamos los datos de la tabla a la lista total
    datos_totales += datos

# Convertimos la lista de datos totales a un objeto JSON y lo guardamos en un archivo
with open('datos_totales.json', 'w') as f:
    json.dump(datos_totales, f)
