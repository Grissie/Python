# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:15:17 2020

@author: Gris 
"""

def main():
    entero=8
    float=3.15
    cadena="Una cadena"
    print(entero);print(float);print(cadena)
    
    #Asignacion multiple
    a,b,c=45,7.89,"Hola mundo"
    print(a)
    print(b)
    print(c)
    
    #Lista, se puede modificar 
    list=[1.2,-4.5,"Griselda",67]
    print(list)
    
    #Tupla, no se puede modificar 
    tupla=(5,'Nunca',8+4j)
    print(tupla)
    
    #Set, elementos unicos, NO repetidos
    set={5,7,8,'Gris','Pero',7+5j,3.45}
    print(set)
    
    #Diccionario, relacion clave-valor
    diccionario={1:'Uno',2:'Dos'}
    print(diccionario)
    
main()

