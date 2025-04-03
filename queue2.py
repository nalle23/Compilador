class Node:
    # Nodo para la implementación de la cola
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    # Implementación de una cola (FIFO - First In, First Out)
    def __init__(self):
        self.front = self.rear = None
        self._size = 0
    
    def enqueue(self, value):
        # Añade un elemento a la cola
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        # Elimina y devuelve el primer elemento de la cola
        if self.front is None:
            raise IndexError("Desencolar de una cola vacía")
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.value

    def peek(self):
        # Devuelve el primer elemento sin eliminarlo
        if self.front is None:
            raise IndexError("Inspeccionar una cola vacía")
        return self.front.value

    def back(self):
        # Devuelve el último elemento sin eliminarlo
        if self.rear is None:
            raise IndexError("Inspeccionar el último elemento de una cola vacía")
        return self.rear.value
    
    def is_empty(self):
        # Verifica si la cola está vacía
        return self.front is None
    
    def size(self):
        # Devuelve el número de elementos en la cola
        return self._size
