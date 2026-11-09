class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlasada:
    def __init__(self):
        self.cabeza = None # Referencia inicial que va a indicar el primer nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        
        # Caso 1: si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
            
        # Caso 2: recorrer hasta el último nodo que existe
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        # Conectar el último nodo con el nuevo nodo (fuera del while)
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("...".join(elementos) + "--None")

# Uso del Programa
lista = ListaEnlasada()

# Insertar elementos
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")

# Mostrar lista
lista.mostrar_lista()