# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 20:31:40 2026

@author: PC-FAMILIA
"""
import csv
import pandas as pd
# 1-

nombreArchivo = "arbolado-en-espacios-verdes.csv"
def leer_parque(nombre_archivo, parque):
    lista = []
    with open(nombre_archivo, encoding='utf-8') as f:
        for fila in csv.DictReader(f):
            if fila['espacio_ve'] == parque:
                lista.append(fila)
    return lista
parque = 'GENERAL PAZ'

b =leer_parque(nombreArchivo, parque)
print(b)

# 2-
def especies(lista_arboles):
    lista = set()
    for i in lista_arboles:
        lista.add(i['nombre_com'])
    return lista

c = especies(b)

# 3-

def contar_ejemplares(lista_arboles):
    dicc = {}
    for i in lista_arboles:
        if i['nombre_com'] in dicc.keys():
            dicc[i['nombre_com']] += 1 
        else:
            dicc[i['nombre_com']] = 1
    return dicc

d = contar_ejemplares(b)

#4-

def obtener_alturas(lista_arboles, especie):
    lista = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            lista.append(float(i['altura_tot']))
    return lista 
e = obtener_alturas(b, 'Jacarandá')

altura_prom = sum(e) / len(e)
    
#5-

def obtener_inclinaciones(lista_arboles, especie):
    lista = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            lista.append(int(i['inclinacio']))
    return lista

f = obtener_inclinaciones(b, 'Jacarandá')

#6-

def especimen_mas_inclinado(lista_arboles):
    especie = ''
    inclinacion_maxima = 0
    for i in lista_arboles:
        if int(i['inclinacio']) > inclinacion_maxima:
            inclinacion_maxima = int(i['inclinacio'])
            especie = i['nombre_com']
    return (especie,inclinacion_maxima)

g = especimen_mas_inclinado(b)

#7-

def especie_promedio_mas_inclinada(lista_arboles):
    especie = ''
    promedio_maximo = 0
    for i in especies(lista_arboles):
        inclinaciones = obtener_inclinaciones(lista_arboles, i)
        promedio = sum(inclinaciones)/len(inclinaciones)
        if promedio > promedio_maximo:
            promedio_maximo = promedio
            especie = i
    return (especie,promedio_maximo)

h = especie_promedio_mas_inclinada(b)

#8- 

df_parques = pd.read_csv('arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('arbolado-publico-lineal-2017-2018.csv')

data_arboles_veredas =  df_veredas[
    ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']].copy()

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

especie = 'Tipuana tipu'

"""df_vereda_especie = data_arboles_veredas[
    data_arboles_veredas['nombre_cientifico'] == especie
]"""
    
def filtrar_especie(df, especie):
    return df[df['nombre_cientifico'] == especie]

df_vereda_especie = filtrar_especie(data_arboles_veredas, especie)

a = df_vereda_especie.head()

especiee = 'Tipuana Tipu'

v = df_parques['nombre_cie']


def filtrar_especie2(df, especie):
    return df[df['nombre_cie'] == especie]        

v = df_parques.columns
data_arboles_parques =  df_parques[
    ['nombre_cie', 'diametro', 'altura_tot']].copy()

j = filtrar_especie2(data_arboles_parques, especiee)
parques= j.copy()

#9-
parques['ambiente'] = 'parque'
veredas = df_vereda_especie.rename(columns={'nombre_cientifico':'nombre_cie',
    'altura_arbol': 'altura_tot',
    'diametro_altura_pecho': 'diametro'
})

veredas['ambiente'] = 'vereda'
veredas = veredas[['nombre_cie','altura_tot', 'diametro', 'ambiente']]

#10- 

pd.concat([parques,veredas])