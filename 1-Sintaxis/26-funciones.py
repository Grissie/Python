# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:38:05 2020

@author: Gris 
"""

def suma(n):
    """Esta función realiza la suma de números"""
    suma=0
    while(n>0):
        suma+=n
        n-=1
    return suma

def maximoLista(*numeros):
    if not numeros:
        return None
    else:
        numMaximo = numeros[0]
        for n in numeros [1:]:
            if n>numMaximo:
                numMaximo=n
    return numMaximo 

def main():
    y=int(input("Ingrese un número: "))
    print("La suma es %d"%(suma(y)))
    suma.__doc__
    
    print("El número máximo es: %d"%maximoLista(1,8,9,34,128,45,67))
    
main()
