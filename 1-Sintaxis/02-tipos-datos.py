# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:00:17 2020

@author: Gris
"""
def main():
    x=None
    y=5*2+4-3*8
    z=5/2.0
    w="Esto es una cadena"
    d='Esta es un dicho "Más vale pájaro en mano, que cientos volando"'
    a="""Esto también es una cadena"""
    entrada=input("Ingrese su nombre: ")
    
    print("Tipo de dato de x: ",type(x))
    print("El resultado de y: ",y)
    print("El resultado de z: ",z)
    print('\n')
    print(w)
    print(d)
    print(a)
    print(w+' '+a)
    print(w*4)
    print("Hola %s"%entrada)

main()


