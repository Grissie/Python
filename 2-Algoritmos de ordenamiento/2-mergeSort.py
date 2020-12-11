"""
    Merge Sort
"""
#Necesita dos listas como parametros 
def merge(l1,l2):
    
    #Lista final ordenada
    l3=[]
    
    #Si la lista1 y lista2 no estan vacias
    while (len(l1)>0) and (len(l2)>0):
        #Si el primer elemento de la lista1 es menor al primer elemento de la lista2 a li
        if l1[0] < l2[0]:
            #Agregar elemento a la lista final 
            l3.append(l1[0])
            #Elimia el primer elemento 
            l1=l1[1:]
        #Si el menor es el de la lista2
        else:
            l3.append(l2[0])
            l2=l2[1:]

    
   
    #Preguntar si quedan elementos en las listas
    if len(l1) > 0:
        #Sumar la lista final a la lista1
        l3=l3+l1
    
    if len(l2)>0:
        l3=l3+l2
   
    #Regresa la lista final 
    return l3
    
def mergeSort(l):
    #Caso base
    if len(l)==1:
        return l
    #Caso recursivo
    #Lista de la izquierda
    li=l[:len(l)//2]
    #Lista de la derecha 
    ld=l[len(l)//2:]

    #Recursion de la funcion, se pasa la lista izquierda y se guarda el resultado en lista_izq ordenada 
    li=mergeSort(li)
    #Recursion de la funcion, se pasa la lista derecha y se guarda el resultado en lista_der ordenada
    ld=mergeSort(ld)
    
    return merge(li,ld)

def main():
    lista=[-67,89,45,-23,0,56]
    print('Lista original \n',lista)
    print('Lista ordenada \n',mergeSort(lista))
    
main()