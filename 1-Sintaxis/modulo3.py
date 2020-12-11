# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:47:54 2020

@author: Gris 
"""


import datetime
import locale #Cambiar idioma

#locale0.setlocale(locale.LC_ALL, 'es')  #codigo de idioma 

dt = datetime.datetime.now()
print("Hora y día actual:",dt) 
print("Año actual:",dt.year)
print("Mes actual:",dt.month)
print("Día actual:",dt.day)
print("Hora actual:",dt.hour)
print("Minuto actual:",dt.minute)
print("Segundo actual:",dt.second)
print("Microsegundos actual:",dt.microsecond)
print("Info:",dt.tzinfo)

print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.year,dt.month,dt.day))

dt.isoformat() #Formato de fecha y hora del ISO

dt.strftime("%A %d %B %Y %I:%M") #formato de 12 horas en ingles
dt.strftime("%A %d de %B del %Y %H:%M") #formato de 24 horas en ingles

t = datetime.timedelta(days = 14, hours =4, seconds = 1000)

dentro_dos_semanas = dt + t

print(dentro_dos_semanas)


#modulo pytz  ---> Zona horaria de todo el mundo