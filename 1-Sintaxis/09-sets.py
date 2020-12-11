# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:00:24 2020

@author: Gris
"""

"""
    Conjuntos viene de conjuncion que significa unidos o cercanos
    AND: Uniendo, union logica Y
    OR: Separando, separacion logica O
    
    No almacena elementos repetidos 
"""

#Creacion de un conjunto a partir de una lista
x = set([1,2,3,4]) 
print(x)

#Creacion de un conjunto a partir de una tupla
y = set((1,2,3,4,4))  
print(y)

#Creacion de un conjunto
w={1,2,3,4,'Daniel'}

print("Daniel en w: ",'Daniel' in w)
print("0 no esta en w: ",0 not in w)

#Operaciones con conjuntos
d=set([1,2,3,4])
print("Conjunto original: ",d)
d.add(8)
print("Conjunto Se agrego el elemento 8: ",d)

# Eliminar elementos
d = set([1,2,3,4,9,7])
print("\nConjunto original: ",d)
d.remove(4)
print("Se elimino el 4: ",d)
d.discard(3)
print("Se elimino el 3: ",d)

# Union
uno = set([1,2,3,4])
dos = set([3,4,5,6])
result = uno | dos
print("Uno: ",uno)
print("Dos: ",dos)
print("Union de uno con dos: ",result)

# Interseccion 
uno = set([1,2,3,4])
dos = set([3,4,5,6])
result = uno & dos
print("Uno: ",uno)
print("Dos: ",dos)
print("Interseccion de uno con dos: ",result)

# Diferencia
uno = set([1,2,3,4])
dos = set([3,4,5,6])
result = uno - dos 
print("Uno: ",uno)
print("Dos: ",dos)
print("Diferencia de uno con dos: ",result)

#Convertir una lista a un conjunto y luego a una lista
l=[1,2,3,3,4,4,4,5,6,6,6]
l=list(set(l))
print("\n",l)




