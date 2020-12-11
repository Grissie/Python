# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:21:30 2020

@author: Gris
"""

def main():
    #Creacion de una tupla
    tupla=("a","b","c")
    lista=[1,2,3,4,5]
    print(tupla)
    
    #No se puede modificar una tupla, puede tener elementos repetidos 
    #tupla[0]="z"
    
    #Operador +
    y=tupla+tupla
    print(y)
    
    #Operador 
    z=tupla*4
    print(z)
    
    #Copiae tupla
    copia=tupla[:]
    print("Copia de la tupla: \n",copia)
    
    # Conversion entre listas y tuplas 
    x = list((1, 2, 3, 4))
    print(type(x))
    
    x = tuple([1, 2, 3, 4])
    print(type(x))
    
    # Nota
    x = list("Hola")
    print(x)

    # Desempaque 
    # Se genera una tupla a partir de los elementos
    x = (1, 2, 3, 4, 5)
    a, b, c, d, e = x
    print(b) 

    # Empacar 
    # Se genera una tupla a partir de los elementos
    a = 1, 2, 3
    print(a) 
    
main()