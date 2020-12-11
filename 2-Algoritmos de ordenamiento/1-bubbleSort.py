"""
    Bubble Sort
"""
def bubbleSort(lista):
    #Longitud de la lista
    n=len(lista)
    #Recorrer lista
    for i in range(1,n):
        for j in range(0,n-1):
            #Comparacion de elemento actual y el elemento siguiente 
            if lista[j] > lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista

def main():
    lista=[-67,0,123,45,67,-34,45]
    print('Lista original\n',lista)
    print('Lista ordenada\n',bubbleSort(lista))
            
main()