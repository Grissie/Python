# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:58:43 2020

@author: Gris 
"""
#Modulo para crear, eliminar, listas carpetas de mi sistema operativo 
#Para el manejo de rutas de mi sistema operativo 
import os
from os import remove 

def menu():
    print("\n\n----- Administración de archivos -----"
          +"\n1. Crear un archivo y escribir en el"
          +"\n2. Sobreescribir en un archivo"
          +"\n3. Leer contenido de un archivo"
          +"\n4. Eliminar archivo"
          +"\n5. Salir")
    
def crearArchivo():
    nombre=input("Nombre del archivo: ")
    archivo=open(nombre,'w')
    texto=input("Contenido del archivo: ")
    archivo.write(texto)
    archivo.close()
    
def sobreescribirArchivo():
    nombre=input("Nombre del archivo: ")
    archivo=open(nombre,'a')
    cadena=input("Cadena a agregar: ")
    archivo.write("\n"+cadena)
    archivo.close()
    
def leerArchivo():
    try:
        nombre=input("Nombre del archivo: ")
        with open(nombre,'r') as archivo:
            contenido=archivo.read()
            print("\nContenido del archivo '%s': \n%s"%(nombre,contenido))
        #for linea in archivo:
        #   print(linea)
        #linea=archivo.readline()
        #while linea!='':
        #    print(linea, end='')
        #    linea=archivo.readline()
        archivo.close()
    except OSError as error:
        print("OS error: {0}".format(error))
        
def eliminarArchivo():
    try:
        nombre=input("Archivo a eliminar: ")
        remove(nombre)
        print("Se elimino el archivo %s\n"%nombre)
    except OSError as error:
        print("OS error: {0}".format(error))
        
def main():
    try:
        menu()
        opcion=int(input("Elija una opción: "))
        while True:
            if opcion==1:
                #Crea el archivo y escribe sobre el 
                crearArchivo()
                menu()
                opcion=int(input("Elija una opción: "))
            elif opcion==2:
                #Sobreescribe en un archivo existente, si no existe lo crea 
                sobreescribirArchivo()
                menu()
                opcion=int(input("Elija una opción: "))
            elif opcion==3:
                #Abre un archivo existente y lee su contenido 
                leerArchivo()
                menu()
                opcion=int(input("Elija una opción: "))
            elif opcion==4:
                #Elimina un archivo 
                eliminarArchivo()
                menu()
                opcion=int(input("Elija una opción: "))
            elif opcion==5:
                print("Saliendo !")
                break
            elif opcion>=6 or opcion <=0:
                print("Elija una opción válida")
                menu()
                opcion=int(input("Elija una opción: "))
    except ValueError:
        print("La entrada es incorrecta: escribe un número entero !")
        menu()
        os.system()
        opcion=int(input("Elija una opción:"))
        
        
main()

#Nos situa en la posicion que le pasamos como parametro 
#fichero.seek(10)
