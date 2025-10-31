#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
import pandas as pd
import numpy as np
from keys import *

city = "Rome"
country = "IT"
response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast/?q={city},{country}&appid={OWM_key}&units=metric&lang=en')


# In[20]:


# Convertimos lo que nos responde la API en un diccionario de Python
data = response.json()

# Imprimimos todo el contenido tal cual lo manda la API
print(data)

# Sacamos la lista de pronósticos
forecast_list = data.get('list', [])

# Creamos listas vacías para guardar los datos que luego vamos a meter en el DataFrame
times = []
temperatures = []
humidities = []
weather_statuses = []
wind_speeds = []
rain_volumes = []
snow_volumes = []

# Recorremos cada pronóstico de 3 horas que viene en el JSON
for entry in forecast_list:
    # Guardamos la fecha y hora
    times.append(entry.get('dt_txt', np.nan))
    # Guardamos la temperatura
    temperatures.append(entry.get('main', {}).get('temp', np.nan))
    # Guardamos la humedad
    humidities.append(entry.get('main', {}).get('humidity', np.nan))
    # Guardamos el tipo de clima (Clear, Clouds, Rain, etc.)
    weather_statuses.append(entry.get('weather', [{}])[0].get('main', np.nan))
    # Guardamos la velocidad del viento
    wind_speeds.append(entry.get('wind', {}).get('speed', np.nan))
    # Guardamos cuánta lluvia cayó en esas 3 horas
    rain_volumes.append(entry.get('rain', {}).get('3h', np.nan))
    # Guardamos cuánta nieve cayó en esas 3 horas
    snow_volumes.append(entry.get('snow', {}).get('3h', np.nan))

# Armamos un DataFrame con todos los datos que juntamos
df = pd.DataFrame({
    'time': times,
    'temperature': temperatures,
    'humidity': humidities,
    'weather_status': weather_statuses,
    'wind_speed': wind_speeds,
    'rain_volume_3h': rain_volumes,
    'snow_volume_3h': snow_volumes,
    'municipality_iso_country': f"Rome,IT"
})

# Mostramos las primeras 5 filas del DataFrame para ver si todo se acomodó bien
print(df.head())


# In[41]:


import sqlalchemy
import pymysql
# connection details for the local mysql database
schema = 'gans'
host = '172.25.112.1'
user = 'root'
password = '12345'
port = 3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# In[42]:


# send the weather data to the database
df.to_sql('weather_data', if_exists = 'append', con = con, index=False)

