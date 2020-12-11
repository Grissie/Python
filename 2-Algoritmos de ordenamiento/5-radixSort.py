import random

"""
    Los número se reprensentan como cadenas 
"""
def radixSort(lista):
    #Maximo de digitos en la lista
    n=0
    #Iterar sobre la lista
    for i in lista:
        if len(i) > n:
            n=len(i)

    for i in range(0,len(lista)):
        while len(lista[i])<n:
            lista[i]="0"+lista[i]

    #Inicia en la longitud-1 de la lista hasta -1
    #decrementando en uno
    for j in range(n-1,-1,-1):
        grupos=[[] for i in range(10)]

        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(lista[i])

        lista=[]
        for g in grupos:
            lista+=g

    return [int(i) for i in lista]

def main():
    #Un numero aleatorio del 0 al 200 y se castee en cadena
    lista=[str(random.randint(0,200)) for i in range (10)]

    print("Lista original \n",lista)

    print("Lista ordenada \n",radixSort(lista))

main()


