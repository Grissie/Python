# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:41:36 2020

@author: Gris 
"""
#Conjunto vacio
c=set()
c.add(1)
c.add(2)
c.add(3)
print(c)

#Quitamos el elemento con valor de 1 
print("Eliminando al 1")
c.discard(1)
print(c)

#Copiar conjunto
c2=c.copy()
print("Copia \n",c2)

#Limpiamos conjunto
c2.clear() 
print("Limpiando el conjunto c2")
print(c2)


#Comparar conjuntos
#Conjuntos Disyuntos -> Sin nada en comun
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {1,-99}
c4 = {1,2,3,4,5}

c1.isdisjoint(c3) #Son disjuntos el C1 y C2
c1.issubset(c4) #C1 es subconjunto de C4
c4.issuperset(c1) #C4 es un super contenedor de C1

#Uniones, diferencias y conjuntos

c1.union(c2) == c4 #Union de conjunto C1 y C2 es igual al C4

c1.update(c2) #unirlos de verdad

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {1,-99}
c4 = {1,2,3,4,5}

c1.difference(c2)
c1.difference_update(c2) 


#Devuelve un conjunto con elementos comunes
#Intercepcion

c1.intesection(c2)  #Solo nos muesta
c1.intesection_update(c2) #Lo guarda en el c1


#Elementos que no concuerdan entre 2 conjuntos
c1.symmmetric_difference(c2)













