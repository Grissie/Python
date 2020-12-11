# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:23:26 2020

@author: Gris 
"""

#Se agrega el modulo predefinido 
import modulo1
import os 

y = float(input("Radio: "))
print("Radio del círculo: %.2f [u]"%(y))
print("Área del círculo %.2f [u^2]"%modulo1.areaCirculo(y))
print("Perímetro del círculo: %.2f [u]"%(modulo1.perimetroCirculo(y)))

print()
print("Directorio actual %s"%os.getcwd())
print("Directorio actual %s"%os.listdir(os.curdir))

modulo1.imprimeCadena()

