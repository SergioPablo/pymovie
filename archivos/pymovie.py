__author__ = 'Sergio'
#-*- coding: utf-8 -*-
import math

#Esta función calculará el promedio de una lista
def promedio(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

#Para usar la correlación de pearson hacen falta 4 variables en este caso.
#La primera es una lista con los puntajes INTERSECTADOS y ORDENADOS que el usuario "x" le dio a las peliculas.
#La primera es una lista con los puntajes INTERSECTADOS y ORDENADOS que el usuario "y" le dio a las peliculas.
#La tercera es una lista con TODOS LOS PUNTAJES que dió el usuario "x" no importando su orden
#La tercera es una lista con TODOS LOS PUNTAJES que dió el usuario "y" no importando su orden
#Ej:
#  usuario  pelicula_1  pelicula_2  pelicula_3  pelicula_4
#     x         5           3           2           ???
#     y         2           1          ???           2
# Según el esquema anterior la función se usaria de la siguiente manera:
# pearson([5,3],[2,1],[5,3,2],[2,1,2])
def pearson(x, y, puntajes_x, puntajes_y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - promedio(puntajes_x)
        ydiff = y[idx] - promedio(puntajes_y)
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


# Este archivo crea una lista ordenada con todos los puntajes de las peliculas con
# [usuario, pelicula, puntaje]
def crear_lista_puntaje(archivo):
    usuarios_pelicula_puntaje = list()
    usuarios = open(archivo)

    for linea in usuarios:
        usuarios_pelicula_puntaje.append(linea.strip().split(' '))
    usuarios.close()
    return usuarios_pelicula_puntaje.sort()





#Esta definición retornará 2 listas, la primera es con el ID de las películas que vió y la segunda con el puntaje respectivo.
#Ej:
# [pelicula_1, pelicula_2, pelicula_3...]
# [puntaje_1, puntaje_2 .......]
# Esto tiene el objetivo de saber que puntaje tiene cada película... ¿Por qué? Porque la pelicula en la lista estará en la misma posición que su respectivo puntaje en la otra lista
def puntaje_pelicula(usuario, lista_puntaje):
    peliculas_que_vio = list()
    puntaje_de_peliculas = list()
    for i in lista_puntaje:
        if i[0] == usuario:
            peliculas_que_vio.append(i[1])
            puntaje_pelicula.append(i[2])
    return peliculas_que_vio, puntaje_de_peliculas