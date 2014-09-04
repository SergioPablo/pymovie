__author__ = 'Sergio'
#-*- coding: utf-8 -*-
import scipy
from scipy.stats import pearsonr
def correlacion(x,y):
    return pearsonr(x,y)[0]
x = [50,500,1500,2500]
y = [-50,-500,-1500,-2500]

print correlacion(x,y)

usuarios_puntaje = list()
usuarios = open('u.dat')

for linea in usuarios:
    usuarios_puntaje.append(linea.strip().split(' '))
usuarios.close()

