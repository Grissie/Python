# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:58:09 2020

@author: Gris 
"""
import collections 
from collections import Counter

l= [1,1,2,2,2,3,4,5,5,5,5]
print("Lista original \n",l)

#Metodo que cuenta las veces que aparece un elemento, regresa una coleccion
#del tipo elemento:numero de apariciones y los ordena del mayor al menor 
#5:4  2:3  1:2  3:1  4:1
print("Número de incidencias de cada digito \n",Counter(l))

p = "Palabra"
print("Numero de incidendias de cada letra \n",Counter(p))

#Contar palabras de una lista de elementos 
animales = ["perro","perro","perro","gato"]
print("Lista original \n",animales)

#Crear un objeto de Counter 
cuenta=collections.Counter(animales)
print("Veces que aparece un elemento en la lista\n",cuenta)

#Construye un counter vacio y luego se actualiza 
print("\n\n")
counter=collections.Counter()
counter.update('xxxyyyzzzzx')

print(counter)
counter.update({'m':4,'f':6})
print(counter)

#most_common() regresa el elemento mas repetido, si le paso 1 me regresa un valor,
#si le paso 2 me regresa los dos elementos mas repetidos 
print("Elemento que mas se repite \n",counter.most_common(2))

#Obtener una lista de Counter, con todos lo elementos ya sean repetidos 
lista=list(counter.elements())
print("Lista creada a partir de counter() \n",lista)


sagan = 'La ausencia de prueba no es prueba de ausencia'
lista5 = sagan.split()
print("\n\nCadena en formato de texto \n",sagan)
print("Cadena en formato de lista \n",lista5)
cuenta5 = collections.Counter(lista5)
print("Numero de incidencia \n",cuenta5)

for clave, valor in cuenta5.items():
    print(clave,':',valor) 
    # no : 1, ausencia : 2, La : 1, de : 2, es : 1, prueba : 2


