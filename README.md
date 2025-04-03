# Compilador

# Estructuras de Datos - Casos de Prueba

Este documento describe los casos de prueba para las estructuras de datos **Stack (Pila)**, **Queue (Cola)** y **Hash Table (Tabla Hash)**.

---

## Stack - Casos de Prueba

### Caso 1: Inserción y eliminación básica
- Se agregan los valores `1`, `2` y `3`.
- Se espera que `pop()` devuelva `3` (el último en entrar).

### Caso 2: Inspeccionar el último elemento
- Después de hacer `pop()`, el último elemento debería ser `2`.

### Caso 3: Vaciar la pila y verificar estado
- Se eliminan todos los elementos con `pop()`.
- Se espera que `is_empty()` devuelva `True`.

### Caso 4: Intentar eliminar de una pila vacía
- Se espera que `pop()` en una pila vacía genere un `IndexError`.

### Caso 5: Intentar inspeccionar una pila vacía
- Se espera que `peek()` en una pila vacía genere un `IndexError`.

---

## Queue - Casos de Prueba

### Caso 1: Inserción y eliminación básica
- Se insertan los valores `"A"`, `"B"`, `"C"`.
- `dequeue()` debería devolver `"A"` (el primero en entrar).

### Caso 2: Inspeccionar el primer elemento
- Después de un `dequeue()`, `peek()` debería devolver `"B"`.

### Caso 3: Verificar tamaño de la cola
- `size()` debería reflejar el número correcto de elementos tras cada operación.

### Caso 4: Intentar eliminar de una cola vacía
- Se espera que `dequeue()` en una cola vacía genere un `IndexError`.

### Caso 5: Intentar inspeccionar una cola vacía
- Se espera que `peek()` en una cola vacía genere un `IndexError`.

---

## Hash Table - Casos de Prueba

### Caso 1: Inserción de elementos
- Se insertan varios pares clave-valor en la tabla hash, donde la clave es un nombre y el valor es un diccionario con la edad y la dirección.
- Se espera que los elementos se inserten correctamente en la tabla.

### Caso 2: Rehashing
- Se insertan suficientes elementos para forzar un rehash (cuando la tabla hash se llena y se redimensiona).
- Después del rehash, se espera que los nuevos elementos se distribuyan correctamente en la tabla.

### Caso 3: Obtención de un valor
- Se solicita el valor asociado a una clave existente (`'Andre'`).
- Se espera que se devuelva el diccionario asociado a `'Andre'`.

### Caso 4: Eliminación de un elemento
- Se elimina el elemento con la clave `'Lizbeth'`.
- Se espera que la tabla refleje la eliminación correctamente.

### Caso 5: Limpieza de la tabla
- Se llama a la función `clear()` para eliminar todos los elementos.
- Se espera que la tabla esté vacía después de la limpieza.

### Caso 6: Verificación de tabla vacía
- Se verifica si la tabla está vacía después de limpiarla.
- Se espera que `is_empty()` devuelva `True`.
