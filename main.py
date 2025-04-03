# Nallely Lizbeth Serna Rivera A00833111 - Tarea 1

from stack import Stack
from queue2 import Queue
from hash2 import HashTable

# Pruebas de las estructuras de datos
if __name__ == "__main__":

    """ --- STACK TEST CASES ---
    
    Caso 1: Inserción y eliminación básica
    Se agregan los valores 1, 2, y 3.
    Se espera que pop() devuelva 3 (último en entrar).
    
    Caso 2: Inspeccionar el último elemento
    Después de hacer pop(), el último elemento debería ser 2.
    
    Caso 3: Vaciar la pila y verificar estado
    Se eliminan todos los elementos con pop().
    Se espera que is_empty() devuelva True. 
    
    Caso 4: Intentar eliminar de una pila vacía
    Se espera que pop() en una pila vacía genere un IndexError.
    
    Caso 5: Intentar inspeccionar una pila vacía
    Se espera que peek() en una pila vacía genere un IndexError.
    """

    print("--- Stack ---")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack pop:", stack.pop())  # Debe imprimir 3
    print("Stack peek:", stack.peek())  # Debe imprimir 2

    stack.pop()
    stack.pop()
    print("Stack is empty:", stack.is_empty())  # Debe imprimir True

    try:
        stack.pop()  # Debe lanzar IndexError
    except IndexError as e:
        print("Error esperado en pop():", e)

    try:
        stack.peek()  # Debe lanzar IndexError
    except IndexError as e:
        print("Error esperado en peek():", e)

    
    """ --- QUEUE TEST CASES ---
    
    Caso 1: Inserción y eliminación básica
    Se insertan "A", "B", "C".
    dequeue() debería devolver "A" (primero en entrar).
    
    Caso 2: Inspeccionar el primer elemento
    Después de un dequeue(), peek() debería devolver "B".
    
    Caso 3: Verificar tamaño de la cola
    size() debería reflejar el número correcto de elementos tras cada operación.
    
    Caso 4: Intentar eliminar de una cola vacía
    Se espera que dequeue() en una cola vacía genere un IndexError.
    
    Caso 5: Intentar inspeccionar una cola vacía
    Se espera que peek() en una cola vacía genere un IndexError.
    """

    print("\n--- Queue ---")
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue dequeue:", queue.dequeue())  # Debe imprimir 'A'
    print("Queue peek:", queue.peek())  # Debe imprimir 'B'
    print("Queue size:", queue.size())  # Debe imprimir 2
    print("Queue back:", queue.back())  # Debe imprimir C

    queue.dequeue()
    queue.dequeue()
    print("Queue is empty:", queue.is_empty())  # Debe imprimir True

    try:
        queue.dequeue()  # Debe lanzar IndexError
    except IndexError as e:
        print("Error esperado en dequeue():", e)

    try:
        queue.peek()  # Debe lanzar IndexError
    except IndexError as e:
        print("Error esperado en peek():", e)


    """ --- HASH TABLE TEST CASES ---
    
    Caso 1: Inserción de elementos
    Se insertan varios pares clave-valor en la tabla hash, donde la clave es un nombre y el valor es un diccionario con la edad y la dirección.
    Se espera que los elementos se inserten correctamente en la tabla.

    Caso 2: Rehashing
    Se insertan suficientes elementos para forzar un rehash (cuando la tabla hash se llena y se redimensiona).
    Después del rehash, se espera que los nuevos elementos se distribuyan correctamente en la tabla.

    Caso 3: Obtención de un valor
    Se solicita el valor asociado a una clave existente ('Andre').
    Se espera que se devuelva el diccionario asociado a 'Andre'.

    Caso 4: Eliminación de un elemento
    Se elimina el elemento con la clave 'Lizbeth'.
    Se espera que la tabla refleje la eliminación correctamente.

    Caso 5: Limpieza de la tabla
    Se llama a la función clear() para eliminar todos los elementos.
    Se espera que la tabla esté vacía después de la limpieza.

    Caso 6: Verificación de tabla vacía
    Se verifica si la tabla está vacía después de limpiarla.
    Se espera que is_empty() devuelva True.

    """


    print("\n--- HashTable---")

    hash_table = HashTable()

    # Insertamos datos como nombre, edad y dirección
    hash_table.insert("Nallely", {"edad": 21, "direccion": "Calle 123"})
    hash_table.insert("Andre", {"edad": 23, "direccion": "Avenida 456"})
    hash_table.insert("Daniel", {"edad": 22, "direccion": "Calle 789"})
    hash_table.insert("Aitana", {"edad": 4, "direccion": "Boulevard 101"})

    # Mostramos la tabla
    print("Tabla antes de rehash:")
    hash_table.display()

    # Insertamos más datos para forzar un rehash
    hash_table.insert("Marta", {"edad": 28, "direccion": "Calle 102"})
    hash_table.insert("Sofia", {"edad": 26, "direccion": "Avenida 303"})
    hash_table.insert("Pedro", {"edad": 24, "direccion": "Calle 404"})
    hash_table.insert("Edith", {"edad": 41, "direccion": "Calle 102"})
    hash_table.insert("Francisco", {"edad": 44, "direccion": "Avenida 303"})
    hash_table.insert("Lizbeth", {"edad": 24, "direccion": "Calle 404"})

    # Mostramos la tabla después del rehash
    print("\nTabla después de rehash:")
    hash_table.display()

    # Obtener un valor
    print("\nValor asociado a 'Andre':", hash_table.get("Andre"))  # Output: {'edad': 23, 'direccion': 'Avenida 456'}

    # Borrar un elemento
    hash_table.delete("Lizbeth")
    print("\nTabla después de borrar a Lizbeth:")
    hash_table.display()

    # Limpiar la tabla
    hash_table.clear()
    print("\nTabla después de limpiar:")
    hash_table.display()

    # Verificar si está vacía
    print("\n¿Está vacía?", hash_table.is_empty())  # Output: True