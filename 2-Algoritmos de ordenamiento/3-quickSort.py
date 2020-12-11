"""
    Quick Sort 
"""
def quickSort(lista):
    #Caso base
    if len(lista) <=1:
        return lista
    #Caso recursivo
    #Escoger pivote, se escoge el ultimo elemento
    pivote=lista.pop()
    lista1=[]
    lista2=[]
    
    #Itero sobre la lista original
    for i in lista:
        #Si el elemento es menor o igual al pivote, se agrega a la lista1
        if i <= pivote:
            lista1.append(i)
        #Si el elemento es mayo al pivote
        else:
            lista2.append(i)
      
    #Recursividad y ordenamiento 
    lista1=quickSort(lista1)
    lista2=quickSort(lista2)
    
    
    return lista1+[pivote]+lista2

lista=[0,56,78,-34,-23,-23,78]
print('Lista original \n',lista)
print('Lista ordenada \n',quickSort(lista))