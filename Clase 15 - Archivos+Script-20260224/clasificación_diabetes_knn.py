#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:00:22 2025

@author: mcerdeiro
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
#%% cargar datos de diabetes
df_diabetes = pd.read_csv('diabetes.csv')
df_diabetes.columns
#%% X atributos, y etiqueta
X = df_diabetes[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df_diabetes['Outcome']
#%% para usar solo 2 atributos
X2 = df_diabetes[['Glucose', 'BMI']].values
y = df_diabetes['Outcome'].values
#%% gráfico de dispersión
plt.figure(figsize=(6, 4))
plt.scatter(X2[:, 0], X2[:, 1], c=y)
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.title('Distribución de los datos: Glucose vs BMI')
plt.show()
#%% construyo y ajusto el clasificador
clasificador = KNeighborsClassifier(n_neighbors=10)
clasificador.fit(X2, y)
#%% predicción para un nuevo paciente
nuevo_paciente = [[130, 32.0]] 
prediccion = clasificador.predict(nuevo_paciente)
print("Predicción para el nuevo paciente:", "Diabetes" if prediccion[0] == 1 else "No diabetes")
#%%
y_pred = clasificador.predict(X2)

a = confusion_matrix(y, y_pred)

b = accuracy_score(y, y_pred)

#%%
 
X_train = X2[:500]
y_train = y[:500]

# 2. Usamos X2 también para el test
X_test = X2[500:]
y_test = y[500:]

# 3. Entrenamos (el fit sí lleva X e y)
clasificador1 = KNeighborsClassifier(n_neighbors=5)
clasificador1.fit(X_train, y_train)

# 4. PREDICCIÓN (Aquí estaba el error: SOLO va X_test)
y_pred1 = clasificador1.predict(X_test)

# 5. Comparación y precisión
precision = accuracy_score(y_test, y_pred1)
print(precision)

k_valores = [5, 10, 15, 20, 25, 30, 35, 40]
lista_precision = []

for k in k_valores:
   
    modelo = KNeighborsClassifier(n_neighbors=k)
    
    # Entrenar con los primeros 500
    modelo.fit(X_train, y_train)
    
    #  Predecir con el resto
    y_pred = modelo.predict(X_test)
    
    
    precision = accuracy_score(y_test, y_pred)
    lista_precision.append(precision)
    print(f"Para K={k}, la precisión es: {precision:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(k_valores, lista_precision, marker='o', color='blue', linestyle='-')
plt.title('Precisión según el valor de K')
plt.xlabel('Valor de K (Vecinos)')
plt.ylabel('Precisión (Accuracy)')
plt.grid(True)
plt.show()

#%%





