class Nodo:
    def __init__(self,dato):
        self.dato= dato
        self.siguiente= None
        #Creacion de un nodo individual
nodo_singular= Nodo("primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)