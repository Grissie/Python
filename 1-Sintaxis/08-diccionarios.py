# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:59:48 2020

@author: Gris
"""

#Creacion de un diccionario vacio
x={}
x['1']="Uno"
x['2']="Dos"
x['3']="Tres"
x['4']="Cuatro"
x['5']="Cinco"
print(x)

#Diccionario usa clave:valor 
v={'red':'rojo','green':'verde','blue':'azul'}
print(v)

#Las claves y valores pueden ser de diferente tipo
y={'1':'Uno','flotante':2.34,'complejo':3-4j,'lista':[-5,2,0],'tupla':(1,2,5,6)}
print(y)

#Modificacion a un diccionario
print("Diccionario original: \n",x)
x['White']='Blanco'
x['Cero']=0
print("Diccionario modificado: \n",x)

#Obtener claves o valores del diccionario
claves=x.keys()
print("Calves del diccionario x: \n",claves)
valores=x.values()
print("Valores del diccionario x: \n",valores)

#Obtener pares clave-valor como una lista de tuplas
print(x.items())

#Eliminar un elemento de la lista
print(x)
#Se elimina el par clave-valor de la clave '4'
del(x['4'])
print(x)

#Iterar sobre un diccionario 
for i in x:
    print(i)
    
for i in x:
    print(x[i])
    
for clave,valor in x.items():
    print(clave,valor)