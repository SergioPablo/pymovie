__author__ = 'Sergio'
#-*- coding: utf-8 -*-
import math
import numpy as np
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
    usuarios_pelicula_puntaje.sort()
    usuarios_pelicula_puntaje = np.array(usuarios_pelicula_puntaje)
    return usuarios_pelicula_puntaje

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
            puntaje_de_peliculas.append(i[2])
    puntaje_de_peliculas = map(int,puntaje_de_peliculas)
    lista_nueva = [peliculas_que_vio, puntaje_de_peliculas]
    return lista_nueva

#Esta función un conjunto con las películas que vió
def crear_conjunto_pelicula(lista_usuario):
    return set(lista_usuario[0])

#Esta función crea una lista de las peliculas que vio el usuario a y el usuario b
def crear_lista_intersectada_peliculas(lista_usuario_a, lista_usuario_b):
    conjunto_usuario_a = crear_conjunto_pelicula(lista_usuario_a)
    conjunto_usuario_b = crear_conjunto_pelicula(lista_usuario_b)
    lista_intersectada = list(conjunto_usuario_a&conjunto_usuario_b)
    return lista_intersectada
#Esta función crea una lista con todos los puntajes intersecatados del usuario a y b, para funcionar necesita la lista intersectada
def crear_lista_puntaje_intersectado(lista_peliculas_intersectadas, lista_usuario_a, lista_usuario_b):
    lista_puntaje_usuario_a = list()
    lista_puntaje_usuario_b = list()
    for pelicula in lista_peliculas_intersectadas:
        indice_a = lista_usuario_a[0].index(pelicula)
        lista_puntaje_usuario_a.append(lista_usuario_a[1][indice_a])
        indice_b = lista_usuario_b[0].index(pelicula)
        lista_puntaje_usuario_b.append(lista_usuario_b[1][indice_b])
    lista_nueva = [lista_puntaje_usuario_a, lista_puntaje_usuario_b]
    return lista_nueva


############################### ACÁ TERMINAN LAS FUNCIONES #############################################################
#Empiezo creando la lista de puntaje
lista_puntaje = crear_lista_puntaje('u.dat')

correlacion = -10
usuario_b = ''
usuario_c = ''
usuario = raw_input('Ingrese el id del usuario al cual quiere comparar: ')

lista_usuario_a = puntaje_pelicula('435', lista_puntaje)
lista_usuario_b = puntaje_pelicula('254', lista_puntaje)
lista_de_peliculas_ambos = crear_lista_intersectada_peliculas(lista_usuario_a,lista_usuario_b)
lista_de_puntajes_ambos = crear_lista_puntaje_intersectado(lista_de_peliculas_ambos,lista_usuario_a,lista_usuario_b)

print pearson(lista_de_puntajes_ambos[0],lista_de_puntajes_ambos[1],lista_usuario_a[1],lista_usuario_b[1])



