#####EJERCICIOS PARTE 01
"Duplicar nodos"
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sigu = None  # Apunta al siguiente nodo
        self.ante = None  # Apunta al nodo anterior

class LsitDoble:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo de la lista
        self.fin = None     # Apunta al último nodo de la lista

    def vacia(self):
        return self.inicio is None

    def agreg_princ(self, dato):
        # Agrega un nodo al principio de la lista
        nuev_nodo = Nodo(dato)
        if self.vacia():
            self.inicio = self.fin = nuev_nodo
        else:
            nuev_nodo.sigu = self.inicio
            self.inicio.ante = nuev_nodo
            self.inicio = nuev_nodo

    def agregar_finl(self, dato):
        # Agrega un nodo al final de la lista
        if self.vacia():
            self.agreg_princ(dato)
        else:
            nuev_nodo = Nodo(dato)
            self.fin.sigu = nuev_nodo
            nuev_nodo.ante = self.fin
            self.fin = nuev_nodo

    def duplicar(self):
        # Duplica los nodos de la lista
        actual = self.inicio
        while actual:
            nuev_nodo = Nodo(actual.dato)  # Creamos un nuevo nodo con el mismo dato
            nuev_nodo.sigu = actual.sigu   # El nodo siguiente al nuevo es el mismo siguiente del actual
            if actual.sigu:                
                actual.sigu.ante = nuev_nodo  # El nodo anterior al siguiente del actual es el nuevo nodo
            actual.sigu = nuev_nodo       # El siguiente del actual es el nuevo nodo
            nuev_nodo.ante = actual      # El anterior del nuevo nodo es el actual
            actual = nuev_nodo.sigu      # Movemos al siguiente nodo para duplicar

            if actual is None:
                self.fin = nuev_nodo  # Si llegamos al final de la lista, actualizamos el fin

    def imprimir(self):
        # Imprime los datos de la lista en orden
        actual = self.inicio
        while actual:
            print(actual.dato, end=' ')
            actual = actual.sigu
        print()

    def imprimir_at(self):
        # Imprime los datos de la lista en orden inverso
        actual = self.fin
        while actual:
            print(actual.dato, end=' ')
            actual = actual.ante
        print()

# Creación de la lista original
lst_original = LsitDoble()
lst_original.agreg_princ(4)
lst_original.agreg_princ(3)
lst_original.agreg_princ(2)
lst_original.agreg_princ(1)

# Duplicación de cada nodo de la lista
lst_original.duplicar()

# Impresión de la lista original hacia adelante
print("Lista Original hacia adelante:")
lst_original.imprimir()

# Impresión de la lista original hacia atrás
print("Lista Original hacia atrás:")
lst_original.imprimir_at()

"Contar nodos pares e impares"
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sigu = None  # Apunta al siguiente nodo
        self.ante = None  # Apunta al nodo anterior

class LsitDoble:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo de la lista
        self.fin = None     # Apunta al último nodo de la lista

    def vacia(self):
        return self.inicio is None

    def agreg_princ(self, dato):
        # Agrega un nodo al principio de la lista
        nuev_nodo = Nodo(dato)
        if self.vacia():
            self.inicio = self.fin = nuev_nodo
        else:
            nuev_nodo.sigu = self.inicio
            self.inicio.ante = nuev_nodo
            self.inicio = nuev_nodo

    def agregar_finl(self, dato):
        # Agrega un nodo al final de la lista
        if self.vacia():
            self.agreg_princ(dato)
        else:
            nuev_nodo = Nodo(dato)
            self.fin.sigu = nuev_nodo
            nuev_nodo.ante = self.fin
            self.fin = nuev_nodo

    def contar_p_i(self):
        # Cuenta el número de nodos con dato par e impar
        pares = 0
        impares = 0
        actual = self.inicio
        while actual:
            if actual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            actual = actual.sigu
        return pares, impares

    def imprimir(self):
        # Imprime los datos de la lista en orden
        actual = self.inicio
        while actual:
            print(actual.dato, end=' ')
            actual = actual.sigu
        print()

    def imprimir_at(self):
        # Imprime los datos de la lista en orden inverso
        actual = self.fin
        while actual:
            print(actual.dato, end=' ')
            actual = actual.ante
        print()

# Creación de la lista con al menos 9 nodos
lst = LsitDoble()
for dato in range(1, 10):
    lst.agregar_finl(dato)

# Conteo de nodos con datos pares e impares
pares, impares = lst.contar_p_i()
print("Nodos con dato par:", pares)
print("Nodos con dato impar:", impares)

# Impresión de la lista hacia adelante
print("Lista hacia adelante:")
lst.imprimir()

# Impresión de la lista hacia atrás
print("Lista hacia atrás:")
lst.imprimir_at()

"Incertar nodos duplicados"
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sigu = None  # Apunta al siguiente nodo
        self.ante = None  # Apunta al nodo anterior

class LsitDoble:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo de la lista
        self.fin = None     # Apunta al último nodo de la lista

    def vacia(self):
        return self.inicio is None

    def agreg_princ(self, dato):
        # Agrega un nodo al principio de la lista
        nuev_nodo = Nodo(dato)
        if self.vacia():
            self.inicio = self.fin = nuev_nodo
        else:
            nuev_nodo.sigu = self.inicio
            self.inicio.ante = nuev_nodo
            self.inicio = nuev_nodo

    def agregar_finl(self, dato):
        # Agrega un nodo al final de la lista
        if self.vacia():
            self.agreg_princ(dato)
        else:
            nuev_nodo = Nodo(dato)
            self.fin.sigu = nuev_nodo
            nuev_nodo.ante = self.fin
            self.fin = nuev_nodo

    def agreg_en(self, dato, posicion):
        # Inserta un nodo en una posición específica de la lista
        if posicion == 0 or self.vacia():
            self.agreg_princ(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.inicio
            idx = 0
            while actual.sigu is not None and idx < posicion - 1:
                actual = actual.sigu
                idx += 1
            if actual.sigu is None:
                self.agregar_finl(dato)
            else:
                nuevo.sigu = actual.sigu
                actual.sigu.ante = nuevo
                actual.sigu = nuevo
                nuevo.ante = actual

    def imprimir(self):
        # Imprime los datos de la lista en orden
        actual = self.inicio
        while actual:
            print(actual.dato, end=' ')
            actual = actual.sigu
        print()

    def imprimir_at(self):
        # Imprime los datos de la lista en orden inverso
        actual = self.fin
        while actual:
            print(actual.dato, end=' ')
            actual = actual.ante
        print()

# Creación de la lista con al menos 5 nodos
lst = LsitDoble()
for dato in range(1, 6):
    lst.agregar_finl(dato)

# Insertar un nuevo nodo con el dato 15 en la posición 3
lst.agreg_en(15, 3)

# Impresión de la lista hacia adelante
print("Lista hacia adelante:")
lst.imprimir()

# Impresión de la lista hacia atrás
print("Lista hacia atrás:")
lst.imprimir_at()


"Eliminar nodos duplicados"
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sigu = None  # Apunta al siguiente nodo
        self.ante = None  # Apunta al nodo anterior

class LsitDoble:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo de la lista
        self.fin = None     # Apunta al último nodo de la lista

    def vacia(self):
        return self.inicio is None

    def agreg_princ(self, dato):
        # Agrega un nodo al principio de la lista
        nuev_nodo = Nodo(dato)
        if self.vacia():
            self.inicio = self.fin = nuev_nodo
        else:
            nuev_nodo.sigu = self.inicio
            self.inicio.ante = nuev_nodo
            self.inicio = nuev_nodo

    def agregar_finl(self, dato):
        # Agrega un nodo al final de la lista
        if self.vacia():
            self.agreg_princ(dato)
        else:
            nuev_nodo = Nodo(dato)
            self.fin.sigu = nuev_nodo
            nuev_nodo.ante = self.fin
            self.fin = nuev_nodo

    def elm_dup(self):
        # Elimina los nodos duplicados de la lista
        actual = self.inicio
        vistos = set()  # Conjunto para almacenar los datos ya vistos
        while actual:
            if actual.dato in vistos:
                if actual.ante:
                    actual.ante.sigu = actual.sigu
                if actual.sigu:
                    actual.sigu.ante = actual.ante
                if actual == self.inicio:
                    self.inicio = actual.sigu
                if actual == self.fin:
                    self.fin = actual.ante
            else:
                vistos.add(actual.dato)
            actual = actual.sigu

    def imprimir(self):
        # Imprime los datos de la lista en orden
        actual = self.inicio
        while actual:
            print(actual.dato, end=' ')
            actual = actual.sigu
        print()

    def imprimir_at(self):
        # Imprime los datos de la lista en orden inverso
        actual = self.fin
        while actual:
            print(actual.dato, end=' ')
            actual = actual.ante
        print()

# Creación de la lista con nodos que contienen datos duplicados
lst = LsitDoble()
elem = [1, 1, 2, 3, 4, 4, 5, 6, 6] 
for dato in elem:
    lst.agregar_finl(dato)

# Eliminar los nodos duplicados de la lista
lst.elm_dup()

# Impresión de la lista hacia adelante
print("Lista hacia adelante:")
lst.imprimir()

# Impresión de la lista hacia atrás
print("Lista hacia atrás:")
lst.imprimir_at()

"Invertir la lista"
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sigu = None  # Apunta al siguiente nodo
        self.ante = None  # Apunta al nodo anterior

class LsitDoble:
    def __init__(self):
        self.inicio = None  # Apunta al primer nodo de la lista
        self.fin = None     # Apunta al último nodo de la lista

    def vacia(self):
        return self.inicio is None

    def agreg_princ(self, dato):
        # Agrega un nodo al principio de la lista
        nuev_nodo = Nodo(dato)
        if self.vacia():
            self.inicio = self.fin = nuev_nodo
        else:
            nuev_nodo.sigu = self.inicio
            self.inicio.ante = nuev_nodo
            self.inicio = nuev_nodo

    def agregar_finl(self, dato):
        # Agrega un nodo al final de la lista
        if self.vacia():
            self.agreg_princ(dato)
        else:
            nuev_nodo = Nodo(dato)
            self.fin.sigu = nuev_nodo
            nuev_nodo.ante = self.fin
            self.fin = nuev_nodo

    def inv_lst(self):
        # Invierte el orden de la lista
        actual = self.inicio
        temp = None
        self.fin = self.inicio
        while actual is not None:
            temp = actual.ante
            actual.ante = actual.sigu
            actual.sigu = temp
            actual = actual.ante
        if temp is not None:
            self.inicio = temp.ante

    def imprimir(self):
        # Imprime los datos de la lista en orden
        actual = self.inicio
        while actual:
            print(actual.dato, end=' ')
            actual = actual.sigu
        print()

    def imprimir_at(self):
        # Imprime los datos de la lista en orden inverso
        actual = self.fin
        while actual:
            print(actual.dato, end=' ')
            actual = actual.ante
        print()

# Creación de la lista con al menos 6 nodos
lst = LsitDoble()
for dato in range(1, 7):
    lst.agregar_finl(dato)

# Invertir el orden de la lista
lst.inv_lst()

# Impresión de la lista hacia adelante
print("Lista hacia adelante:")
lst.imprimir()

# Impresión de la lista hacia atrás
print("Lista hacia atrás:")
lst.imprimir_at()

#####EJERCICIOS PARTE 02
"Invertir una cadena"
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def invertir_cadena(cadena):
    pila = Pila()  # Creación de una instancia de la clase Pila
    # Apila cada caracter de la cadena en la pila
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ""  # Variable para almacenar la cadena invertida
    # Desapila cada caracter de la pila y lo agrega a la cadena invertida
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida  # Devuelve la cadena invertida

# Ejemplo de uso
cadena = "Hola mundo"
print("Cadena original:", cadena)
# Invierte la cadena utilizando una pila
print("Cadena invertida:", invertir_cadena(cadena))


"Convertir un número a decimal"

class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def decimal_a_binario(decimal):
    pila = Pila()  # Creación de una instancia de la clase Pila

    # Conversión del número decimal a binario mediante división sucesiva
    while decimal > 0:
        residuo = decimal % 2  # Calcula el residuo de la división por 2
        pila.apilar(residuo)  # Apila el residuo en la pila
        decimal //= 2  # Actualiza el número decimal dividiéndolo por 2

    # Construcción del número binario a partir de los residuos almacenados en la pila
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())  # Desapila y agrega los residuos a la cadena binaria

    return binario  # Devuelve la representación binaria del número decimal

# Lectura del número decimal desde el usuario
numero_decimal = int(input("Ingresa un número decimal: "))

# Conversión del número decimal a binario
binario_resultante = decimal_a_binario(numero_decimal)

# Impresión del resultado
print("El número binario equivalente es:", binario_resultante)

"Evaluar la expresión pos fija"
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def evaluar_expresion_posfija(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila

    # Dividir la expresión en una lista de tokens
    tokens = expresion.split()

    # Operadores válidos
    operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    # Procesar cada token de la expresión
    for token in tokens:
        # Si el token es un operador
        if token in operadores:
            # Desapilar los dos operandos
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            # Realizar la operación y apilar el resultado
            resultado = operadores[token](operando1, operando2)
            pila.apilar(resultado)
        else:
            # Si el token es un número, convertirlo a entero y apilarlo
            pila.apilar(int(token))

    # El resultado final estará en el tope de la pila
    return pila.desapilar()

# Expresión matemática en notación posfija
expresion_posfija = "3 4 + 2 *"

# Evaluación de la expresión
resultado = evaluar_expresion_posfija(expresion_posfija)

# Impresión del resultado
print("El resultado de la expresión posfija es:", resultado)

"Validar operadores anidados"

class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def operadores_anidados(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila

    # Operadores válidos
    operadores = {'(': ')', '[': ']', '{': '}'}

    # Procesar cada caracter de la expresión
    for caracter in expresion:
        # Si el caracter es un operador de apertura, apilarlo
        if caracter in operadores.keys():
            pila.apilar(caracter)
        # Si el caracter es un operador de cierre, verificar si coincide con el operador de apertura en el tope de la pila
        elif caracter in operadores.values():
            # Si la pila está vacía o el operador de cierre no coincide con el operador de apertura en el tope de la pila, la expresión no está bien anidada
            if pila.esta_vacia() or operadores[pila.desapilar()] != caracter:
                return False

    # Si la pila está vacía al final, significa que todos los operadores están bien anidados
    return pila.esta_vacia()

# Expresión matemática a verificar
expresion = "[(5+3)*2-1]"

# Verificar si los operadores están bien anidados en la expresión
if operadores_anidados(expresion):
    print("Los operadores en la expresión están correctamente anidados.")
else:
    print("Los operadores en la expresión NO están correctamente anidados.")


"Ordenar una pila"

class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def ordenar_pila_ascendente(pila):
    pila_temp = Pila()  # Pila temporal para almacenar los elementos ordenados
    # Mientras la pila original no esté vacía
    while not pila.esta_vacia():
        temp = pila.desapilar()  # Desapila un elemento de la pila original
        # Mientras la pila temporal no esté vacía y el elemento desapilado sea menor que el elemento del tope de la pila temporal
        while not pila_temp.esta_vacia() and temp < pila_temp.esta_vacia():
            pila.apilar(pila_temp.desapilar())  # Desapila un elemento de la pila temporal y lo apila en la pila original
        pila_temp.apilar(temp)  # Apila el elemento desapilado en la pila temporal
    return pila_temp  # Devuelve la pila temporal ordenada

# Ejemplo de uso
pila = Pila()
elementos = [5, 2, 8, 1, 9]
for elemento in elementos:
    pila.apilar(elemento)

# Ordenar la pila de manera ascendente
pila_ordenada = ordenar_pila_ascendente(pila)

# Imprimir la pila ordenada
print("Pila ordenada de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar(), end=" ")


"Eliminar duplicados"

class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def eliminar_duplicados_pila(pila):
    pila_temp = Pila()  # Pila temporal para almacenar los elementos únicos
    elementos_vistos = set()  # Conjunto para almacenar los elementos ya vistos
    # Mientras la pila original no esté vacía
    while not pila.esta_vacia():
        elemento = pila.desapilar()  # Desapila un elemento de la pila original
        # Si el elemento no ha sido visto antes
        if elemento not in elementos_vistos:
            pila_temp.apilar(elemento)  # Apila el elemento en la pila temporal
            elementos_vistos.add(elemento)  # Agrega el elemento al conjunto de elementos vistos
    return pila_temp  # Devuelve la pila temporal sin elementos duplicados

# Ejemplo de uso
pila = Pila()
elementos = [3, 5, 2, 5, 7, 3, 8, 2]
for elemento in elementos:
    pila.apilar(elemento)

# Eliminar los elementos duplicados de la pila
pila_sin_duplicados = eliminar_duplicados_pila(pila)

# Imprimir la pila sin elementos duplicados
print("Pila sin elementos duplicados:")
while not pila_sin_duplicados.esta_vacia():
    print(pila_sin_duplicados.desapilar(), end=" ")


"Implementar una calculadora sencilla"
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def evaluar_expresion(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila

    # Dividir la expresión en una lista de tokens
    tokens = expresion.split()

    # Operadores válidos
    operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    # Procesar cada token de la expresión
    for token in tokens:
        # Si el token es un operador
        if token in operadores:
            # Desapilar los dos operandos
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            # Realizar la operación y apilar el resultado
            resultado = operadores[token](operando1, operando2)
            pila.apilar(resultado)
        else:
            # Si el token es un número, convertirlo a flotante y apilarlo
            pila.apilar(float(token))

    # El resultado final estará en el tope de la pila
    return pila.desapilar()

# Función principal de la calculadora
def calculadora():
    while True:
        expresion = input("Ingrese una expresión matemática en notación posfija (o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            print("¡Hasta luego!")
            break
        try:
            resultado = evaluar_expresion(expresion)
            print("El resultado de la expresión es:", resultado)
        except:
            print("Error: Expresión inválida. Intente de nuevo.")

# Ejecutar la calculadora
calculadora()


"Comprobar palíndromos"
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para ignorar diferencias de mayúsculas y minúsculas
    pila = Pila()  # Crear una instancia de la clase Pila

    # Apilar los caracteres de la mitad izquierda de la palabra (o de la parte inicial si la longitud es impar)
    for caracter in palabra[:len(palabra)//2]:
        pila.apilar(caracter)

    # Desapilar y comparar los caracteres de la pila con los de la mitad derecha de la palabra
    for caracter in palabra[len(palabra)//2 + len(palabra) % 2:]:
        if caracter != pila.desapilar():
            return False

    return True

# Ejemplo de uso
palabra = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')


"Simular el proceso de deshacer (undo)"
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la lista que representa la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Comprueba si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agrega un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento del tope de la pila

# Clase para el sistema de "deshacer"
class SistemaDeshacer:
    def __init__(self):
        self.pila_acciones = Pila()  # Pila para almacenar las acciones realizadas
        self.pila_deshacer = Pila()  # Pila para almacenar las acciones deshechas

    # Método para realizar una acción
    def realizar_accion(self, accion):
        self.pila_acciones.apilar(accion)  # Agregar la acción a la pila de acciones
        # Limpiar la pila de deshacer, ya que una nueva acción impide deshacer acciones anteriores
        while not self.pila_deshacer.esta_vacia():
            self.pila_deshacer.desapilar()

    # Método para deshacer la última acción
    def deshacer_accion(self):
        if not self.pila_acciones.esta_vacia():
            accion_deshacer = self.pila_acciones.desapilar()  # Obtener la última acción realizada
            self.pila_deshacer.apilar(accion_deshacer)  # Agregar la acción deshecha a la pila de deshacer

    # Método para rehacer la última acción deshecha
    def rehacer_accion(self):
        if not self.pila_deshacer.esta_vacia():
            accion_rehacer = self.pila_deshacer.desapilar()  # Obtener la última acción deshecha
            self.pila_acciones.apilar(accion_rehacer)  # Agregar la acción de nuevo a la pila de acciones

    # Método para imprimir el estado actual del sistema
    def imprimir_estado(self):
        print("Acciones realizadas:", self.pila_acciones.items)
        print("Acciones deshechas:", self.pila_deshacer.items)


# Ejemplo de uso
sistema = SistemaDeshacer()

# Realizar algunas acciones
sistema.realizar_accion("Editar texto")
sistema.realizar_accion("Eliminar elemento")
sistema.realizar_accion("Guardar cambios")

# Imprimir el estado actual del sistema
print("Estado actual del sistema:")
sistema.imprimir_estado()

# Deshacer una acción
sistema.deshacer_accion()

# Imprimir el estado actual del sistema después de deshacer
print("\nEstado después de deshacer una acción:")
sistema.imprimir_estado()

# Rehacer una acción
sistema.rehacer_accion()

# Imprimir el estado actual del sistema después de rehacer
print("\nEstado después de rehacer una acción:")
sistema.imprimir_estado()


