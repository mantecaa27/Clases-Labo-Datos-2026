# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================
carpeta = "/home/Estudiante/Descargas/datos 3-2/Clases 06-08 - SQL - Archivos clase (template script + datos)-20260203/"
# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.query(consultaSQL).df()

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
               SELECT DISTINCT Sexo
               FROM empleado;

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
                SELECT DISTINCT DNI, Nombre, Sexo, Salario
                FROM empleado
                WHERE Sexo='F';
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
                SELECT DISTINCT DNI, Nombre, Sexo, Salario
                FROM empleado
                WHERE Sexo='F' AND Salario>15000;
              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
                SELECT DISTINCT DNI AS id, Salario AS Ingreso
                FROM empleado;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
                SELECT DISTINCT Codigo, Nombre
                FROM aeropuerto
                WHERE Ciudad='Londres'

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
                SELECT DISTINCT Ciudad AS City 
                FROM aeropuerto 
                WHERE Codigo='ORY' OR Codigo='CDG';

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
                SELECT DISTINCT Numero  
                FROM vuelo 
                WHERE Origen='CDG' AND Destino='LHR';

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
                SELECT DISTINCT Numero  
                FROM vuelo 
                WHERE (Origen='CDG' AND Destino='LHR') OR (Origen='LHR' AND Destino='CDG');
              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
                SELECT DISTINCT Fecha  
                FROM reserva
                WHERE Precio > 200;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
                SELECT DISTINCT * 
                FROM alumnosBD
                UNION 
                SELECT DISTINCT *
                FROM alumnosTLeng;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """

              """

dataframeResultado = dd.query(consultaSQL).df()

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
                
                
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT DISTINCT * numero 
                FROM vuelo
            EXCEPT
                SELECT DISTINCT * NroVuelo
                FROM reserva;
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                SELECT DISTINCT Destino
                FROM vuelo
            UNION
                SELECT DISTINCT Origen
                FROM vuelo;
              """
              
dataframeResultado = dd.query(consultaSQL).df()



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
                CROSS JOIN nacionalidades;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
                INNER JOIN nacionalidades
                ON Nacionalidad=IDN
                
              """

dataframeResultado = dd.query(consultaSQL).df()


#%% --------------------------------------------------------------------------------------------
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """
                

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
                LEFT OUTER JOIN nacionalidades
                ON Nacionalidad=IDN 

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
                SELECT DISTINCT LU, nombre
                FROM se_inscribe_en
                INNER JOIN materia
                ON se_inscribe_en.codigo_materia = materia.codigo_materia
              """

dataframeResultado = dd.query(consultaSQL).df()

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                SELECT DISTINCT *
                FROM aeropuerto
                INNER JOIN vuelo
                ON Codigo = Origen
                WHERE Numero = 165
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.query("""
            SELECT DISTINCT Numero, Destino
            FROM vuelo AS v
            WHERE v.Origen = 'MAD';
              """).df()

dniPersonasDesdeMadrid = dd.query("""
            SELECT DISTINCT DNI, Destino, Fecha
            FROM reserva AS r
            INNER JOIN vuelosDesdeMadrid AS v
            ON v.Numero = r.NroVuelo

              """).df()

consultaSQL = """
                SELECT Nombre, Fecha, Destino
                FROM dniPersonasDesdeMadrid AS d
                INNER JOIN pasajero AS p
                ON d.DNI = p.DNI

              """

dataframeResultado = dd.query(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
                SELECT DISTINCT r.fecha,v.salida, p.Nombre
                FROM reserva AS r, vuelo AS v, pasajero AS p
                WHERE r.DNI and r.Nrovuelo = v.numero
              """

dataframeResultado = dd.query(consultaSQL).df()

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
                SELECT DISTINCT er.empleado, er.rol, rp.proyecto
                FROM empleadoRol AS er
                INNER JOIN rolProyecto AS rp 
                ON er.rol=rp.rol

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
                SELECT count(*) AS cantidadExamenes
                FROM examen;

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
                SELECT count(*) AS cantidadExamenes
                FROM examen
                WHERE instancia = 'Parcial-01'

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """
                SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
                SELECT count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                HAVING Asistieron < 4 
                ORDER BY Instancia ASC
                

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """
                SELECT Instancia,
                AVG(Edad) AS PromedioEdad
                FROM examen
                GROUP BY Instancia
                ORDER BY Instancia;

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """
                SELECT Instancia, AVG(Nota) AS NotaPromedio
                FROM examen
                GROUP BY Instancia
                HAVING instancia LIKE'Parcial%'
                ORDER BY Instancia;

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
                SELECT Instancia, AVG(Nota) AS NotaPromedio
                FROM examen
                GROUP BY Instancia
                HAVING instancia LIKE'Parcial%'
                ORDER BY Instancia;


              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT Nombre, Nota,
                CASE WHEN Nota>=4
                    THEN 'APROBÓ'
                    ELSE 'NO APROBÓ'
                END AS Estado
                FROM examen
                WHERE Instancia='Parcial-01'
                ORDER BY Nombre;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                SELECT Instancia,
CASE WHEN Nota>=4
THEN 'APROBÓ'
ELSE 'NO APROBÓ'
END AS Estado,
COUNT(*) as Cantidad
FROM examen
GROUP BY Instancia, Estado
ORDER BY Instancia, Estado;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen AS e1
                WHERE e1.Nota > (
                    SELECT AVG(e2.Nota)
                    FROM examen AS e2
                    WHERE e2.Instancia = e1.Instancia
)
                ORDER BY Instancia ASC, Nota DESC;
            
              """


dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
              SELECT e1.Nombre, e1.Instancia, e1.Nota
FROM examen AS e1
WHERE e1.Nota >= ALL (
SELECT e2.Nota
FROM examen AS e2
WHERE e2.Instancia = e1.Instancia
)
ORDER BY e1.Instancia ASC, e1.Nombre ASC;
                

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
  FROM examen AS e1
  WHERE e1.Nombre NOT IN (
  SELECT Nombre
  FROM examen AS e2 
  WHERE e2.Instancia LIKE 'Recuperatorio%'
  )
  ORDER BY e1.Instancia ASC, e1.Nombre ASC;
                  


              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """
                SELECT *
                FROM examen
                WHERE Nota > """ + str(umbralNota)
dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
                SELECT *
                FROM examen03
                WHERE Nota < 9

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                SELECT *
                FROM examen03
                WHERE Nota >= 9
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
SELECT *
FROM examen03
WHERE (Nota >= 9) OR (Nota < 9)

              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
                SELECT AVG(Nota) AS NotaPromedio
                FROM examen03
                
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
                SELECT AVG(CASE WHEN Nota IS NULL THEN 0 ELSE Nota END) AS NotaPromedio
                FROM examen03


              """


dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """
                SELECT empleado, UPPER(rol) AS rol
FROM empleadoRol;

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """
SELECT empleado, LOWER(rol) AS rol
FROM empleadoRol;

              """

dataframeResultado = dd.sql(consultaSQL).df()




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """
SELECT empleado, REPLACE(rol,'ñ','ni') AS rol
FROM empleadoRol;

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
consultaSQL = """
                SELECT Nombre, Sexo,Edad
FROM examen



"""
datosEstudiantes = dd.sql(consultaSQL).df()

consultaSQL = """
SELECT DISTINCT de.*,Nota AS Parcial_01
FROM datosEstudiantes AS de 
LEFT OUTER JOIN examen AS e
ON de.Nombre = e.Nombre AND Instancia = 'Parcial-01'

 
"""
auxParcial01= dd.sql(consultaSQL).df()

consultaSQL = """
SELECT DISTINCT aux.*,Nota AS Parcial_02
FROM auxParcial01 AS aux 
LEFT OUTER JOIN examen AS e
ON aux.Nombre = e.Nombre AND Instancia = 'Parcial-02'

 
"""
auxParcial02 = dd.sql(consultaSQL).df()

consultaSQL = """
SELECT DISTINCT aux.*,Nota AS Recuperatorio_01
FROM auxParcial02 AS aux 
LEFT OUTER JOIN examen AS e
ON aux.Nombre = e.Nombre AND Instancia = 'Recuperatorio-01'

 
"""
auxRecu01 = dd.sql(consultaSQL).df()

consultaSQL = """
SELECT DISTINCT aux.*,Nota AS Recuperatorio_02
FROM auxRecu01 AS aux 
LEFT OUTER JOIN examen AS e
ON aux.Nombre = e.Nombre AND Instancia = 'Recuperatorio-02'

 
"""
auxRecu02 = dd.sql(consultaSQL).df()




desafio_01 = dd.sql(consultaSQL).df()




#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
                SELECT d.*,
                CASE WHEN ((d.Parcial_01 >= 4 OR d.Recuperatorio_01 >= 4) AND 
                           (d.Parcial_02 >= 4 OR d.Recuperatorio_02 >= 4))
                THEN 'APROBO'
                ELSE 'NO APROBO'
                END AS Estado
                FROM desafio_01 AS d
                 

              """

desafio_02 = dd.sql(consultaSQL).df()
df_nuevo = desafio_02.copy()



#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.


consultaSQL = """
                SELECT Nombre,
                Sexo,
                Edad, 
                'Parcial-01' AS Instancia,
                Parcial_01 AS Nota
                FROM desafio_02

              """
              
aux_parcial01 = dd.sql(consultaSQL).df()

consultaSQL = """
                SELECT Nombre,
                Sexo,
                Edad, 
                'Parcial-02' AS Instancia,
                Parcial_02 AS Nota
                FROM desafio_02

              """
              
aux_parcial02 = dd.sql(consultaSQL).df()

consultaSQL = """
                SELECT Nombre,
                Sexo,
                Edad, 
                'Recuperatorio-01' AS Instancia,
                Recuperatorio_01 AS Nota
                FROM desafio_02

              """
              
aux_recu01 = dd.sql(consultaSQL).df()

consultaSQL = """
                SELECT Nombre,
                Sexo,
                Edad, 
                'Recuperatorio-02' AS Instancia,
                Recuperatorio_02 AS Nota
                FROM desafio_02

              """
              
aux_recu02 = dd.sql(consultaSQL).df()

consultaSQL = """
                SELECT Nombre,
                Sexo,
                Edad, 
                'Parcial-01' AS Instancia,
                Parcial_01 AS Nota
                FROM desafio_02

              """
              
aux_parcial01 = dd.sql(consultaSQL).df()


desafio_03 = dd.sql(consultaSQL).df()
