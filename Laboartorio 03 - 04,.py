
import numpy as np
import random

a=int(input())

if a==1:#ejercicio 1
    def par(a):
        if a>=0:
            if (100-a)%2==0:
                print(100-a)
            return par(a-1)
    par(100)
            
elif a==2:#ejercicio 2
    n=int(input())
    def par(a):
        if a!=0:

            return a+par(a-1)
        else:
            return 0
    print(par(n))

elif a == 3:
    def imprimir_piramide_ascendente(n):
        if n > 0:
            imprimir_piramide_ascendente(n - 1)
            print(" " * (n - 1) + "".join(str(i) for i in range(1, n + 1)))

    print("\nEjercicio 3: Pirámide de Números del 1 al n")
    imprimir_piramide_ascendente(5)  # Puedes cambiar el valor de n

elif a == 4:
    def imprimir_piramide_descendente(n):
        if n > 0:
            print(" " * (n - 1) + "".join(str(i) ) for i in range(1, n + 1))
            imprimir_piramide_descendente(n - 1)

    print("\nEjercicio 4: Pirámide de Números Invertidos del 1 al n")
    imprimir_piramide_descendente(5)  # Puedes cambiar el valor de n


elif a == 5:
    def tabla_multiplicar(n, multiplicador=1):
        if multiplicador <= 10:
            print(f"{n} x {multiplicador} = {n * multiplicador}")
            tabla_multiplicar(n, multiplicador + 1)

    print("\nEjercicio 5: Tabla de Multiplicar del n")
    n = 7  # Puedes cambiar el valor de n
    tabla_multiplicar(n)




elif a == 6:
    matriz_reales = np.random.rand(3, 3)
    print("Matriz de números reales aleatorios:")
    print(matriz_reales)


elif a == 7:
    matriz_complejos = np.random.rand(3, 3) + 1j * np.random.rand(3, 3)
    print("\nMatriz de números complejos aleatorios:")
    print(matriz_complejos)


elif a == 8:
    matriz_de_matrices = np.random.rand(2, 3, 3)

    print("\nMatriz de matrices aleatorias:")

    print(matriz_de_matrices)


elif a == 9:
    if 'matriz_reales' not in locals():

        matriz_reales = np.random.rand(3, 3)

    elemento_central = matriz_reales[1, 1]  # Para una matriz de 3x3

    print("\nElemento central de la matriz de números reales:")

    print(elemento_central)


elif a == 10:
    matriz1 = np.random.rand(2, 2)
    matriz2 = np.random.rand(2, 3)

    suma_matrices = matriz1 + matriz2

    print("\nSuma de dos matrices de diferentes tamaños:")
    print(suma_matrices)


elif a == 11:
    if 'matriz_a_multiplicar' not in locals():
        matriz_a_multiplicar = np.random.rand(2, 2)

    numero_multiplicador = np.random.rand()

    matriz_resultante = matriz_a_multiplicar * numero_multiplicador

    print("\nMatriz multiplicada por un número:")
    print(matriz_resultante)


elif a == 12:
    matriz_para_media = np.random.rand(3, 3)

    media_elementos = np.mean(matriz_para_media)

    print("\nMedia de los elementos de la matriz:")
    print(media_elementos)


elif a==13:#ejercicio 1.1
    
    matrizc=np.random.randint(0,100,size=(100,100))

    for i in range(100):

        for j in range(100):

            print(matrizc[i][j],end=" ")

        print()


elif a==14:
    matrizc = np.random.randint(0, 10, size=(3, 3))

    print(matrizc)

    print("Mda: ", np.mean(matrizc))
    print("Mdna: ", np.median(matrizc))
    print("D e: ", np.std(matrizc))
elif a==15:

    matrizc = np.random.randint(0, 10, size=(3, 3))
    
    print(matrizc)

    def mx(mt):

        res=np.amax(mt)

        return res
    
    print(mx(matrizc))

elif a==16:


    def submatriz_mayor_suma(matriz):

        filas, columnas = matriz.shape

        max_suma = float('-inf')
        mejor_submatriz = None

        for i in range(filas):

            temp = np.zeros(columnas)

            for j in range(i, filas):

                temp += matriz[j, :]
                suma_kadane, inicio, fin = kadane(temp)

                if suma_kadane > max_suma:

                    max_suma = suma_kadane
                    mejor_submatriz = matriz[i:j+1, inicio:fin+1]

        return mejor_submatriz

    def kadane(arr):
        max_suma_global = float('-inf')

        max_suma_local = 0
        inicio_temp = 0
        inicio_global = 0
        fin_global = 0

        for i, val in enumerate(arr):
            if max_suma_local <= 0:
                max_suma_local = val
                inicio_temp = i
            else:
                max_suma_local += val

            if max_suma_local > max_suma_global:
                max_suma_global = max_suma_local
                inicio_global = inicio_temp
                fin_global = i

        return max_suma_global, inicio_global, fin_global

    matriz_ejemplo = np.array([[1, 2, -1, 4],
                            [-3, 0, 2, 1],
                            [2, -1, 4, -2]])

    submatriz_resultante = submatriz_mayor_suma(matriz_ejemplo)
    print("Submatriz de mayor suma:")

    print(submatriz_resultante)
    
elif a==17:
    def matriz_covarianza(matriz1, matriz2):
        
        if matriz1.shape[1] != matriz2.shape[1]:
            raise ValueError("Ambas matrices deben tener el mismo número de columnas")

        matriz_combinada = np.vstack((matriz1, matriz2))

        covarianza = np.cov(matriz_combinada, rowvar=False)

        return covarianza


    matriz1=np.random.randint(0, 10, size=(3, 3))
    print(matriz1)

    print()

    matriz2=np.random.randint(20, 10, size=(3, 3))
    print(matriz2)

    matriz_cov = matriz_covarianza(matriz1, matriz2)

    print("Matriz de Covarianza:")
    print(matriz_cov)