def heapify(l,i):
    #Si el nodo tiene dos hijos
    if 2*i+2<=len(l)-1:
        #El hijo izquierdo es menor al hijo derecho
        if l[2*i+1]<= l[2*i+2]:
            min=2*i+1
        #El hijo derecho es el menor
        else:
            min=2*i+2
        #Comparar el valor del menor de los hijos con el padre, preguntamos
        #El padre es mayor al menor del hijo 
        if l[i]>l[min]:
            #Intercambio 
            aux=l[i]
            l[i]=l[min]
            l[min]=aux

            #Recursividad 
            heapify(l,min)

    #Si tiene un hijo
    elif 2*i+1<=len(l)-1:
        #Hijo menor que el padre ?
        if l[i]>l[2*i+1]:
            aux=l[i]
            l[i]=l[2*i+1]
            l[2*i+1]=aux
    return l

def heapSort(l):
    #Lista final 
    l2=[]
    #Iterar sobre lista desde la longitud de la lista//2-1
    #hasta -1, decremento de -1 
    for i in range(len(l)//2-1,-1,-1):
        #Recibe una lista a ordenar y el valor i 
        l=heapify(l,i)
    #Iterar en el rango de 0 hasta la longitud de la lista menos uno
    for i in range(0,len(l)):
        #Intercambio 
        aux=l[0]
        #Primer elemento de la lista igual al ultimo elmento
        l[0]=l[len(l)-1]
        #Ultimo elemento de la lista igual al primero 
        l[len(l)-1]=aux

        #Agregar ultimo elemento de la lista 
        l2.append(aux)
        #Eliminar el ultimo elemento de la lista 
        l=l[:len(l)-1]

        #Recursividad con la lista y el nodo cero 
        l=heapify(l,0)
    return l2

lista=[12,78,90,2,12,0,32,65]

print("Lista original \n",lista)
print("Lista ordenada \n",heapSort(lista))

