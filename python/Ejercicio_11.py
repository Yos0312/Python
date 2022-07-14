#EJERCICIO 11 



def Sumar(a, b):  
    return a + b
def Sumar(a,c):
    return a+c

def Sumar(b,c):
    return b+c
def Restar(b,c):
    return b-c
def Restar(a,c):
    return a-c
def Restar(a,b):
    return a-b
def Multiplicar (a,b):
    return a * b
def Multiplicar (a,c):
    return a * c
def Multiplicar (b,c):
    return b * c

n1= float(input("Escribe el 1er numero: "))
n2= float(input("Escribe el 2do numero: "))
n3= float(input("Escribe el 3er numero: "))

numeros = [Sumar(n1, n2),Sumar(n1,n3),Sumar(n2,n3),Restar(n2,n3), Restar(n1,n2), Restar(n1,n3), Multiplicar (n1,n2), Multiplicar (n1,n3), Multiplicar (n2,n3) ]

numeros.append(10)


print("Números: ", numeros)