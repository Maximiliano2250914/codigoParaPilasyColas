#Nodo 
class Nodo:
    def __init__(self, data, prioridad):
        self.data=data
        self.siguiente=None
        self.prioridad=prioridad

# Clase Lista Enlazada Simple (sirve igual para cola, cola con prioridad y pila)
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista vacía
    def vacio(self):
        if self.cabeza is None:
            print("Esta vacia")
        else:
            print("Lista no vacia")
  
  #Agregar elemento al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

  #Mostrar la lista (este while me ayuda a recorrer la lista)
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.data, " -- ")
            actual = actual.siguiente

  def eliminar(self):
        if self.cabeza is None:
            print("No hay elementos para eliminar")
            return None
        
        else:
            eliminado = self.cabeza          
            self.cabeza = self.cabeza.siguiente  
            eliminado.siguiente = None       
        return eliminado

    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente  #me lleva hasta el final

        actual.siguiente = nuevo_nodo

    def insertarAntes(self, x, data):
        if self.cabeza is None:
            return

        # Si el elemento X esta al principio
        if self.cabeza.data == x:
            self.agregarInicio(data)
            return

        anterior = None
        actual = self.cabeza

        while actual and actual.data != x:  #
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Elemento no encontrado")
            return

        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = actual
        anterior.siguiente = nuevo_nodo

    def eliminarPrimero(self):
        if self.cabeza is None:
            print("Lista vacia")

        else:
            self.cabeza = self.cabeza.siguiente

#Eliminar el ultimo elemento
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("Lista vacia")

        elif self.cabeza.siguiente is None: #si despues de el 1ro no hay, borrar el 1ro pues es el ultimo
            self.cabeza = None
            return

        else:
            anterior = None
            actual = self.cabeza

            while actual.siguiente:
                anterior = actual       #me lleva hasta el final
                actual = actual.siguiente

            anterior.siguiente = None

    #Insertar (pila)
    def push(self, data):
        nuevo = Nodo(data)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        cont += 1
        
#Eliminar (pila)
    def pop (self):
        if self.vacio():
            return None
            
        else:
            eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            contPila -= 1
            return eliminado.data

#Devolver el proximo elemento a eliminarse (pila)
    def elProximo(self):
        if self.vacio():
            return None
        
        else:
            return self.cabeza.data
#insertar cola
    def enqueue(self, data):
        nuevo = Nodo(data)
        if self.vacio():
            self.cabeza = nuevo
            self.final = nuevo
            
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        
        contCola += 1

#Eliminar (cola)
    def dequeue(self):
        if self.vacio():
            return None
            
        else:
            eliminado = self.cabeza
            self.frente = self.frente.siguiente
            
        
        if self.cabeza is None:
            self.final = None
            
        else:
            contCola -= 1
            return eliminado.data

    def insertar(self,data,prioridad):
        nuevo_nodo = Nodo(data,prioridad)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        elif nuevo_nodo.prioridad<=self.cabeza.prioridad:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.prioridad<=prioridad:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
