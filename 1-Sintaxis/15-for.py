# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:38:38 2020

@author: Gris 
"""

#For itera sobre una lista,cadena,tupla o diccionario

lista=[1,2,6,-7,-3,2,0]
cadena="Esta es una cadena"
tupla=(1,2,3,4,5)
diccionario={1:'Uno',2:'Dos',3:'Tres',4:'Cuatro',5:'Cinco'}

print("Imprimiendo la lista")
for i in lista:
    print(i)
    
print("\nImprimiendo la cadena")
for letra in cadena:
    print(letra)
    
print("\nImprimiendo la tupla")
for i in tupla:
    print(i)
    
print("\nImprimiendo el diccionario")
coleccion=diccionario.items()
for i in coleccion:
    print(i)
    

"""
programa que imprime el conteido de una lista
"""
cont = 0
nombres=['Juan','Paco','Pablo','Brayan','Kevin','Rosa']
for n in nombres:
	print(n)
	cont+=1
print('total = ',cont) 

print()
#Funcion range, inicia en 0 y termina en n-1, en este caso va del [0,4]
for i in range(5):
    print(i)
    
#Abarca del 10 al 39 
print("Numeros pares:")
for i in range(10,40):
    if(i%2==0):
        print(i)
        
#Tercer parametro nos indica el incremento entre cada elemento
print("")
for i in range(10,40,4):
    print(i)
    
    
    
    
    

    
    