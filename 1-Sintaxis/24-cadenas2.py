# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:49:30 2020

@author: Gris 
"""

#Otros metodos para string
cadena="hola Mundo"
print("Cadena original \n",cadena)

print("Cadena en mayuscula \n",cadena.upper())
print("Cadena en minuscula \n",cadena.lower())
print("Primer caracter en mayuscula \n",cadena.capitalize())
print("Copia de la cadena \n",cadena.title())
print("Apariciones de %s en %s: %d vece(s)"%('mundo',cadena,cadena.count('Mundo')))

print("Primera aparicion de %s y su posicion es %d\n"%('Mundo',cadena.find('Mundo')))

saludo = "Hola mundo mundo mundo mundo"
print(saludo)
print("Posicion de la ultima aparicion de %s es: %d"%('mundo',saludo.rfind('mundo')))

#Comprobar si la cadena es un numero 
c='1000'
print(c)
print("La cadena es un numero ? %s"%(c.isdigit()))

#Comprobar si la cadena es alfanumerico 
c='ABC10034p'
print(c)
print("La cadena es un alfanumerico ? %s"%(c.isalnum()))

c3="Hola Mundo en Python"
c4="ESTA ES UNA FRASE EN MAYUSCULA"
c5="esta cadena esta es minuscula"

#comprueba si es mayuscula
print("La cadena es mayuscula? \n",c4.isupper())

#comprueba si es minuscula
print("La cadena es minuscula? \n",c5.islower())

#Comprobar si es un espacio
c4 = " "
print("Este es un espacio? \n",c4.isspace())

#comprobar si empieza con algun caracter
print("'%s' empieza con 'Hola': %s"%(c3,c3.startswith("Hola")))

#comprobar si termina con algun caracter
print("'%s' termina con 'mundo': %s"%(c3,c3.endswith("mundo")))

c6="Esta es una cadena de ejemplo"
#Separar palabra con el metodo SPLIT 
print("\nCadena original \n",c6)
#Devueleve lista con las palabras que forman la cadena original 
#['Esta','es','una','cadena','de','ejemplo']
print("Cadena separada \n",c6.split())  
#Devueleve lista con la posicion: 0,1,2 y 3
print(c6.split()[0:4] ) 

c7 = "Hola,Hola,Hola"
#Separar por comas
print(c7.split(','))


