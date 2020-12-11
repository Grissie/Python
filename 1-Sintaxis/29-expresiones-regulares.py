#-*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:54:24 2020

@author: Gris 
"""

#Libreria para hacer uso de expresiones regulares 
import re

buscar='no'
texto='Este es un texto de ejemplo, el cual no dice nada en concreto. Además sirve para probar el modulo regex de python.'
texto2='Nosotros no somos animales, somos humanos.'

#Buscamos alguna coincidencia en cualquier posicion 
match = re.search(buscar,texto)
print(match)

#Regresa la posicion/indice donde encuentra la coincidencia 
inicio=match.start()
fin=match.end()
print(inicio);print(fin)

print('Buscar: "{}" en \n"{}"\nIndices donde se encontro: \nDe {} a {} ("{}")'
      .format(match.re.pattern, match.string,inicio, fin, texto[inicio:fin]))

#Compilar para buscar el patron

# Precompile the patterns
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')



    
    


    