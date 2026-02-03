# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:46:17 2026

@author: PC-FAMILIA
"""

#00-
empleado_01 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000]]

#01-
def superanSalarioActividad01(empleados,umbral):
    empleados_buen_salario = []
    for i in empleados:
        
        if i[3] > umbral:
            empleados_buen_salario.append(i)
    return empleados_buen_salario

uno = superanSalarioActividad01(empleado_01, 15000)

#02-
empleado_02 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000],[43967304,37,0,12000],[42236276,36,0,18000]]

dos = superanSalarioActividad01(empleado_02, 15000)   

#03-
def superanSalarioActividad03(empleados,umbral):
    buen_salario = []
    
    for i in empleados:
        
        if i[1] > umbral:
            empleados_aux = []
            dni = i[0]
            edad = i[2]
            cantidad_hijos = i[3]
            salario = i[1]
            empleados_aux = [dni,edad,cantidad_hijos,salario]
            buen_salario.append(empleados_aux)
            
        """    
            empleados_aux.append(i)
    for j in empleados:
        for h in empleados_aux:
            if h == j:
                h[3] = j[1]
                h[1] = j[2]
                h[2] = j[3]
                buen_salario.append(h)"""
    return buen_salario
            
           
   

empleado_03 = [[20222333,20000,45,2],[33456234,25000,40,0],[45432345,10000,41,1],[43967304,12000,37,0],[42236276,18000,36,0]]

tres = superanSalarioActividad03(empleado_03, 15000)

#04-

def superanSalarioActividad04(empleados,umbral):
    buen_salario = []
    
    for i in range(len(empleados[1])):
        
        if empleados[1][i] > umbral:
            empleados_aux = []
            dni = empleados[0][i]
            edad = empleados[2][i]
            cantidad_hijos = empleados[3][i]
            salario = empleados[1][i]
            empleados_aux = [dni,edad,cantidad_hijos,salario]
            buen_salario.append(empleados_aux)
    return buen_salario

empleado_04 = [[20222333,33456234,45432345,43967304,42236276],[20000,25000,10000,12000,18000],[45,40,41,37,36],[2,0,1,0,0]]

cuatro = superanSalarioActividad04(empleado_04, 15000)

# 05 - Respuestas a las preguntas conceptuales

"""
1. ¿Cómo afectó a la programación de la función cuando cambiaron levemente la matriz de empleado?
   a. En el caso en que le agregaron más filas:
      No afectó en absoluto porque la función estaba diseñada para recorrer todas las filas de la matriz, 
      independientemente de cuántas hubiera. El ciclo 'for' itera sobre cada fila, por lo que agregar más 
      filas no requiere cambios en la lógica.

   b. En el caso en que le alteraron el orden de las columnas:
      Afectó significativamente porque la función original asumía que el salario estaba en la columna 3 (índice 3). 
      Al cambiar el orden, tuvimos que crear una nueva función (superanSalarioActividad03) que:
        - Busca el salario en la nueva posición (índice 1 en empleado_03)
        - Reordena las columnas para devolverlas en el formato original: [DNI, Edad, Hijos, Salario]

2. ¿Y cuando a empleado le cambiaron la forma de representar las matrices (de lista de filas a lista de columnas)?
   Este fue el cambio más significativo. En lugar de una lista de filas (cada fila es un empleado), pasamos a una 
   lista de columnas (cada columna es una lista de valores para todos los empleados). Esto obligó a:
        - Cambiar completamente la forma de iterar (ahora por índices de columna)
        - Reconstruir cada fila tomando el elemento i-ésimo de cada columna
   La función superanSalarioActividad04 tuvo que ser escrita desde cero con una lógica diferente.

3. ¿Cuál es la ventaja, desde el punto de vista del usuario de la función, disponer de ella y no escribir 
   directamente el código de la consulta dentro de su programa?
   La ventaja principal es la Reutilización:
        - El usuario no necesita conocer la estructura interna de los datos
        - No tiene que escribir la lógica de filtrado cada vez
        - Si la estructura cambia, solo se actualiza la función (no todos los programas que la usan)
        - El código principal queda más limpio y legible
        - Se reduce la posibilidad de errores al no duplicar código
"""


