# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:21:30 2020

@author: Gris 
"""

import sys
#Docstring del documento
""" Modulo de cálculo de área y perímetro de un círculo """ 

PI=3.141516

def areaCirculo(r):
    return PI*r**2

def perimetroCirculo(r):
    return PI*2*r

def imprimeCadena():
    print("Imprimiendo la cadena")
    print(sys.argv)


