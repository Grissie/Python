'''
Implementación del método de costo uniforme en python  
'''

'''
    Clase que simula una Ciudad
'''
class Ciudad:
    '''
    Constructor de la clase
    :param nombre: es el nombre de la ciudad
    :vecinos: lista de vecinos de la ciudad 
    :visitado: variable para indicar si ya fue visitado 
    :padre: variable que indica de quien proviene 
    '''
    def __init__(self,nombre):
        self.nombre=nombre
        self.vecinos=[]
        self.visitado=False
        self.padre=None
        self.distancia=float('inf')

    '''
    Función que agrega una ciudad vecina
    :param vecino: nombre de la ciudad vecina
    :param peso: costo de la arista 
    '''
    def agregarVecino(self,vecino,peso):
        if not vecino in self.vecinos:
            self.vecinos.append([vecino,peso])

'''
Clase que simula el mapa de Rumania 
'''
class Mapa:
    '''
    Constructor de la clase 
    :ciudades: diccionario que guarda las ciudades del mapa completo
    '''
    def __init__(self):
        self.ciudades={}

    '''
    Función que agrega una ciudad al mapa
    :param nombre: es el nombre de la ciudad
    '''
    def agregarCiudad(self,nombre):
        if nombre not in self.ciudades:
            self.ciudades[nombre]=Ciudad(nombre)

    '''
    Función que agrega una arista al mapa
    :param inicio: nombre de la ciudad del extremo
    :param fin: nombre de la ciudad del otro extremo
    :param peso: costo de la arista 
    '''
    def agregarArista(self,inicio,fin,peso):
        if inicio in self.ciudades and fin in self.ciudades:
            self.ciudades[inicio].agregarVecino(fin,peso)
            self.ciudades[fin].agregarVecino(inicio,peso)

    '''
    Función que imprime los pasos para llegar a la ruta óptima
    :c: es una variable que recorrero al diccionario de ciudades 
    '''
    def imprimirGrafo(self):
        for ciudad in self.ciudades:
            if self.ciudades[ciudad].distancia==0 and self.ciudades[ciudad].padre==None:
                print('Inicio: ',ciudad)
            else:
                print(str(self.ciudades[ciudad].padre)+'   -->   '+str(ciudad)+': '
                +str(self.ciudades[ciudad].distancia))
    
    '''
    Función que imprime las ciudades visitadas
    :visitados: lista de ciudades que guarda a las ya visitadas 
    :noVisitados: lista de ciudades que aún no se visitan 
    :actual: permite identificar la ciudad actual 
    '''
    def imprimirVisitados(self):
        visitados=[]
        noVisitados=[]
        for ciudad in self.ciudades:
            if self.ciudades[ciudad].distancia==0 and self.ciudades[ciudad].padre==None:
                self.ciudades[ciudad].distancia=0
                actual=ciudad
                a=ciudad
            self.ciudades[ciudad].padre=None
            noVisitados.append(ciudad)

        while len(noVisitados)>0:
            self.ciudades[actual].visitado=True
            visitados.append(actual)
            noVisitados.remove(actual)
            actual=self.menor(noVisitados)

    '''
    Función que muestra la ruta y costo óptimo
    :param inicio: ciudad de inicio
    :param fin: ciudad final 
    :ruta: guarda la ruta óptima
    '''
    def ruta(self,inicio,fin):
        ruta=[]
        actual=fin
        while actual!=None:
            ruta.insert(0,actual)
            actual=self.ciudades[actual].padre
        print('Ruta: ',ruta)
        if inicio==fin:
            print('Costo: 0')
        else:
            print('Costo: ',self.ciudades[fin].distancia)
    
    '''
    Función que obtiene la menor distancia 
    '''
    def menor(self,lista):
        if len(lista)>0:
            m=self.ciudades[lista[0]].distancia
            v=lista[0]
            for e in lista:
                if m>self.ciudades[e].distancia:
                    m=self.ciudades[e].distancia
                    v=e
            return v

    '''
    Función que va expandiendo la ciudad actual a su ciudad con menor costo en la arista 
    :actual: variable auxiliar que guarda la ciudad actual 
    :noVisitados: lista que guarda las ciudades que aún  no se visitan 
    '''
    def costoUniforme(self,inicio):
        if inicio in self.ciudades:
            self.ciudades[inicio].distancia=0
            actual=inicio
            noVisitados=[]

            for ciudad in self.ciudades:
                if ciudad!=inicio:
                    self.ciudades[ciudad].distancia=float('inf')
                self.ciudades[ciudad].padre=None
                noVisitados.append(ciudad)

            while len(noVisitados)>0:
                for vecino in self.ciudades[actual].vecinos:
                    if self.ciudades[vecino[0]].visitado==False:
                        if self.ciudades[actual].distancia+vecino[1]<self.ciudades[vecino[0]].distancia:
                            self.ciudades[vecino[0]].distancia=self.ciudades[actual].distancia+vecino[1]
                            self.ciudades[vecino[0]].padre=actual

                self.ciudades[actual].visitado=True
                noVisitados.remove(actual)
                actual=self.menor(noVisitados)

        else:
            return False 

'''
Función principal del programa, donde se crea el mapa, las ciudades y aristas
:ciudades: lista del nombre de las ciudades que conforman el mapa
:aristas: lineas que unen las ciudades con su peso respectivo
:origen: ciudad desde donde inicia la búsqueda
:destino: ciudad donde termina la búsqueda 
'''
def main():
    ciudades=[
                'Arad','Bucharest','Craiova','Drobeta','Eforie','Fagaras','Giurgiu','Hirsova',
                'Iasi','Lugoj','Mehadia','Neamt','Oradea','Pitesti','Rimnicu Vilcea','Sibiu',
                'Timisoara','Urziceni','Vaslui','Zerind'
            ]

    aristas=[
                'Arad','Zerind',75,
                'Arad','Timisoara',118,
                'Zerind','Oradea',71,
                'Timisoara','Lugoj',111,
                'Oradea','Sibiu',151,
                'Craiova','Drobeta',120,
                'Craiova','Rimnicu Vilcea',146,
                'Craiova','Pitesti',138,
                'Rimnicu Vilcea','Sibiu',80,
                'Rimnicu Vilcea','Pitesti',97,
                'Sibiu','Arad',140,
                'Sibiu','Fagaras',99,
                'Lugoj','Mehadia',70,
                'Mehadia','Drobeta',75,
                'Fagaras','Bucharest',211,
                'Pitesti','Bucharest',101,
                'Bucharest','Urziceni',85,
                'Bucharest','Giurgiu',90,
                'Urziceni','Vaslui',142,
                'Urziceni','Hirsova',98,
                'Iasi','Neamt',87,
                'Iasi','Vaslui',92,
                'Hirsova','Eforie',86
            ]

    mapa_Rumania=Mapa()

    for ciudad in ciudades:
        mapa_Rumania.agregarCiudad(ciudad)

    for i in range(0,len(aristas)-1,3):
        mapa_Rumania.agregarArista(aristas[i],aristas[i+1],aristas[i+2])

    origen=''
    destino=''
    print('╔═════════════════════════════════╗')
    print('║    Método del Costo Uniforme    ║')
    print('╚═════════════════════════════════╝')
	
    print("\nCiudad inicio:")
    while origen not in ciudades:
        origen=input()
		
    print("\nCiudad destino:")
    while destino not in ciudades:
        destino=input()
		
    if origen != destino:
        mapa_Rumania.costoUniforme(origen)            

    print('┌────────────────────┐')
    print('│  Método por pasos  │')
    print('└────────────────────┘')
    mapa_Rumania.imprimirGrafo()
    print('┌────────────────────┐')
    print('│     Ruta óptima    │')
    print('└────────────────────┘')
    mapa_Rumania.ruta(origen,destino)
    mapa_Rumania.imprimirVisitados()

main()
