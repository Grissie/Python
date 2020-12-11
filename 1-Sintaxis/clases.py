# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:06:22 2020

@author: gray_
"""
#Definicion de la clase
class Complejo:
    """ Clase que simula un numero complejo """
    
    def __init__(self,p_real,p_imaginaria):
        self.real=p_real
        self.imag=p_imaginaria
        
    def muestra(self,mensaje):
        print("Hola "+mensaje)
        
    def muestraComplejo(self):
        print("Numero completo: (%s,%s)"%(str(x.real),str(x.imag)))
        
#Creacion de objeto
x=Complejo(3,5)
cadena=input("Frase:")
#Uso del metodo 
x.muestra(cadena)
print("Numero completo: (%s,%s)"%(str(x.real),str(x.imag)))
print()
x.muestraComplejo()
