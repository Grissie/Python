# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:10:56 2020

@author: Gris
"""

#Eliminar con pop, regresa el ultimo dato de la lista y lo elimina
x = [4, 2, 3, 4, 5, 4, 7, 8, 9, 10]
print(x)
x.append(11)
print(x)

#Elimina el ultimo dato, en este caso el 10 y lo regresa
valor = x.pop() 
print(valor) 
print(x)


