import math

'''
Ejercicio parte 01:
Operaciones Básicas:
1) Realiza la suma, resta, multiplicación y división de 
dos números ingresados por el usuario.

'''
a=int(input())
if a==1:
    n1=int(input())
    n2=int(input())
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)
    print(n1/n2)

    
elif a==2:
    n1=int(input())
    if n1%2!=0:
        print(n1,"es impar")
    else:
        print(n1,"es par")
elif a==3:
    b=int(input())
    a=int(input())
    print((b*a)/2)
elif a==4:
    n1=int(input())
    i=1
    res=1
    while i<=n1:
        res*=i
        i+=1
    print(res)
elif a==5:
    n1=int(input())
    i=2
    van=0
    while i<n1:
        if n1%i==0:
            van+=1
        i+=1
    if  van==0:
        print("es primo")
    else:
        print("no es primo")
elif a==6:  
    a="holamundo"
    res=""
    for b in a:
        res=b+res
    print(res)
elif a==7:   
    n1=int(input())
    n2=int(input())
    res=0
    for a in range(n1+1,n2):#tomando los valores seria:          range(n1,n2+1)
        if a%2==0:
            res+=a
    
    print(res)
elif a==8:
    res=[]
    for i in range(1,11):
        res.append(i**2)
    print(res)
elif a==9:
    cont=0
    txt="holamundo"
    for i in txt:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            cont+=1
    print(cont)
elif a==10:
    i=0
    a=0
    b=1
    van=0
    while i<10:
        van=a
        a=b
        print(a)
        b=a+van
        i+=1
elif a==11:
    n1=int(input("ingrese el numero de elementos: "))
    i=0
    a=[]
    while i<n1:
        l=int(input())
        a.append(l)
        i+=1
    print(a)
    res=sorted(a)
    print(res)
elif a==12:
    pl=input()
    pl=pl.replace(" ","")
    inve=""
    for b in pl:
        inve=b+inve
    if inve==pl:
        print("si es palindromo")
    else:
        print("no es palindromo")
elif a==13:
    n1=int(input())
    for b in range(0,13):
        print(n1," x ",b," = ",n1*b)

elif a==14:
    n1=int(input())
    res=(n1**2)*math.pi
    print(res)
elif a==15:
    nmr=input()
    res=0
    for i in nmr:
        res+=int(i)
    print(res)