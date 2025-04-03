import gc

class HashTable:
    def __init__(self, size=10):
        self.size = size  # Tamaño inicial de la tabla
        self.table = [[] for _ in range(size)]  # Lista de listas para manejo de colisiones
        self.count = 0  # Número de elementos actuales
        self.threshold = 0.7  # Umbral del 70% para rehashing

    def _hash(self, key):
        # Calcula el índice hash para una clave
        return hash(key) % self.size

    def _rehash(self):
        # Duplica el tamaño de la tabla y rehasea los elementos
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]  # Nueva tabla vacía

        # Reinsertamos todos los elementos en la nueva tabla
        old_items = []  # Guardamos los elementos antiguos temporalmente
        for bucket in self.table:
            for key, value in bucket:
                old_items.append((key, value))  # Guardamos clave-valor

        # Actualizamos la tabla y el tamaño
        self.size = new_size
        self.table = new_table
        self.count = 0  # Reiniciamos el contador

        # Volvemos a insertar todos los elementos en la nueva tabla
        for key, value in old_items:
            self.insert(key, value)  # Usamos insert() para mantener la lógica


    def insert(self, key, value):
        # Inserta un par clave-valor en la tabla hash
        if self.count / self.size > self.threshold:
            self._rehash()  # Hacer rehash si se supera el umbral del 70%

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Reemplazo de valor si la clave ya existe
                return
        self.table[index].append([key, value])  # Inserción al final
        self.count += 1  # Incrementar el contador de elementos

    def get(self, key):
        # Obtiene el valor asociado a una clave
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # No encontrado

    def delete(self, key):
        # Elimina un par clave-valor de la tabla hash
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Eliminar par clave-valor
                self.count -= 1  # Decrementar el contador de elementos
                return
        raise KeyError("Clave no encontrada")

    def clear(self):
        # Elimina todos los elementos de la tabla
        self.table = [[] for _ in range(self.size)]  # Reiniciar la tabla
        self.count = 0  # Reiniciar el contador de elementos

    def is_empty(self):
        # Devuelve True si la tabla está vacía, False si no lo está
        return self.count == 0

    def display(self):
        # Muestra el contenido de la tabla hash
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")