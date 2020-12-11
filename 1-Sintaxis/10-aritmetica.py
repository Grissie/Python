3# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:09:14 2020

@author: Gris 
"""

print("%d + %d = %d"%(2,3,2+3))

print("%.2f - %.2f = %.2f"%(5.78,3.45,5.78-3.45))

print("%d * %.2f = %.2f"%(5,2.34,5*2.34))

print("%d ** %d = %d"%(5,2,5**2))

print("%d / %d = %.2f"%(23,5,23/5))

print("%d // %d = %d"%(23,5,23//5))

print("%.2f // %d = %.2f"%(23.0,5,23.0//5))

print('%d %s %d = %d'%(25,'%',4,25%4))

print('%.1f %s %d = %.1f'%(25.0,'%',4,25%4))


print("Corrimiento de bits a la izquierda")
"""
2^4  2^3  2^2  2^1  2^0
 0    0    1    0    1
"""
x=5
print(x)

"""
2^4  2^3  2^2  2^1  2^0
 0    1    0    1    0
"""
#Imprime un 10 
print(5<<1)
