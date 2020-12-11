# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:34:37 2020

@author: Gris 
"""

import math
import random 
pi = 3.14159

#Redondear numero
print("Redondeando 3.141516:",round(pi))

#Redondear hacia abajo
print("Redondeando para abajo 3.78:",math.floor(3.78))

#Redondea a la baja
print("Redondeando para abajo 3.98:",math.floor(3.98))


#Redondear hacia arriba
print("Redondeando para arriba 3.56:",math.ceil(3.56))

#Valor Absoluto
print("Valor absoluto de |-10|:",abs(-10))

#Sumatorio
n = [1,2,3]

#Suma los elementos de la lista 
print("Lista n \n",n)
print("Suma de la lista n:",sum(n)) 

print("Suma de la lista n, en flotante:",math.fsum(n))

#Truncar Parte decimal
print(100.121323548)
print("Truncar la parte decimal:",math.trunc(100.121323548))


#Generar numero flotante Aleatorio entre el [0,1)
print("\n\n")
print("Numero aleatorio: ",random.random())

#Genera un numero entre el [1,10)
print("Numero aleatorio: ",random.uniform(1,10))

#Generar numero Entero Aleatorio
print("Numero aleatorio:",random.randrange(10))      #[0,10)
print("Numero aleatorio:",random.randrange(0,101))   #[0,101)
print("Numero aleatorio:",random.randrange(0,101,5)) #[0,101,multiplo de 5)

#Aleaorio de la cadena
c = "Hola Mundo"  
#Obtine una letra aleatoria de la cadena que se le pasa 
print("Letra random de la cadena:",random.choice(c))
  
#Barajear
l=[1,2,3,4,5,6]
print(l)


#Toma 3 elementos de forma aleatoria de la lista que se le pasa 
print(random.sample(l,3))





