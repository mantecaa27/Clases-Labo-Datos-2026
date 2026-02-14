# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 01:32:42 2026

"""

import pandas as pd 
archivo = "instituciones_de_salud.xlsx"

df = pd.read_excel(archivo)

df.to_csv("instituciones_de_salud.csv",index=False,encoding='utf-8')

archivoo = "instituciones_de_salud.csv"

df3 = pd.read_csv(archivoo,nrows=100)

columnas_validas = ['establecimiento_id', 'establecimiento_nombre','departamento_id','provincia_id','origen_financiamiento','tipologia_nombre']

df_valido = df[columnas_validas].copy()

df_valido.to_excel("instituciones_de_saludd.xlsx",index=False)
