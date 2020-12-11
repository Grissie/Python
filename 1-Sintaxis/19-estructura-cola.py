# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:10:23 2020

@author: Gris
"""

# Eliminar con pop, regresa el ultimo dato de la lista y lo elimina
from collections import deque

#Inicializar cola
cola = deque() 

cola = deque(['German','Daniel,','Torito'])
print(cola)

#Agregar Elemento
cola.append('Maria') #Agregar Elemento
print(cola)

#Elimina el primer elemento de la cola 
cola.popleft()
print(cola)

