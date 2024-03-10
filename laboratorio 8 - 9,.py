a = int(input())  

if a == 1:  
    def val_edad():  # Define una función para validar la edad
        edad = float(input("Ingrese edad: "))  # Solicita al usuario que ingrese la edad como un número decimal
        assert 0 < edad <= 90, "Edad no es válida"  # Verifica que la edad esté en el rango válido
        print("Edad válida")  # Imprime un mensaje si la edad es válida

    try:
        val_edad()  # Llama a la función para validar la edad
    except AssertionError as er:
        print(er)  # Captura y muestra cualquier error de validación de la edad

elif a == 2:  
    def val_tip(tip, s):  # Define una función para validar el tipo de datos
        assert isinstance(tip, s), "Los tipos de datos no son del mismo tipo de variable"  # Verifica si los tipos de datos son del mismo tipo de variable
        print("Los datos dados son del mismo tipo de variable")  # Imprime un mensaje si los tipos de datos son del mismo tipo de variable

    try:
        tp = 10
        val_tip("hola", int)  # Llama a la función para validar el tipo de datos
    except AssertionError as er:
        print(er)  # Captura y muestra cualquier error de validación del tipo de datos

elif a == 3: 
    def val_nota():  # Define una función para validar la nota
        nota = float(input("Ingrese nota: "))  # Solicita al usuario que ingrese la nota como un número decimal
        assert 0 <= nota <= 20, "La nota no es válida"  # Verifica que la nota esté en el rango válido
        print("La nota es válida")  # Imprime un mensaje si la nota es válida

    try:
        val_nota()  # Llama a la función para validar la nota
    except AssertionError as er:
        print(er)  # Captura y muestra cualquier error de validación de la nota

elif a == 4:  
    def val_list(lst):  # Define una función para validar una lista
        assert len(lst) > 0, "La lista está vacía"   # Verifica que la lista no esté vacía
        print("La lista no está vacía.")   # Imprime un mensaje si la lista no está vacía

    listp = [1,2]   # Crea una lista con elementos
    try:
        val_list(listp)   # Llama a la función para validar la lista
    except AssertionError as er:
        print(er)   # Captura y muestra cualquier error relacionado con la validación de la lista

elif a == 5:  
    def val_obj(ob1, ob2):  # Define una función para validar objetos
        assert ob1 == ob2, "Los objetos son diferentes"  # Verifica si los objetos son iguales
        print("Los objetos son iguales")  # Imprime un mensaje si los objetos son iguales

    objet1 = [1, 2, 3]  # Crea un objeto (lista) con elementos
    objet2 = [1, 2, 3]  # Crea otro objeto (lista) con elementos
    try:
        val_obj(objet1, objet2)  # Llama a la función para validar los objetos
    except AssertionError as er:
        print(er)  # Captura y muestra cualquier error relacionado con la validación de los objetos

elif a == 6: 
    def contwh(b):  # Define una función para contar en un ciclo while
        cont = 0
        while cont < b:  # Realiza un ciclo while mientras cont sea menor que b
            cont += 1
        assert cont > 0, "El ciclo while no se ejecutó ni una vez"   # Verifica si el ciclo while se ejecutó al menos una vez
        print("El ciclo while se ejecutó al menos una vez")   # Imprime un mensaje indicando que el ciclo while se ejecutó al menos una vez

    try:
        contwh(1)   # Llama a la función para contar en un ciclo while con b=1
    except AssertionError as er:
        print(er)   # Captura y muestra cualquier error relacionado con la ejecución del ciclo while


elif a == 7:  
    def f1():  # Define una función que devuelve el valor 10
        return 10

    def aseg(f, b):  # Define una función para asegurar que un valor sea el esperado
        assert f == b, "El valor de la función no es el esperado"  # Verifica si el valor de la función es igual al valor esperado
        print("El valor fue el esperado")  # Imprime un mensaje si el valor es el esperado

    try:
        aseg(f1(), 0)  # Llama a la función 'aseg' con los valores devueltos por 'f1' y 0 como parámetros
    except AssertionError as er:
        print(er)  # Captura y muestra cualquier error relacionado con la validación del valor de la función


elif a == 8:  
    def f1():  # Define una función que devuelve el valor 10
        return 10

    def aseg(f, b):  # Define una función para asegurar que un valor sea el esperado
        assert f == b, "El valor de la función no es el esperado"   # Verifica si el valor de la función es igual al valor esperado
        print("El valor fue el esperado")   # Imprime un mensaje si el valor es el esperado

    try:
        aseg(f1(), 0)   # Llama a la función 'aseg' con los valores devueltos por 'f1' y 0 como parámetros
    except AssertionError as er:
        print(er)   # Captura y muestra cualquier error relacionado con la validación del valor de la función

elif a == 9:  
    try:
        import turtle   # Intenta importar el módulo turtle
        print("El módulo se ha importado correctamente.")   # Muestra un mensaje si el módulo se importa correctamente
    except ImportError:
        print("Error al importar el módulo. Asegúrate de que el nombre del módulo es correcto y está instalado.")  
        # Muestra un mensaje si hay un error al importar el módulo



elif a == 10:  #Todos los ejerccios de 10 hasta 15
    class Nodo:
        # Construimos el Nodo
        def __init__(self, dato=0, siguiente=None):
            self.dato = dato  # Valor almacenado en el nodo
            self.siguiente = siguiente  # Referencia al siguiente nodo

    class ListaEnlazada:
        # Construimos  la Lista Enlazada
        def __init__(self):
            self.cabeza = None  # Inicializa la cabeza de la lista como None

        # Agregar un elemento al final de la lista
        def agregar_al_final(self, dato):
            if not self.cabeza:
                # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
                self.cabeza = Nodo(dato=dato)
            else:
                # Si la lista no está vacía, recorrer hasta el final y agregar el nuevo nodo
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = Nodo(dato=dato)
        
# 10 Desarrollar el código de buscar nodo en la lista enlazada simple
        def buscar(self, dato):    # creamos la función Buscar un nodo en la lista
            actual = self.cabeza
            while actual:
                if actual.dato == dato:
                    return True  # Retorna True si encuentra el dato
                actual = actual.siguiente
            return False  # Retorna False si no encuentra el dato

#Suma de Nodos
#11. Implementa una función que sume todos los nodos de una lista enlazada simple
        
        def suma_de_nodos(self):
            suma = 0
            actual = self.cabeza
            while actual:
                suma += actual.dato  # Acumula el valor del nodo en suma
                actual = actual.siguiente
            return suma

#Longitud de la Lista
#12. Crea una función que devuelva la longitud de una lista enlazada simple
       
        def longitud(self):
            contador = 0
            actual = self.cabeza
            while actual:
                contador += 1  # Incrementa el contador por cada nodo
                actual = actual.siguiente
            return contador

#Concatenar Listas
#13. Implementa una función que concatene dos listas enlazadas simples
        
        def concatenar(self, otra_lista):  #cremos la función para conacatenar la lista enlazaad simple
            if self.cabeza is None:
                # Si la lista actual está vacía, simplemente asigna la otra lista
                self.cabeza = otra_lista.cabeza
            else:
                # Si no, recorre hasta el final de la lista actual y enlaza la otra lista
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = otra_lista.cabeza

#Eliminar Duplicados
#14. Crea una función que elimine los nodos duplicados de una lista enlazada simple
        def eliminar_duplicados(self):        # 14. creamos la funcion para eliminar duplicados de una lista enlazada simple
            previo = None
            actual = self.cabeza
            valores_vistos = set()
            while actual:
                if actual.dato in valores_vistos:
                    # Si el valor ya fue visto, se elimina el nodo actual del enlace
                    previo.siguiente = actual.siguiente
                else:
                    # Si no, se añade el valor a los vistos y se actualiza el nodo previo
                    valores_vistos.add(actual.dato)
                    previo = actual
                actual = actual.siguiente

#Invertir Lista
#15. Implementa una función que invierta el orden de una lista enlazada simple
        def invertir_lista(self):       # Cremamos la función para Invertir la lista enlazada simple
            anterior = None
            actual = self.cabeza
            while actual:
                siguiente_temp = actual.siguiente  # Guarda referencia al siguiente nodo
                actual.siguiente = anterior  # Invierte el enlace actual hacia el anterior
                anterior = actual  # Actualiza el anterior al nodo actual
                actual = siguiente_temp  # Avanza al siguiente nodo
            self.cabeza = anterior  # La nueva cabeza es el último nodo procesado



        # Crear una nueva lista enlazada
    lista = ListaEnlazada()

    # Agregar algunos elementos a la lista
    
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_final(2)  # Duplicado para demostrar eliminar_duplicados
    lista.agregar_al_final(4)

    # Buscar un elemento en la lista
    print("--------------------------------------< 10 >-------------------------------------------------")
    print("¿Está el 3 en la lista?", lista.buscar(3))  # Debería ser True
    print("¿Está el 5 en la lista?", lista.buscar(5))  # Debería ser False

    # Sumar todos los nodos de la lista
    print("--------------------------------------< 11 >-------------------------------------------------")
    print("Suma de todos los nodos:", lista.suma_de_nodos())  # Debería ser 12 antes de eliminar duplicados

    # Obtener la longitud de la lista
    print("--------------------------------------< 12 >-------------------------------------------------")
    print("Longitud de la lista:", lista.longitud())  # Debería ser 5 antes de eliminar duplicados

    # Eliminar duplicados y volver a verificar suma y longitud
    print("--------------------------------------< 13 >-------------------------------------------------")
    lista.eliminar_duplicados()
    print("Suma de todos los nodos después de eliminar duplicados es:", lista.suma_de_nodos())  # Debería ser 10
    print("Longitud de la lista después de eliminar duplicados es:", lista.longitud())  # Debería ser 4

    # Crear otra lista enlazada y concatenar con la primera lista
    print("--------------------------------------< 14 >-------------------------------------------------")
    otra_lista = ListaEnlazada()
    otra_lista.agregar_al_final(5)
    otra_lista.agregar_al_final(6)
    lista.concatenar(otra_lista)
    print("Longitud de la lista después de concatenar otra lista es:", lista.longitud())  # Debería ser 6

    # Invertir la lista y mostrar la longitud (debería ser la misma)
    
    lista.invertir_lista()
    print("--------------------------------------< 15 >-------------------------------------------------")
    print("Longitud de la lista después de invertirla es:", lista.longitud())  # Debería ser 6
