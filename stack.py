class Stack:
    #Implementación de una pila STACK (LIFO - Last In, First Out)
    def __init__(self):
        self.items = []

    def push(self, item):
        #Añade un elemento a la pila
        self.items.append(item)

    def pop(self):
        #Elimina y devuelve el último elemento de la pila
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Extraer de una pila vacía")

    def peek(self):
        #Devuelve el último elemento sin eliminarlo
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Inspeccionar una pila vacía")

    def is_empty(self):
        #Verifica si la pila está vacía
        return len(self.items) == 0

    def size(self):
        #Devuelve el número de elementos en la pila
        return len(self.items)
