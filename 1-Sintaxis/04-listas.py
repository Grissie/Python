# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:26:59 2020

@author: Gris
"""

def main():
    #Definicion de una lista 
    enteros=[1,4,5,-7,8,-9]
    flotantes=[-5.6,8.9,4.5,-3.4]
    varios=['Hola','Mundo',56,-7.8,4+3j,[5,-7.8,4.5,2]]
    
    print("Lista de enteros:\n",enteros)
    print("Lista de floantes:\n",flotantes)
    print("Lista de varios:\n",varios)
    
    print("\n")
    #Longitud de una lista
    print("Tamaño de la lista enteros: ",len(enteros))
    
    #Indices de listas
    #Devuelve el primer elemento de la lista enteros 
    print("\nPrimer elemento de la lista enteros:",enteros[0])
    #Devuelve el ultimo elemento de la lista enteros
    print("Ultimo elemento de la lista enteros:",enteros[-1])  
    
    #Listas internas
    #Devuelve el elemento tres de la lista interna del elemento seis
    print(varios[5][2]) 
    
    #Copiar listas
    #Solo abarca del elemento 0 al elemento 2
    copia=enteros[0:3] 
    print("Copia de la lista enteros: \n",copia)
    
    #Modificacion
    flotantes[-1]=-5.6
    print("\nLista de flotantes modificada: \n",flotantes)
    
    #Agregar elemento
    varios.append(5 +8j)
    print("Agrego un nuevo elemento en la lista varios: \n",varios)
    
    #Agregar una lista dentro de otra
    z=[-4,6.7,5,-3]
    enteros.append(z)
    print("\nSe agrega una lista como elemento de otra: \n",enteros)
    
    #Agregar elemento en una posicion especifica
    varios.insert(1,'País de nunca jámas')
    print("Inserta elemento en la posición 1 de varios: \n",varios)
    
    #Concatenar una lista a otra
    w=[-7,6.7,-9,3,4.5]
    enteros.extend(w)
    print("\nConcatena una lista con otra: \n",w)
    
    #Buscar el indice de un elemento especifico
    print("Lista de enteros: \n",enteros)
    print("Indice del digito -9: ",enteros.index(-9))
    
    #Otra forma de concatenar listas
    a=[-4,7.6,5,2.3,-8.0]
    b=[-7,9.0,2.3,5]
    lista=a+b
    print("Otra forma de concatenar listas: \n",lista)
    
    #Eliminar datos
    #Elimina el ultimo elemento de la lista enteros
    print("Lista de enteros:\n",enteros)
    del(enteros[-1])
    print("Elimina el último elemento de la lista de enteros: \n",enteros)
    #Elimina los elementos del 0 al 4 de la lista enteros
    del(enteros[0:5])
    print("Elimina los elementos del 0 al 4: \n",enteros)
    
    #Eliminar con remove
    #Elimina la primer coincidencia que le pasamos como parametro
    enteros.remove(-9)
    print(enteros)
    print("Se elimino el primer -9: \n",enteros)
    
    #Pop elimina el ultimo elemento de una lista y lo devuelve
    print("\nLista de flotantes: \n",flotantes)
    valor=flotantes.pop()
    print(flotantes)
    print("Se elimino: ",valor)
    
    #Invertir una lista
    print("Lista flotante original: \n",flotantes)
    flotantes.reverse()
    print("Lista flotantes al reves: \n",flotantes)
    
    #Ordenar una lista, debe ser del mismo tipo 
    print("Lista original: \n",flotantes)
    flotantes.sort()
    print("Lista ordenada: \n",flotantes)
    
    #Copia de una lista
    copia_enteros=enteros[:]
    print("Copia de la lista enteros: \n",copia_enteros)
    
    #Pertenencia
    numeros=[89,56,23,-14,-32,45,12]
    print("Lista de numeros: \n",numeros)
    print("89 esta en numeros: ",89 in numeros)
    print("56 no esta en numeros: ",56 not in numeros)
    print("Máximo: ",max(numeros))
    print("Mínimo: ",min(numeros))
    
    #Contar incidencias de una lista
    numeros2=[-5,7,8,9,-2,0,-23,0,23,0,0]
    print("El numero 0 aparece: ",numeros2.count(0))
    
main()


