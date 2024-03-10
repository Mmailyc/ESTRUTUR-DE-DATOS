"Verificar si una palabra es palíndroma"

from collections import deque

def es_palindroma(palabra):
    cola = deque(palabra)  # Convierte la palabra en una cola (estructura de datos FIFO).
    es_palindromo = True  # Asume inicialmente que la palabra es un palíndromo.
    
    while len(cola) > 1 and es_palindromo:  # Mientras haya más de un caracter y siga siendo palíndromo...
        if cola.popleft() != cola.pop():  # Compara y remueve el primer y último caracter de la cola.
            es_palindromo = False  # Si no son iguales, no es un palíndromo.
    
    return es_palindromo  # Retorna True si es palíndromo, False si no lo es.
print("---------------------------- Ejercicio 1 --------------------------")
palabra = "radar"
print(es_palindroma(palabra))  # Debería imprimir True

palabra = "python"
print(es_palindroma(palabra))  # Debería imprimir False

#ejerccio 2
"Diseño de un sistema de gestión de pedidos"
from collections import deque

from collections import deque  # Importa deque para usar colas.

class SistemaPedidos:  # Define una clase para el sistema de gestión de pedidos.
    def __init__(self):  
        self.cola_pedidos = deque()  # Inicializa una cola vacía para almacenar los pedidos.
    
    def agregar_pedido(self, pedido):  # Método para agregar un pedido a la cola.
        self.cola_pedidos.append(pedido)  # Agrega el pedido al final de la cola.
        print(f"Pedido {pedido} agregado.")  # Imprime un mensaje indicando que el pedido fue agregado.
    
    def procesar_pedido(self):  # Método para procesar el primer pedido de la cola.
        if self.cola_pedidos:  # Si hay pedidos en la cola...
            pedido_procesado = self.cola_pedidos.popleft()  # Remueve y retorna el primer pedido de la cola.
            print(f"Pedido {pedido_procesado} procesado.")  # Imprime un mensaje indicando que el pedido fue procesado.
        else:  # Si no hay pedidos en la cola...
            print("No hay pedidos para procesar.")  # Imprime un mensaje indicando que no hay pedidos para procesar.
    
    def mostrar_estado(self):  # Método para mostrar todos los pedidos en la cola.
        if self.cola_pedidos:  # Si hay pedidos en la cola...
            print("Pedidos en cola:", list(self.cola_pedidos))  # Imprime la lista de pedidos.
        else:  # Si la cola está vacía...
            print("No hay pedidos en cola.")  # Imprime un mensaje indicando que no hay pedidos.


# Demostración del código corregido
print("---------------------------- Ejercicio 2 --------------------------")
sistema = SistemaPedidos()  # Instanciación correcta de SistemaPedidos
sistema.agregar_pedido("Pedido numeero 1")
sistema.agregar_pedido("Pedido numero 2")
sistema.mostrar_estado()
sistema.procesar_pedido()
sistema.mostrar_estado()

"Búsqueda de rutas en un laberinto"

from collections import deque

def encontrar_camino(laberinto, inicio, fin):
    filas, columnas = len(laberinto), len(laberinto[0])  # Obtiene las dimensiones del laberinto.
    visitados = [[False] * columnas for _ in range(filas)]  # Crea una matriz para marcar casillas visitadas.
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Define posibles movimientos: arriba, abajo, izquierda, derecha.
    cola = deque([(inicio, [inicio])])  # Cola para BFS, contiene posición actual y el camino recorrido.
    
    while cola:
        (x, y), camino = cola.popleft()  # Extrae la posición actual y el camino hasta esa posición.
        if (x, y) == fin:  # Si se alcanza el destino, retorna el camino.
            return camino
        for dx, dy in movimientos:  # Para cada posible movimiento...
            nx, ny = x + dx, y + dy  # Calcula la nueva posición.
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 1 and not visitados[nx][ny]:  # Si la nueva posición es válida y no visitada...
                visitados[nx][ny] = True  # Marca la nueva posición como visitada.
                cola.append(((nx, ny), camino + [(nx, ny)]))  # Añade la nueva posición y el camino actualizado a la cola.
    
    return "No se encontró un camino."  # Si no se encuentra un camino al destino, retorna mensaje.
# Definimos un laberinto de ejemplo
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1]
]

inicio = (0, 0)
fin = (4, 4)

print("---------------------------- Ejercicio 3 --------------------------")
camino = encontrar_camino(laberinto, inicio, fin)
print("Camino encontrado:", camino)

"Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como completadas y mostrar la próxima tarea pendiente."

from collections import deque

class SistemaTareas:
    def __init__(self):  # Corregido __init__
        self.tareas = deque()
    
    def agregar_tarea(self, tarea):
         # Añade una nueva tarea al final de la cola.
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
    
    def marcar_completada(self):
        if self.tareas:
            # Remueve y devuelve la tarea más antigua (la primera añadida).
            tarea_completada = self.tareas.popleft()
            print(f"Tarea '{tarea_completada}' completada.")
        else:
            # Si no hay tareas, informa al usuario.
            print("No hay tareas pendientes.")
    
    def mostrar_proxima_tarea(self):
        # Verifica si hay tareas pendientes para mostrar.
        if self.tareas:
            # Imprime la lista de tareas pendientes.
            print(f"Próxima tarea pendiente: '{self.tareas[0]}'")
        else:
            # Informa al usuario si no hay tareas pendientes.
            print("No hay tareas pendientes.")

# imprimimos todos los valores agregados y los resultados de estos
print("---------------------------- Ejercicio 4 --------------------------")
sistema_tareas = SistemaTareas()  # Creación del objeto sistema_tareas
sistema_tareas.agregar_tarea("Tarea 1")
sistema_tareas.agregar_tarea("Tarea 2")
sistema_tareas.mostrar_proxima_tarea()
sistema_tareas.marcar_completada()
sistema_tareas.mostrar_proxima_tarea()

"Implementar una función que cuente la cantidad de nodos en el árbol."

class Nodo:
    def __init__(self, valor):
        self.valor = valor  # El valor almacenado en el nodo
        self.izquierda = None  # Referencia al nodo hijo izquierdo
        self.derecha = None  # Referencia al nodo hijo derecho

# Definición de la clase ArbolBinario que representa un árbol binario
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz  # La raíz del árbol

# Función para contar el número de nodos en un árbol binario
def contar_nodos(nodo):
    if nodo is None:  # Si el nodo es None, significa que es un árbol vacío
        return 0
    else:  # Si el nodo no es None, cuenta este nodo y los nodos en los subárboles izquierdo y derecho
        return 1 + contar_nodos(nodo.izquierda) + contar_nodos(nodo.derecha)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear nodos
    nodo1 = Nodo(1)  # Crear un nodo con valor 1
    nodo2 = Nodo(2)  # Crear un nodo con valor 2
    nodo3 = Nodo(3)  # Crear un nodo con valor 3

    # Construir el árbol
    arbol = ArbolBinario(nodo1)  # Crear un árbol con nodo1 como raíz
    arbol.raiz.izquierda = nodo2  # Asignar nodo2 como el hijo izquierdo de la raíz
    arbol.raiz.derecha = nodo3  # Asignar nodo3 como el hijo derecho de la raíz

    print("---------------------------- Ejercicio 5 --------------------------")
    print("Número total de nodos en el árbol:", contar_nodos(arbol.raiz))  # Imprimir el número total de nodos en el árbol


"Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos)."

# Definición de la clase Nodo para representar un nodo en un árbol binario
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor  # Valor almacenado en el nodo
        self.izquierda = izquierda  # Referencia al nodo hijo izquierdo
        self.derecha = derecha  # Referencia al nodo hijo derecho

# Función recursiva para imprimir los nodos hoja de un árbol binario
def imprimir_nodos_hoja(nodo):
    if nodo is None:  # Si el nodo es None, se detiene la función
        return
    if nodo.izquierda is None and nodo.derecha is None:  # Si es un nodo hoja (sin hijos)
        print(nodo.valor)  # Imprime el valor del nodo
    else:  # Si no es un nodo hoja
        imprimir_nodos_hoja(nodo.izquierda)  # Llama recursivamente a la función con el hijo izquierdo
        imprimir_nodos_hoja(nodo.derecha)  # Llama recursivamente a la función con el hijo derecho

print("---------------------------- Ejercicio 6 --------------------------")
# Ejemplo de uso:
# Construimos el árbol binario:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo2 = Nodo(2, nodo4, nodo5)
nodo3 = Nodo(3, derecha=nodo6)
raiz = Nodo(1, nodo2, nodo3)

# Imprimimos los nodos hoja del árbol
imprimir_nodos_hoja(raiz)

"Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo)"


# Definición de la clase Nodo para representar un nodo en un árbol binario
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor  # Valor almacenado en el nodo
        self.izquierda = izquierda  # Referencia al nodo hijo izquierdo
        self.derecha = derecha  # Referencia al nodo hijo derecho

# Función recursiva para imprimir los nodos internos de un árbol binario
def imprimir_nodos_internos(nodo):
    # Si el nodo es None o es una hoja (ambos hijos son None), no hace nada (no imprime nada).
    if nodo is None or (nodo.izquierda is None and nodo.derecha is None):
        return
    else:
        # Imprimimos el valor del nodo actual, ya que no es una hoja (es un nodo interno).
        print(nodo.valor)
        # Luego, continúamos la búsqueda de manera recursiva en los subárboles izquierdo y derecho.
        imprimir_nodos_internos(nodo.izquierda)
        imprimir_nodos_internos(nodo.derecha)


print("---------------------------- Ejercicio 7 --------------------------")
# Construimos el árbol binario:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo2 = Nodo(2, nodo4, nodo5)
nodo3 = Nodo(3, derecha=nodo6)
raiz = Nodo(1, nodo2, nodo3)

# Imprimimos los nodos internos del árbol
imprimir_nodos_internos(raiz)

"Calcular altura y profundidad:"

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

def altura_arbol(nodo):
    # Un árbol vacío tiene altura -1
    if nodo is None:
        return -1
    else:
        # Calcular la altura de cada subárbol
        altura_izquierda = altura_arbol(nodo.izquierda)
        altura_derecha = altura_arbol(nodo.derecha)
        # La altura del árbol es el máximo de las alturas de los subárboles + 1
        return 1 + max(altura_izquierda, altura_derecha)


if __name__ == "__main__":
    # Crear nodos
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    # Construimos  el árbol
    arbol = ArbolBinario(nodo1)
    arbol.raiz.izquierda = nodo2
    arbol.raiz.derecha = nodo3
    nodo2.izquierda = nodo4  # Añadir un nivel más para hacer el árbol más interesante

    print("---------------------------- Ejercicio 8 --------------------------")
    
    print("Altura del árbol:", altura_arbol(arbol.raiz))

"Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo"

class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asigna el valor proporcionado al atributo 'valor' del nodo
        self.izquierda = None  # Inicializa el puntero al hijo izquierdo como nulo
        self.derecha = None  # Inicializa el puntero al hijo derecho como nulo

# Definición de la clase ArbolBinario para representar el árbol
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz  # Asigna la raíz proporcionada al atributo 'raiz' del árbol, o la deja como nula si no se proporciona ninguna

# Función para calcular la profundidad de un nodo con un valor específico en el árbol
def profundidad_nodo(nodo, valor, profundidad_actual=0):
    if nodo is None:
        return -1  # Si el nodo es nulo, el valor no se encuentra en el árbol, retorna -1
    elif nodo.valor == valor:
        return profundidad_actual  # Si el valor del nodo actual es igual al valor buscado, retorna la profundidad actual
    else:
        # Si el valor no es el buscado, busca en los subárboles izquierdo y derecho recursivamente
        profundidad_izquierda = profundidad_nodo(nodo.izquierda, valor, profundidad_actual + 1)
        profundidad_derecha = profundidad_nodo(nodo.derecha, valor, profundidad_actual + 1)
        
        # Si el valor no se encuentra en el subárbol izquierdo, retorna el resultado del derecho y viceversa
        if profundidad_izquierda != -1:
            return profundidad_izquierda
        else:
            return profundidad_derecha

# Ejemplo de uso
# Verifica si este script es el script principal que se está ejecutando
if __name__ == "__main__":
    # Creamos nodos y construimos el árbol como en ejemplos anteriores
    nodo1 = Nodo(1)  # Creamos un nodo con valor 1
    nodo2 = Nodo(2)  # Creamos un nodo con valor 2
    nodo3 = Nodo(3)  # Creamos un nodo con valor 3
    nodo4 = Nodo(4)  # Creamos un nodo con valor 4
    
    arbol = ArbolBinario(nodo1)  # Creamos un árbol con nodo1 como raíz
    arbol.raiz.izquierda = nodo2  # Establecemos nodo2 como hijo izquierdo de la raíz
    arbol.raiz.derecha = nodo3  # Establecemos nodo3 como hijo derecho de la raíz
    nodo2.izquierda = nodo4  # Añadimos un nivel más al establecer nodo4 como hijo izquierdo de nodo2
    print("---------------------------- Ejercicio 9 --------------------------")  # Imprimimos un mensaje indicando el inicio del ejercicio
    
    valor_a_buscar = 4  # Definimos el valor que queremos buscar en el árbol
    profundidad = profundidad_nodo(arbol.raiz, valor_a_buscar)  # Calculamos la profundidad del nodo con el valor dado
    if profundidad != -1:  # Si se encontró el valor en el árbol
        print(f"La profundidad del nodo con valor {valor_a_buscar} es: {profundidad}")  # Imprimimos la profundidad del nodo encontrado
    else:  # Si el valor no se encontró en el árbol
        print(f"El valor {valor_a_buscar} no se encuentra en el árbol.")  # Imprimimos un mensaje indicando que el valor no se encuentra en el árbol


"Buscar el mínimo y el máximo:"
# Definición de la clase Nodo para representar los nodos del árbol binario de búsqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asigno el valor proporcionado a mi atributo 'valor'
        self.izquierda = None  # Inicializo el puntero a mi hijo izquierdo como nulo
        self.derecha = None  # Inicializo el puntero a mi hijo derecho como nulo

# Definición de la clase ArbolBinarioBusqueda para representar el árbol binario de búsqueda
class ArbolBinarioBusqueda:
    def __init__(self, raiz=None):
        self.raiz = raiz  # Asigno la raíz proporcionada a mi atributo 'raiz', o la dejo como nula si no se proporciona ninguna

def encontrar_minimo(nodo):
    """Encuentro el valor mínimo en el árbol binario de búsqueda."""
    actual = nodo  # Establezco el nodo actual para comenzar el recorrido desde la raíz
    # El mínimo está en el nodo más a la izquierda
    while actual.izquierda is not None:  # Itero hasta que no haya más nodos a mi izquierda
        actual = actual.izquierda  # Avanzo al siguiente nodo a mi izquierda
    return actual.valor  # Retorno el valor del nodo actual, que es el valor mínimo del árbol

print("---------------------------- Ejercicio 10 --------------------------")  # Imprimo un mensaje indicando el inicio del ejercicio
# Verifico si este script es el script principal que se está ejecutando
if __name__ == "__main__":
    # Creo nodos y construyo el árbol binario de búsqueda
    raiz = Nodo(8)  # Creo un nodo raíz con valor 8
    raiz.izquierda = Nodo(3)  # Establezco mi nodo izquierdo con valor 3
    raiz.derecha = Nodo(10)  # Establezco mi nodo derecho con valor 10
    raiz.izquierda.izquierda = Nodo(1)  # Establezco el nodo izquierdo de mi hijo izquierdo con valor 1
    raiz.izquierda.derecha = Nodo(6)  # Establezco el nodo derecho de mi hijo izquierdo con valor 6
    raiz.derecha.derecha = Nodo(14)  # Establezco el nodo derecho de mi hijo derecho con valor 14
    raiz.izquierda.derecha.izquierda = Nodo(4)  # Establezco el nodo izquierdo de mi hijo derecho del hijo izquierdo con valor 4
    raiz.izquierda.derecha.derecha = Nodo(7)  # Establezco el nodo derecho de mi hijo derecho del hijo izquierdo con valor 7
    raiz.derecha.derecha.izquierda = Nodo(13)  # Establezco el nodo izquierdo de mi hijo izquierdo del hijo derecho con valor 13

    arbol = ArbolBinarioBusqueda(raiz)  # Creo un árbol binario de búsqueda con la raíz definida
    valor_minimo = encontrar_minimo(arbol.raiz)  # Encuentro el valor mínimo en el árbol
    print(f"El valor mínimo en el árbol es: {valor_minimo}")  # Imprimo el valor mínimo encontrado en el árbol

"Implementar una función que encuentre el nodo con el valor máximo en el árbol."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self, raiz=None):
        self.raiz = raiz

def encontrar_maximo(nodo):
    """Encuentra el valor máximo en el árbol binario de búsqueda."""
    actual = nodo
    # El máximo está en el nodo más a la derecha
    while actual.derecha is not None:
        actual = actual.derecha
    return actual.valor

print("---------------------------- Ejercicio 11 --------------------------")
if __name__ == "__main__":
    # Crear nodos y construir el árbol binario de búsqueda como antes
    raiz = Nodo(8)
    raiz.izquierda = Nodo(3)
    raiz.derecha = Nodo(10)
    raiz.izquierda.izquierda = Nodo(1)
    raiz.izquierda.derecha = Nodo(6)
    raiz.derecha.derecha = Nodo(14)
    raiz.izquierda.derecha.izquierda = Nodo(4)
    raiz.izquierda.derecha.derecha = Nodo(7)
    raiz.derecha.derecha.izquierda = Nodo(13)

    arbol = ArbolBinarioBusqueda(raiz)
    valor_maximo = encontrar_maximo(arbol.raiz)
    print(f"El valor máximo en el árbol es: {valor_maximo}")


