# -*- coding: utf-8 -*-
"""
@author: Clara
"""

# %% Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns


# %% WINE DATASET

# Import file
wine = pd.read_csv('/home/Estudiante/Descargas/datos 3-2/clase 12-2/Clase 12 - Archivos-20260212/Archivos/wine.csv', sep=";")
# wine = pd.read_csv('wine.csv', sep=";")
cheetah_region = 'cheetahregion.csv'

# Display the first few rows of the DataFrame
print(wine.head())

# %% SCATTER PLOT Acidez vs Contenido de acido citrico
#ver - paneles -explorador de codigo

fig, ax = plt.subplots()

ax.scatter(
    data=wine,
    x='fixed acidity',
    y='citric acid',
    s=8,
    color='magenta'
)

ax.set_title('Acidez vs contenido de ácido cítrico')
ax.set_xlabel('Acidez (g/dm³)', fontsize=12)
ax.set_ylabel('Ácido cítrico (g/dm³)', fontsize=12)

plt.show()
# Genera el grafico que relaciona tres variables en simultaneo
# (mejorando la informacion mostrada)
fig, ax = plt.subplots()
tamanoBurbuja = 5
# Cuanto queremos modificar el tamaño de cada burbuja
ax.scatter(data=wine, x='fixed acidity',
y='citric acid', s=wine['residual sugar']*tamanoBurbuja)
ax.set_title('Relación entre tres variables')
ax.set_xlabel('Acidez (g/dm3)', fontsize='medium')
ax.set_ylabel('Contenido de ácido cítrico (g/dm3)',
fontsize='medium')
# remueve la variable temporal tamanoBurbuja que ya no utilizaremos
del(tamanoBurbuja)

# %% EJERCICIO VINO
# ¿Existe o no alguna relación entre el pH de los vinos (pH) 
# y alguna de las otras variables? Mostrarlo gráficamente 

fig, ax = plt.subplots()
ax.scatter(
    data=wine,
    x='pH',
    y='chlorides',
    s=8,
    color='magenta'
)
ax.set_title('pH vs citric acid')
ax.set_xlabel('pH', fontsize=12)
ax.set_ylabel('Ácido cítrico (g/dm³)', fontsize=12)





# %% CHEETAH REGIONS                              #

# Cargamos el dataset
cheetahRegion= pd.read_csv("/home/Estudiante/Descargas/datos 3-2/clase 12-2/Clase 12 - Archivos-20260212/Archivos/cheetahRegion.csv")

#%% GRAFICO DE LINEAS
# Genera el grafico de la serie temporal (grafico por defecto)
plt.scatter(data=cheetahRegion, x='Anio', y='Ventas')

# Genera el grafico de la serie temporal (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.plot('Anio', 'Ventas', data=cheetahRegion, marker="o")

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 12)
ax.set_ylim(0, 250)

# %% EJERCICIO BIODIESEL
#Considerar los siguientes datos correspondientes a los precios del 
#biodiesel en distintos períodos en la Argentina
#(se encuentran subidos en el campus)






# %% GRAFICO DE BARRAS (BAR PLOT)

#### Genera el grafico de barras de las ventas mensuales (grafico por defecto)
fig, ax = plt.subplots()

ax.bar(data=cheetahRegion, x='Anio', height='Ventas')

#### Genera el grafico de barras de las ventas mensuales (mejorando la informacion mostrada)
fig, ax = plt.subplots()       

ax.bar(data=cheetahRegion, x='Anio', height='Ventas')
       
ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1))               # Muestra todos los ticks del eje x
ax.set_yticks([])                          # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)   # Agrega la etiqueta a cada barra

#%% 10. PIE PLOT

# Contamos cuantos vinos de cada tipo hay en el dataset
wine['type'].value_counts()

# Transformamos la salida de value_counts en
# un dataframe
conteos = pd.DataFrame(wine['type'].value_counts()).reset_index()
conteos.columns = ['type', 'count']

# Genera el grafico de barras torta (mejorando la informacion mostrada)
fig, ax = plt.subplots()

ax.pie(data=conteos, 
       x='count', 
       labels='type',          # Etiquetas
       autopct='%1.2f%%',       # porcentajes
       colors=['gold',
               'purple'],
       shadow = True, 
       explode = (0.1,0)        # separa las slices del pie plot
       )

#%% EJERCICIO Telefonos
# Sean los siguientes datos correspondientes a 
# poseedores de teléfonos 
# (se encuentran subidos en el campus) 


# Generar un gráfico para representarlos gráficamente
# Analizar los resultados obtenidos
# Discutir con el resto de la clase
# ¿Cuál fue su objetivo: Explorar, Explicar, Otro?
# ¿Qué tipos de variables estaban en juego?
# ¿Qué tipo de gráfico decidió utilizar?
# ¿Qué resultados obtuvo?
# ¿Mejoró alguna característica del gráfico para cumplir con el objetivo?
# Responder Verdadero o Falso y justificar visualmente. 
# “Es más probable que las personas mayores posean un teléfono 
# inteligente a que las personas más jóvenes posean uno inteligente.”






# %% DISTRIBUCION DE DATOS CATEGORICOS

#### Cargamos dataset gaseosas
gaseosas= pd.read_csv("gaseosas.csv")

# Mostramos las primeras observaciones
gaseosas.head()

# Tabla de frecuencias
gaseosas['Compras_gaseosas'].value_counts()    

##### Genera el grafico de frecuencias (grafico por defecto)
gaseosas['Compras_gaseosas'].value_counts().plot.bar()

#### Genera el grafico de frecuencias mejorado

plt.rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
plt.rcParams['axes.spines.left']  = False            # Elimina linea izquierda  del recuadro
plt.rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro

fig, ax = plt.subplots()
gaseosas['Compras_gaseosas'].value_counts().plot.bar(ax = ax)

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas') 
ax.set_yticks([])                                  # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)         # Agrega la etiqueta a cada barra
ax.tick_params(axis='x', labelrotation=0)          # Rota las etiquetas del eje x
                                                    # para que las muestre horizontales
plt.show()      

# %% DISTRIBUCION DE DATOS CONTINUOS

ageAtDeath= pd.read_csv("ageAtDeath.csv")

#### Genera el grafico de frecuencias

#Graficar la distribucion usando seaborn
plt.figure(figsize=(8, 6))
sns.histplot(ageAtDeath['AgeAtDeath'], kde=False, bins=16, color='purple') # kde=True agrega la curva de densidad

plt.title('Distribución de edades al momento de muerte')
plt.xlabel('Edad al momento de muerte (años)')
plt.ylabel('Cantidad de personas')

# Mostrar el grafico
plt.show()

#%% DISTRIBUCION DE DATOS CONTINUOS SEGUN DOS VARIABLES

sns.histplot(data=ageAtDeath, x='AgeAtDeath', hue='Sex', kde=False)#hue='Sex' separa los datos por ese atributo

plt.title('Distribución de Edad al Morir por Sexo')
plt.xlabel('Edad al momento de la muerte (años)')
plt.ylabel('Cantidad de Personas')
plt.show()

# %% DISTRIBUCION DE DATOS CONTINUOS SEGUN DOS VARIABLES en forma de linea

# Suponiendo que tu DataFrame se llama df
sns.kdeplot(data=ageAtDeath, x='AgeAtDeath', hue='Sex')

plt.title('Distribución de Edad al Morir (Suavizada)')
plt.xlabel('Edad')
plt.ylabel('Densidad de Frecuencia')
plt.show()

# %% EJERCICIO Propinas
# Sean los datos correspondientes a las propinas de un bar 
# (están cargados en el campus en el archivo tips.csv)
# Generar un gráfico para analizar la distribución de la propina en función del:
# Sexo
# Día de la semana
# Comentar los resultados obtenidos

archivo = '/home/Estudiante/Descargas/datos 3-2/clase 12-2/Clase 12 - Archivos-20260212/Archivos/tips.csv'
df = pd.read_csv(archivo , sep=",")
sns.histplot(data=df, x='tip', hue='sex', kde=False)#hue='Sex' separa los datos por ese atributo

plt.title('Distribución de propinas segun sexo')
plt.xlabel('Dia de la semana')
plt.ylabel('propinas')

# Mostrar el grafico
plt.show()


sns.kdeplot(data=df, x='tip', hue='sex')

plt.title('Distribución de Edad al Morir (Suavizada)')
plt.xlabel('Edad')
plt.ylabel('Densidad de Frecuencia')
plt.show()




