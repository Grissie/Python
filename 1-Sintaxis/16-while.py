# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:43:37 2020

@author: Gris
"""
#Imprime los digitos del 0 al 9
x=0
while(x<10):
    print(x)
    x += 1
   
#Calculadora menu
while True:
	print('Selecciona la operación\n')
	print('1) suma')
	print('2) resta')
	print('3) multiplicación')
	print('4) división')
	print('5) salir')

	opcion = int(input())

	if opcion ==5:
		break
	if (opcion >5 or opcion< 1):
		print('error, igrese un numero del 1 al 5')
	else:
		print('ingrese el operando1')
		op1 = float(input())
		print('ingrese el operando1')
		op2 = float(input())
	if opcion ==1:
		print(op1+op2,'\n')
	elif opcion ==2:
		print(op1-op2,'\n')
	elif opcion ==3:
		print(op1*op2,'\n')
	elif opcion ==4:
		print(op1/op2,'\n')                                    