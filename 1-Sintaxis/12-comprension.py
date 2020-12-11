# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:30:35 2020

@author: Gris 
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = []

#Se usa el ciclo for para copiar una lista 
for x in lista1:
	lista2.append(x+1)
print("Lista 1: \n",lista1)
print("Lista 2: \n",lista2)


lista3 = [5, 2, 1, 7, 8]
lista4 = [x+1 for x in lista3]
print("Lista 3: \n",lista3)
print("Lista 4: \n",lista4)

lista5 = range(10)

lista6 = [x+2 for x in lista5 if x%2==0]
print("Lista 5: \n",lista5)
print("Lista 6: \n",lista6)

#Sintaxis general para listas por comprensión
# listaNueva = [<expr1> for var in listaVieja if <expr2>]

#Diccionario por comprension
diccionario1 = {}
lista = [1, 2, 3, 4]

#Sitaxis general para diccionarios por comprensión
#diccionarioNuevo = {<expr1>:<expr2> for var in lista if <expr3>}

diccionario1 = {x:x+1 for x in lista}

diccionario = {1:"Rodrigo", 2:"Luis", 3:"Pedro"}

listavalores = ["Rod", "Luis", "Pedro"]
listaclaves = [1,2,3]

diccionarioNuevo = {listaclaves[x]: listavalores[x] for x in range(len(listaclaves))}

print(diccionarioNuevo)

