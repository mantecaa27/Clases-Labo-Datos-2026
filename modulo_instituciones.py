# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 01:32:42 2026

"""

import pandas as pd 
import duckdb as dd
archivo = "instituciones_de_salud.xlsx"

df = pd.read_excel(archivo)

#df.to_csv("instituciones_de_salud.csv",index=False,encoding='utf-8')
"""
archivoo = "instituciones_de_salud.csv"

df3 = pd.read_csv(archivoo,nrows=100)



df_valido.to_excel("instituciones_de_saludd.xlsx",index=False)
"""
columnas_validas = ['establecimiento_id', 'establecimiento_nombre','departamento_id','provincia_id','origen_financiamiento','tipologia_nombre']

df_valido = df[columnas_validas].copy()

#%% PRIMERAS CONSULTAS
#Cambio la columna tipologia_nombre por tiene_uai (UNIDAD DE INTERNACION) determinado por el sistema REFES
#El valor de dicha columna es 1 si tiene, y 0 en caso contrario.

consultaSQL = """
SELECT establecimiento_id, establecimiento_nombre, departamento_id, provincia_id, origen_financiamiento,
    CASE 
        WHEN UPPER(tipologia_nombre)
        LIKE '%INTERNACIÓN%'
        OR UPPER(tipologia_nombre) 
        LIKE '%TERAPIA%'
        THEN 1
        ELSE 0
    END AS tiene_uai
FROM df_valido

"""

df_valido = dd.query(consultaSQL).df()

#%% Origen_financiamiento
#Cambio los valores de origen_financiamiento por público y Privado

consultaSQL = """
SELECT establecimiento_id, establecimiento_nombre, departamento_id, provincia_id, tiene_uai,
    CASE 
        WHEN UPPER(origen_financiamiento) IN
        ('PRIVADO', 'MUTUAL', 'MIXTA','UNIVERSITARIO PRIVADO', 'OBRA SOCIAL')
        THEN 'Privado'
        ELSE 'Público'
    END AS origen_financiamiento
FROM df_valido

"""

df_valido = dd.query(consultaSQL).df()

