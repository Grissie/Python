# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:30:22 2020

@author: Gris
"""

def main():
    #Cadena original 
    x="Hola mundo en Python"
    print(x)
    
    #Metodo split regresa una lista de subcadenas de la cadena original
    #['Hola', 'mundo', 'en', 'Python']
    x_copia=x.split()
    print(x_copia)
    
    #Separa la cadena principal en subcadenas, cuando encuentra la letra a
    y="Hola-Mundo-Otra-Palabra"
    z=y.split('a')
    print(y)
    print(z)
    
    #Metodo join, junta las cadenas con el operador que se le pasa 
    cadena='-'.join(['Junta','las','palabras'])
    print(cadena)
    
    #Convertir cadenas a numeros
    num1=int("12")
    num2=float("3.45")
    print(num1);print(num2)
    
    #Metodo find, sirve para buscar una subcadena y regresa la posicion
    cadena_larga="Este es un enunciado algo largo, pero necesario"
    print(cadena_larga)
    print('Posicion donde inicia "pe":',cadena_larga.find('pe'))
    
    #Metodo startsWith, endsWith, realizan una busqueda al inicio y al final de la 
    #cadena, respectivamente y devuelven un valor booleano
    print(cadena_larga.startswith("te"))
    print(x.endswith("ne"))

    # Buscar varias cadenas si se pasan como tupla
    print(cadena_larga.endswith(("es", "nun", "l")))

    # Conviertiendo objetos a cadenas
    # El metodo repr regresa la representacion en cadena de casi cualquier objeto de Python
    XX = [1, 2, 3]
    print("La lista XX es: " + repr(XX))
    XX = (1,2,3)
    print("La tupla XX es: " + repr(XX))
    print(repr(len))

    # Formateando cadenas 
    # El operador % se utiliza para combinar valores con cadenas
    # El operador % (el del centro) requiere cadena <--> tupla
    print("\nEl %s es la %s tradicional %s" % ("tequila", "bebida", "mexicana") )

    # Secuencias de formato 
    # Enteros -> %d
    # Flotante -> %f
    # Cadenas -> %s
    # Tambien tenemos el metdo format
    print("El {0} es la {1} tradicional {2}".format("tequila", "bebida", "mexicana"))
    print("El {bebida} es la {palabra} tradicional {pais}".format(bebida="tequila", palabra="bebida", pais="mexicana"))

    #Metodo de Slicing Consiste es partir alguna cadena utilizando sus indices
    cadena3="Esta es otra cadena"
    print("\n\nCadena 3: ",cadena3)
    print(cadena3[:])
    print(cadena3[1:6])
    print(cadena3[4:-1])
    print(cadena3[1:5]+cadena3[7:-1])
    
    nueva="Esta es otra palabra"+cadena3[4:-1]
    print(nueva)
    
    
    
    
    

main()