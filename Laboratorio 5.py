a=int(input())
if a ==1:
    nmr=int(input("numero de elementos del conjunto : "))
    def conj():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=int(input("Elemento "+str(b)+" :"))

            i=2
            van=0
            while i<nm:
                if nm%i==0:
                    van+=1
                i+=1
            if  van==0:
                
                cnj.add(nm)
        return cnj
    print("El siguiente conjunto esta compuesto por los numeros primos: ", conj())


elif a ==2:
    nmr=int(input("numero de elementos del conjunto : "))
    pd=input("palabra determinada: ")
    def plb():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=input("palabra "+str(b)+" :")
            if pd ==nm[0]:
                cnj.add(nm)
        return cnj
    print(plb())
elif a ==3:
    nmr=int(input("numero de elementos del conjunto : "))
    n=int(input("numero determinado : "))
    def conj():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=int(input("Elemento "+str(b)+" :"))
            if nm%n==0:
                cnj.add(nm)
        return cnj
    print("Los números que son divisibles por: ",n,"es el sigueinte conjunto : ",conj())
elif a ==4:

    def conj():
        nmr=int(input("numero de elementos del conjunto1 : "))
   
        cnj1=set()
        
        for b in range(1,nmr+1):
            nm1=int(input("nmr "+str(b)+" :"))
            cnj1.add(nm1)
    
        nmr=int(input("numero de elementos del conjunto2 : "))
        cnj2=set()
        
        for b in range(1,nmr+1):
            nm2=int(input("nmr "+str(b)+" :"))
            cnj2.add(nm2)
        return cnj1.intersection(cnj2)
    print(conj())

elif a ==5:
    def conj():
        nmr=int(input("numero de elementos del conjunto1 : "))
   
        cnj1=set()
        
        for b in range(1,nmr+1):
            nm1=int(input("nmr "+str(b)+" :"))
            cnj1.add(nm1)
    
        nmr=int(input("numero de elementos del conjunto2 : "))
        cnj2=set()
        
        for b in range(1,nmr+1):
            nm2=int(input("nmr "+str(b)+" :"))
            cnj2.add(nm2)
        return cnj1-cnj1.intersection(cnj2)
    print(conj())
elif a ==6:
    def conj():
        nmr=int(input("numero de elementos del conjunto1 : "))
   
        cnj1=set()
        
        for b in range(1,nmr+1):
            nm1=int(input("nmr "+str(b)+" :"))
            cnj1.add(nm1)
    
        nmr=int(input("numero de elementos del conjunto2 : "))
        cnj2=set()
        
        for b in range(1,nmr+1):
            nm2=int(input("nmr "+str(b)+" :"))
            cnj2.add(nm2)
        return cnj2-cnj1.intersection(cnj2)
    print(conj())

elif a ==7:
    
    nmr=int(input("numero de elementos del conjunto : "))
    
    def plb():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=input("palabra "+str(b)+" :")
            cnj.add(nm)
        
        cnjr=set()
        for pl in cnj:
            for pb in cnj:
                if pl!=pb:
                    if sorted(pl)==sorted(pb):
                        cnjr.add(pl)
                        cnjr.add(pb)
        
        return cnjr
    print(plb())
    
elif a ==8:
    nmr=int(input("numero de elementos del conjunto : "))
    
    def plb():    
        nm=0
        cnjr=set()
        for b in range(0,nmr):
            nm=input("palabra "+str(b)+" :")
            if nm==nm[::-1]:
                cnjr.add(nm)
        
        
        
        return cnjr
    print(plb())

elif a ==9:
    nmr=int(input("numero de elementos del conjunto : "))
    n=int(input("longitud determinado : "))
    def conj():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=input("nmr "+str(b)+" :")
            if len(nm)==n:
                cnj.add(nm)
        return cnj
    print(conj())

elif a ==10:
    nmr=int(input("numero de elementos del conjunto : "))
    pd=input("palabra determinada: ")
    def plb():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=input("Palabra "+str(b)+" :")
            if pd in nm:
                cnj.add(nm)
        return cnj
    print(plb())
elif a ==11:
    nmr=int(input("numero de elementos del conjunto : "))
    def plb():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=int(input("Numero "+str(b)+" :"))
            cnj.add(nm)
        return sorted(cnj)
    print(plb())


elif a ==12:
    nmr=int(input("numero de elementos del conjunto : "))
    def plb():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=int(input("palabra ",str(b)," :"))
            cnj.add(nm)
        cnjr=sorted(cnj)
        cnjr=cnjr[::-1]
        return cnjr
    print(plb())

elif a ==13:

    nmr = int(input("Número de elementos del conjunto: "))

    def plb():
        cnj = set()
        cnjr = set()
        nmv = set()

        for i in range(nmr):
            nm = int(input("Número: "))
            if nm in cnj:
                cnjr.add(nm)
            else:
                nmv.add(nm)
            cnj.add(nm)

        return cnjr

    print(plb())

elif a ==14:
    nmr = int(input("Número de elementos del conjunto: "))

    def plb():
        cnj = set()
        cnjr = set()
        nmv = set()

        for i in range(nmr):
            nm = int(input("Número: "))
            if nm in cnj:
                cnjr.add(nm)
            else:
                nmv.add(nm)
            cnj.add(nm)

        return cnj.difference(cnjr)

    print(plb())


if a ==15:
    nmr=int(input("numero de elementos del conjunto : "))
    def conj():    
        cnj=set()
        nm=0
        for b in range(1,nmr+1):
            nm=int(input("nmr "+str(b)+" :"))

            i=2
            van=0
            while i<nm:
                if nm%i==0:
                    van+=1
                i+=1
            if  van==0:
                
                cnj.add(nm)
        return sorted(cnj)
    print("Los nuumeros primos ordenados de menor a mayor son los siguientes: ", conj())

elif a ==16:
    nmr=int(input("numero de elementos del conjunto : "))
    
    def plb():    
        nm=0
        cnjr=set()
        for b in range(1,nmr+1):
            nm=input("palabra "+str(b)+" :")
            if nm==nm[::-1]:
                cnjr.add(nm)
        
        
        
        return sorted(cnjr)
    print(plb())

elif a ==17:
    nmr=int(input("numero de elementos del conjunto : "))
    n=int(input("longitud determinado : "))
    def conj():    
        cnj=set()
        nm=0
        for b in range(1,n+1):
            nm=input("Palabra " + str(b)+ " :")
            if len(nm)==n:
                cnj.add(nm)
        return sorted(cnj)
    print(conj())

elif a ==18:
    def filtrar_y_ordenar_palabras(palabras, letra):
        # Filtrar palabras que contienen la letra determinada
        palabras_filtradas = {palabra for palabra in palabras if letra in palabra}
        # Ordenar de mayor a menor alfabéticamente y convertir a conjunto
        palabras_ordenadas = sorted(palabras_filtradas, reverse=True)
        return set(palabras_ordenadas)


    palabras = {"arbol", "sol", "luz", "algoritmo", "oro"}
    letra = "o"
    print(filtrar_y_ordenar_palabras(palabras, letra))

elif a ==19:
    def filtrar_y_ordenar_palabras_por_letra(palabras, letra):
        # Filtrar palabras que contienen la letra determinada
        palabras_filtradas = {palabra for palabra in palabras if letra in palabra}
        # Ordenar de mayor a menor (por longitud) y convertir a conjunto
        palabras_ordenadas = sorted(palabras_filtradas, key=lambda x: len(x), reverse=True)
        return set(palabras_ordenadas)

    # Ejemplo de uso
    palabras = {"hola", "mundo", "arbol", "sol", "luz", "algoritmo"}
    letra = "o"
    print(filtrar_y_ordenar_palabras_por_letra(palabras, letra))


elif a==20:
        # Definimos la función 'filtrar_palindromos' que toma dos parámetros: 'palabras' y 'longitud'.
    def filtrar_palindromos(palabras, longitud):
        # Creamos una lista vacía llamada 'palindromos' donde almacenaremos las palabras que cumplan las condiciones.
        palindromos = []
        # Iteramos sobre cada palabra en el conjunto de 'palabras'.
        for palabra in palabras:
            # Verificamos si la palabra es un palíndromo y si tiene la longitud deseada.
            if palabra == palabra[::-1] and len(palabra) == longitud:
                # Si cumple las condiciones, la añadimos a la lista 'palindromos'.
                palindromos.append(palabra)
        # Ordenamos la lista 'palindromos' por longitud de sus elementos, de menor a mayor.
        palindromos_ordenados = sorted(palindromos, key=len)
        # Convertimos la lista ordenada en un conjunto para eliminar duplicados y devolvemos este conjunto.
        return set(palindromos_ordenados)

    # Solicitar al usuario el conjunto de palabras y la longitud determinada
    conjunto_de_palabras = set(input("Ingrese las palabras separadas por espacio: ").split())
    longitud_determinada = int(input("Longitud de los palíndromos: "))

    # Llamar a la función y mostrar el resultado
    conjunto_resultante = filtrar_palindromos(conjunto_de_palabras, longitud_determinada)
    print("Palíndromos ordenados:", conjunto_resultante)
