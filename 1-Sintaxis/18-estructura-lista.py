# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:09:57 2020

@author: Gris 
"""

enteros=[1,2,3,4,5,6,7,8,9,10]
cadenas=['Guayaba','Sandía','Melón','Manzana','Platano','Naranja']
varios=[1,-4,'Lunes',90,2.34,5-4j,'Martes','Mandarina',[-5,6,0,-3]]

print("Lista de enteros \n",enteros)
print("Tamaño de la lista: %d"%(len(enteros)))

print("\nLista de cadenas\n",cadenas)
print("Tamaño de la lista: %d"%(len(cadenas)))

print("\nLista de varios \n",varios)
print("Tamño de la lista: %d"%(len(varios)))

#Indices
print("Ultimo elemento de la lista enteros: %d"%(enteros[-1]))
print("Elemento %d de la lista: %d"%(4,enteros[4]))

#Subindices
print("Primer elemento de la sublista de varios: %d"%(varios[8][0]))
print("Ultimo elemento de la sublista de varios: %d"%(varios[8][-1]))

#Slicing
original=['Dato1','Dato2','Dato3','Dato4','Dato5','Dato6']
#Copia los elementos de la posicion 0 al 3
copia=original[0:4]
#Otra copia 
copia2=original[3:-1]
print("\nLista original \n",original)
print("Lista copia \n",copia)
print("Lista copia2 \n",copia2)

#Modificar lista
#Accede al indice 3 de la lista original y se cambia el valor 
print("\nLista original \n",original)
original[3]='Dato10'
print("Lista modificada \n",original)

#Agregar elemento
original.append('Dato34')
print("Se agrego elemento nuevo \n",original)

#Agregar un elemento en una posicion determinada
print("\nLista original \n",original)
original.insert(1,'Dato120')
print("Lista modificada \n",original)

#Agregar una lista como elemento de otra
lista1=[1,2,3,4,5]
lista2=[-4,5,6,7]
print("\nLista 1 \n",lista1)
print("Lista 2 \n",lista2)
lista2.append(lista1)
print("Agregando la lista1 a la lista2 \n",lista2)

#Concatenando listas
lista3=[-4,5,0,-2,3]
print("Lista3 \n",lista3)
print("Lista2 \n",lista2)
#Otra forma es: lista3 + lista2
lista3.extend(lista2)
print("Concatenando lista3 con la lista2 \n",lista3)

#Eliminar datos
print("\nNueva lista")
x = [1, 2, 3, 4, 5, 6, 7, 8]
#Elimina el dato 2 que se encuentra en el indice 5
print(x)
print("Eliminando %d"%(x[5]))
del(x[5])
print(x)
#Elimina los datos desde el indice 0 al indice 1
print("Eliminando %d, %d"%(x[0],x[1]))
del(x[:2]) 
print(x)
#Elimina los datos desde el indice 2 hasta el final
print("Eliminando %d, %d, %d"%(x[2],x[3],x[4]))
del(x[2:]) 
print(x)

#Eliminar con remove
print("\nOtra lista")
x = [1, 2, 2, 2, 5, 6, 7, 8] 
print(x)
#Elimina la primera coincidencia del valor dado
x.remove(2) 
print(x)

#Eliminar con pop, regresa el ultimo dato de la lista y lo elimina
x = [4, 2, 3, 4, 5, 4, 7, 8, 9, 10]
print("Otra lista mas \n",x)
#Elimina el ultimo dato, en este caso el 10 y lo regresa
valor = x.pop() 
print("Se elimino el valor %d"%(valor)) 
print(x)

#Invertir lista
print("\nLista x \n",x)
x.reverse()
print("Lista al reves \n",x)

#Ordenar lista
x.sort()
print("Lista ordenada \n",x)

#Copiar lista
copia=x[:]
print("Lista copia \n",copia)

#Pertenencia
print("\n%d pertence a %s: %s"%(7,'x',7 in x))

#Maximo
print("%d es maximo de %s"%(max(x),'x'))

#Minimo
print("%d es minimo de %s"%(min(x),'x'))

#Busca el indice
print("El indice del elemento %d es: %d"%(7,x.index(7)))

## Numero de apariciones de un dato
print("El numero 4 aparece: %d veces"%(x.count(4)))

# Inicializar listas con operador * 
x = [None] * 4
y = [1, 2] * 3
print(x)
print(y)




