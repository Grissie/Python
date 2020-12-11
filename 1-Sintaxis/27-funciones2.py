# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:44:02 2020

@author: Griselda 
"""

def presentacion():
    nombre=input("Ingrese su nombre:")
    edad=int(input("Ingrese su edad:"))
    peso=float(input("Ingrese su peso:"))
    print("\nMi nombre es %s, tengo %d años y peso %.2f Kg\n\n"%(nombre,edad,peso))
    
def suma():
    x=float(input("Primer número:"))
    y=float(input("Segundo número:"))
    print("%.2f + %.2f = %.2f\n\n"%(x,y,x+y))

def main():
    print("Elija una opción")
    print("1. Presentación \n2.Suma \n3.Salir\n\n")
    opcion=int(input("Opción:"))
    
    while True:
        if opcion==1:
            presentacion()
            print("Elija una opción")
            print("1. Presentación \n2.Suma \n3.Salir")
            opcion=int(input("Opción:"))
        elif opcion==2:
            suma()
            print("Elija una opción")
            print("1. Presentación \n2.Suma \n3.Salir")
            opcion=int(input("Opción:"))
        elif opcion==3:
            print("Vuelva pronto!")
            break
        elif opcion>=4 or opcion<=0:
            print("Ingrese una opción válida")
            print("1. Presentación \n2.Suma \n3.Salir")
            opcion=int(input("Opción:"))
       
main()

