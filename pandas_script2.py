#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:23:11 2024

@author: mcerdeiro
"""

import pandas as pd
import numpy as np


#%% armo un dataframe a partir de un diccionario
d = {'nombre':['Antonio', 'Brenda', 'Camila', 'David', 'Esteban', 'Felicitas'], 'apellido': ['Restrepo', 'Saenz', 'Torres', 'Urondo', 'Valdes', 'Wainstein'], 'lu': ['78/23', '449/22', '111/24', '1/21', '201/06', '47/20'], 'nota1': [9, 7, 7, 4, 3, np.nan], 'nota2': [10, 6, 7, 8, 5, np.nan], 'aprueba': [True, True, True, False, False, np.nan]}

df = pd.DataFrame(data = d) # creamos un df a partir de un diccionario
df.set_index('lu', inplace = True) # seteamos una columna como index
#%%
df.head()   
df.tail()
df.info() 
df.dtypes
df.columns  
df.index
df.describe() 
df[['nombre', 'nota1']]
df['nombre']
df.iloc[2]
df.iloc[2:6]
df.loc['78/23']
df.loc['78/23', 'nombre']
df.sample()
df.sample(n = 3)

#%% manejo de valores NaN

"""
.isna()
operacion de consulta (no cambia el dataFrame)
si el valor es nulo --> devuelve true 
si el valor es valido --> devuelve false 
"""
df.isna() 


# .notna() -> lo mismo que isna() pero al reves

df.notna()

"""
.dropna() 
.No cambia el dataFrame, devuelve vista limpia sin los valores nulos 
"""
df.dropna()

"""
df.dropna(axis='columns') es = a df.dropna(axis = 1) y si encuentra al menos 1 valor nulo, borra la columna
"""
df.dropna(axis='columns')


df.dropna(how='all') # solo si TODA la fila es nula

# thresh = n: si la fila tiene al menos n valores no nulos (no la borra)
df.dropna(thresh=2) # solo si tiene muy pocos campos (trhesh) no-nan

#borra si encuentra un valor nan en alguna de estas columnas
df.dropna(subset=['nombre', 'apellido'])

df.dropna(subset=['nota1', 'apellido'])

"""
fillna(x) devuelve una copia del df con los datos rellenos
"""
df.fillna(0)

values = {"nota1": 0, "nota2": 0, "aprueba": False}
df.fillna(value=values)


#%% ordenar por alguna columna 
"""
-no cambia el dataFrame
-devuelve el dataFrame con la columna ordenada.
- ascending = true, devuelve de menor a mayor.
-ascending = false de mayor a menor
- en este caso, como la columna 'nombre' es de strings, va de Z-A

"""
df.sort_values(by= 'nombre', ascending = False)


#%% modificar una o varias entradas

df.loc['1/21', 'nombre'] = 'Daniel' # modifico la entrada accediendo a la ubicación por fila (index) y columna (nombre de la columna) y defino el nuevo valor con '='

df 

df.replace({'nombre': {'David': 'Daniel'}}) # modifico todas las apariciones de David
df

### OJO - un caso es inplace, el otro no.
#cambia todos los 7 por 8 en el dataFrame
#no cambia el dataFrame
df.replace(7, 8)

#lo mismo pero con mas valores. 
#  df.replace({7: 8, 3: 2},regex=True) cambia los 7.5 por ejemplo

df.replace({7: 8, 3: 2})

#cambia en la columna 
df.replace({'nota2': {7: 9, 5: 6}})

df.astype({'nota2': 'float'})  # cambio de tipo

#%% modificar nombres de las columnas
#no cambia el df

df.rename(columns={"nota1": "Parcial1", "nota2": "Parcial2"})
df

#%% calcular promedio y otras cosas
#devuelve el minimo de cada columna 
df.agg('min')

#mean funciona solo con datos numericos
df.agg(['sum', 'min', 'max', 'mean'])

df['promedio'] = (df['nota1'] + df['nota2'])/2


#%%
#devuelve true sii en la columna todos los valores son True, strings no vacios o numeros distintos al 0 
df.all() # solo para variables booleanas (OJO --> si no es bool es todo es True salvo el caso vacío)

#devuelve true si alguno lo es
df.any()

#devuelve true si todos (o alguno en any()) los datos son Nan
df.isna().all()
df.isna().any()

#devuelven true si todos o alguno aprueba
df['aprueba'].all()
df['aprueba'].any()

#%% otros "drop" - eliminar partes del df

df.drop(['78/23'], axis = 0) # tiro la fila con index = 78/23

df.drop(['apellido', 'nombre'], axis = 1) # tiro las columnas apellido y nombre

df.duplicated() # dice True en las filas que están duplicadas (luego de la primera aparición)

df.duplicated(keep=False) # dice True en las filas que están duplicadas (incluyendo la primera aparición)

df.duplicated(subset=['nota1'])

df.duplicated(subset=['nota1'], keep = False)

df.drop_duplicates()

df.drop_duplicates(subset=['nota1'])

df.drop_duplicates(subset=['nota1'], keep = 'last')

#%% chequear condiciones

#devuelve una copia del df con true en todos los 7, y false en el resto
df == 7

#mismo que ==7
df.eq(7)

#lo contrario a ==7
df!= 7

# da una copia del df con true en los valores del df que sean 6 o 7
df.isin([6, 7])

#lo contrario
~df.isin([6, 7])

#isin en una columna
df.isin({'nota1': [6,7]})

#%% otras funciones aplicables al df

"""
.eval()
crea o modifica cierta columna del dF
no modifica el dF 
"""
df.eval('nota_final = nota1 + 1')

df.eval('promedio = 0.5*nota1 + 0.5*nota2')

"""
applymap()
devuelve una copia del df con la funcion definida en el argumento aplicada a cada celda del df
"""
df.applymap(lambda x: len(str(x))) # defino la funcion acá mismo

#hace lo mismo pero en la columna 
df[['nombre']].applymap(lambda x: x.upper())

df[['nota1']].applymap(lambda x: x*10)

# puedo armar la función aparte o dentro del applymap con lambda
def f(x):
    res = x+1
    return res
#acá la funcion f ya está creada 
df[['nota1']].applymap(f)

df[['nota1']].applymap(lambda x: x + 1)

"""
.transform() hace lo mismo que applymap() pero se asegura que el tamaño del df que devuelve sea el mismo que el original
"""
df[['nota1', 'nota2']].transform(lambda x: x*10)
#%% iterar sobre las filas
df.iterrows()

for e in df.iterrows():
    print(e)

for i, e in df.iterrows():
    print(i, e['nombre'])


df.itertuples()

for e in df.itertuples():
    print(e)
    
for e in df.itertuples():
    print(e.nombre)

for e in df.itertuples():
    print(e.Index)

#identifica a los estudiantes que arrancaron en la pandemia mediante sus ultimos digitos de LU
lista_ingresantes_pandemia = []
for e in df.itertuples():
    ingreso = int(e.Index.split('/')[1])
    if ingreso in [20, 21]:
        lista_ingresantes_pandemia.append((e.apellido, e.nombre))


#%% concatenar con otro dataframe
d2 = {'nombre':['Gregoria', 'Horacio'], 'apellido': ['Pérez', 'Quirno'], 'lu': ['09/23', '657/21'], 'nota1': [2,10], 'nota2': [7, 8], 'aprueba': [False, True]}

df_nuevo = pd.DataFrame(data = d2)
df_nuevo.set_index('lu', inplace = True) 
#concat devuelve un nuevo df de dos o mas df´s concatenados.
#si tienen las mismas columnas, pone los nuevos elementos abajo. si no, las crea
pd.concat([df, df_nuevo])

#%% armar una copia

df_copia = df.copy()
#%% guardar el dataframe como archivo csv

df.to_csv('planilla')



#%% FILTROS

df['nota1']>=7 # nos da una serie booleana, que indica donde se cumple la condición
# el index de esta serie es el del df

(df['nota1']>=7).sum()

df[df['nota1']>=7] # nos da el sub-dataframe donde se cumple la condición

df[ (df['nota1']>=7) & (df['nota2']>=7)]

df[ df['nota1']== 7]


df[ df['nota1'].isin([7,4])]

df[(df['nota2'] <=7) & df['aprueba']]

df[(df['nota2'] <=7) | df['aprueba']]

#%% otras cosas
#to_numpy() deja los datos crudos en un array
a = df.to_numpy() # con tipos mixtos no

d = df[['nota1', 'nota2']].dropna().to_numpy()

#unique() muestra todos los valores que aparecieron en la columna
df['nota1'].unique() 

#value_counts() cuenta las apariciones de cada valor
#dropna = False hace que cuente los NaN
df['nota1'].value_counts(dropna = False)

# funciona al reves
#donde no cumple la condicion, reemplaza por el valor
#no cambia el df original
df.where(df['nota1'] > 6, 0) # donde no es mayor a 6 pongo 0