# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:24:53 2020

@author: Gris 
"""
#Una excepcion nos ayuda a cachar un error en tiempo de ejecucion 
while(True):
    #Intenta ejecutar este codigo
	try:
		n = float(input("Introduce un numero:"))
		m = 4.0
		print("{}/{}={}".format(n,m,n/m))
    #Si en el try hay una excepcion, ejecuta esto
	except:
		print("Ha ocurrido un error")
	else:
		print("Todo ha funcionado correctamente")
		break
    #Haya excepcion o no, se ejecuta esto 
	finally:
		print("Fin de la excepcion")
        
        
#Otra excepcion es raise 
def miFuncion(algo):
	if algo is None:
		raise ValueError("Error ! No se permite un valor Nulo")
cad="Hola"
miFuncion(cad)


#Multiples Excepciones
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )
