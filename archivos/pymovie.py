#-*- coding: utf-8 -*-
import math
import numpy as np

#Esta función calculará el promedio de una lista
def promedio(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

#Para usar la correlación de pearson hacen falta 4 variables en este caso.
#La primera es una lista con los puntajes INTERSECTADOS y ORDENADOS que el usuario "x" le dio a las peliculas.
#La segunda es una lista con los puntajes INTERSECTADOS y ORDENADOS que el usuario "y" le dio a las peliculas.
#La tercera es una lista con TODOS LOS PUNTAJES que dió el usuario "x" no importando su orden
#La cuarta  es una lista con TODOS LOS PUNTAJES que dió el usuario "y" no importando su orden
#Ej:
#  usuario  pelicula_1  pelicula_2  pelicula_3  pelicula_4
#     x         5           3           2           ???
#     y         2           1          ???           2
# Según el esquema anterior la función se usaria de la siguiente manera:
# pearson([5,3],[2,1],[5,3,2],[2,1,2])
def pearson(x, y, puntajes_x, puntajes_y):
    assert len(x) == len(y) #Verifico que las listas son iguales
    n = len(x)
    if n > 0:
        diffprod = 0
        xdiff2 = 0
        ydiff2 = 0
        for idx in range(n):
            xdiff = x[idx] - promedio(puntajes_x)
            ydiff = y[idx] - promedio(puntajes_y)
            diffprod += xdiff * ydiff
            xdiff2 += xdiff * xdiff
            ydiff2 += ydiff * ydiff
            if math.sqrt(xdiff2 * ydiff2) == 0:
                return 0

        return diffprod / math.sqrt(xdiff2 * ydiff2)
    else:
        return 0


# Esta función crea una lista ordenada a partir de un archivo con todos los puntajes de las peliculas con las variables
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
# [[pelicula_1, pelicula_2, pelicula_3.....],
# [puntaje_1, puntaje_2 , puntaje_3.......]]
# Esto tiene el objetivo de saber que puntaje tiene cada película... ¿Por qué? Porque la pelicula en la lista estará en la misma posición que su respectivo puntaje en la otra lista
def lista_usuario(usuario):
    peliculas_que_vio = list()
    puntaje_de_peliculas = list()
    for i in lista_puntaje:
        if i[0] == usuario:
            peliculas_que_vio.append(i[1])
            puntaje_de_peliculas.append(i[2])
    puntaje_de_peliculas = map(int,puntaje_de_peliculas)
    lista_nueva = [peliculas_que_vio, puntaje_de_peliculas]
    return lista_nueva

#Esta función crea a partir de una lista de usuario un conjunto con las películas que dicho usuario vió
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
    return lista_puntaje_usuario_a, lista_puntaje_usuario_b

def comparar_usuarios(usuario):
    lista_usuario_comarar = lista_usuario(usuario)
    lista_de_peliculas_ambos = crear_lista_intersectada_peliculas(lista_usuario_a,lista_usuario_comarar)
    lista_ptje_a, lista_ptje_b = crear_lista_puntaje_intersectado(lista_de_peliculas_ambos,lista_usuario_a,lista_usuario_comarar)
    return pearson(lista_ptje_a, lista_ptje_b, lista_usuario_a[1],lista_usuario_comarar[1])


def crear_conjunto_peliculas_no_vistas():
    conjunto_a = crear_conjunto_pelicula(lista_usuario_a)
    conjunto_b = crear_conjunto_pelicula(lista_usuario_b)
    conjunto_c = crear_conjunto_pelicula(lista_usuario_c)
    #Al restar conjuntos en este caso se refiere a las peliculas que han visto A y B pero NO ha visto A
    conjunto_peliculas_no_vistas_b = conjunto_b-conjunto_a
    conjunto_peliculas_no_vistas_c = conjunto_c-conjunto_a
    conjunto_intersectado = conjunto_peliculas_no_vistas_b & conjunto_peliculas_no_vistas_c
    lista_restricciones.append(usuario_correlacion_b)
    lista_restricciones.append(usuario_correlacion_c)
    return conjunto_intersectado


def crear_lista_peliculas(archivo_peliculas):
    archivo = open(archivo_peliculas)
    lista_peliculas = list()
    for linea in archivo:
        pelicula = linea.strip().split('(19')[0]
        id = [int(s) for s in pelicula.split() if s.isdigit()]
        nombre= pelicula.split(str(id[0]))[1]
        agregar = [str(id[0]), nombre]
        lista_peliculas.append(agregar)
    lista_peliculas.sort()
    lista_peliculas = np.array(lista_peliculas)
    return lista_peliculas


############################### ACÁ TERMINAN LAS FUNCIONES #############################################################
#PARÁMETROS OBLIGATORIOS
lista_pelis = crear_lista_peliculas('movies.dat')
lista_puntaje = crear_lista_puntaje('u.dat')
usuario = raw_input('Ingrese id del usuario: ')
rango = int(raw_input('Ingrese el rango de usuarios para comparar: '))
puntaje_minimo = float(raw_input('Ingresa el puntaje minimo, ten en cuenta que entre más puntaje, más puede ser la demora : '))
lista_usuario_a = lista_usuario(usuario)

# A Continuación se buscará el primer usuario más parecido

lista_usuario_b = 0
correlacion_b = 0
usuario_correlacion_b= ''
lista_usuario_c = 0
correlacion_c = 0
usuario_correlacion_c= ''
lista_restricciones = list()

conjunto_intersectado = set('1')
id_mejor_pelicula = ''
mejor_puntaje = 0
print 'Lista usuario principal: ' + str(lista_usuario_a)
print 'Buscando... \n'
while mejor_puntaje <= puntaje_minimo:
    correlacion_b = 0
    correlacion_c = 0
    for i in range(1, rango):
        if str(i) != usuario and str(i) not in lista_restricciones:
            if correlacion_b != 1:
                corr = comparar_usuarios(str(i))
                if corr > correlacion_b:
                    correlacion_b = corr
                    usuario_correlacion_b = str(i)
                    lista_usuario_b = lista_usuario(str(i))
            else:
                break

    # Se buscará el segundo jugador más parecido

    for i in range(1, rango):
        if str(i) != usuario and str(i) != usuario_correlacion_b and str(i) not in lista_restricciones:
            if correlacion_c != 1:
                corr = comparar_usuarios(str(i))
                if corr > correlacion_c:
                    correlacion_c = corr
                    usuario_correlacion_c = str(i)
                    lista_usuario_c = lista_usuario(str(i))
            else:
                break

    conjunto_intersectado = crear_conjunto_peliculas_no_vistas()


    for pelicula in conjunto_intersectado:
        puntaje_b = lista_usuario_b[1][lista_usuario_b[0].index(pelicula)]
        puntaje_c = lista_usuario_c[1][lista_usuario_c[0].index(pelicula)]
        puntaje_ponderado = (puntaje_b * correlacion_b + puntaje_c * correlacion_c)/(correlacion_b+correlacion_c)
        if puntaje_ponderado > mejor_puntaje:
            id_mejor_pelicula = pelicula
            mejor_puntaje = puntaje_ponderado



    nombre_mejor_pelicula = ''
    for pelicula in lista_pelis:
        if id_mejor_pelicula == pelicula[0]:
            nombre_mejor_pelicula = pelicula[1]
            break


print 'Este es el conjunto de peliculas que el usuario no ha visto, pero que A y B sí han visto: ' + str(conjunto_intersectado)
print 'Usuario A: ' + str(usuario_correlacion_b), 'Correlacion: ' + str(correlacion_b)
print 'Lista A: ' + str(lista_usuario_b)
print 'Usuario B: ' + str(usuario_correlacion_c), 'Correlacion: ' + str(correlacion_c)
print 'Lista B: ' + str(lista_usuario_c)
print 'La mejor película recomendada para este usuario es: ' + nombre_mejor_pelicula + 'con un puntaje de: ' + str(round(mejor_puntaje,1))



# Probar con usuario 200 y Rango 800
