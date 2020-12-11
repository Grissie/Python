# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:31:48 2020

@author: Gris
"""
def saludo():
    c="Hola desde la funcion"
    print(c)
    
saludo()

#Funciones que reciben y retornan valores
def suma(a,b):
	return a+b

print("%d + %d = %d"%(5,10,suma(5,10)))

#Factorial de un numero
def factorial(x):
	#print("Valor Inicial ->",x)
	if x > 1:
		x = x * factorial(x-1)
	return x

print("Factorial de %d: %d"%(5,factorial(5)))

#Iterativo de un factorial 
def factorial(num):
	fact=1
	for x in range(1,num+1):
		fact*=x
	return fact

print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(6))
print(factorial(2))

#Recursivo de un factorial
def factorialRec(num):
	if num==0 or num==1:
		return 1
	else:
		return num*factorialRec(num-1)
print(factorialRec(1))
print(factorialRec(3))
print(factorialRec(6))


#Fibonacci iterativo
print("----------------------------")
def fibo(n):
	a,b=1,1
	print(a,b)
	for i in range(n-1):
		a,b=b,a+b
		print(b)
	return a

elemento= fibo(30)
print("El elemento 30 es: ",elemento)

#Fibonacci recursivo
def fiboRec(n):
	if n==1 or n==2:
		return 1
	return fiboRec(n-1)+fiboRec(n-2)
