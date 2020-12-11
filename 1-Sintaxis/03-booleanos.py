# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:14:16 2020

@author: Gris 
"""
#False: [],{},0,0.0,0+0j,"",(),None
def main():
    a=bool([1,2,3])
    if(a == True):
        print("Soy verdadero !")
    else:
        print("Soy falso !")
    
    #Operadores logicos AND=y OR=o not=no
    print(True and True)
    print(True and False)
    print(True or False)
    print(False or False)
    print(not True)
    print("\n")
    
    #El operador not se evalúa antes que el operador and
    print(not (True and False))
    #El operador not se evalúa antes que el operador or
    print(not (False or True))
    #El operador and se evalúa antes que el operador or
    print(False and (True or True))
    print("\n")
    
    #Comapracion entre booleanos 
    print(True>False)
    print(False>True)
    print(not True == False)
    
    #Operadores de comparacion
    # > Mayor que
    # < Menor que
    # >= Mayor o igual que
    # <= Menor o igual que
    # == Igual que 
    # != Distinto de 
    print()
    x = 20
    y = 15
    z = 20
    print(x > y)
    print(x < y)
    print(x == z)
    print(x != z)
  
            
main()
