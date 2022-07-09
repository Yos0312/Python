#EJERCICOP FUNCIONES Y ARREGLOS



import string


marca_de_tenis = ["Puma", "Nike", "Adidas"]

precio = [1800, 2500, 2300]

def Imprimir_ASC (a):
    a.sort()
    print(a )

def Imprimir_DESC (a):
    a.reverse()
    print(a)


respuesta = "si"
while (respuesta == "si" or respuesta == "Si" or respuesta == "Y"):

    #ENTRADA
    print("          Menú")
    print("1. Lista ordenada ASC")
    print("2. Lista ordenada DESC")
    print("3. Agregar una marca y un precio a cada arreglo")
    print("4. Modificar un elemento de cada arreglo")
    print("5. Limpiar o vaciar los arreglos")

    opción = float(input("Selecionar opción "))




    #Menu

    if(opción == 1):
     Imprimir_ASC(marca_de_tenis) 
     Imprimir_ASC(precio)

    elif(opción ==  2):
        Imprimir_DESC (marca_de_tenis) 
        Imprimir_DESC(precio)

    elif(opción == 3):
        n= str(marca_de_tenis[1] ) + str(precio[1] )
        p= str(marca_de_tenis[0] ) + str(precio[0] )
        a= str(marca_de_tenis[2] ) + str(precio[2] )
        print ("3. Agregar una marca y un precio a cada arreglo")
        print (n,p,a)

    elif ( opción == 4 ):
        print("4. Modificar un elemento de cada arreglo")
    
        marca_de_tenis[0]="Charly"
        marca_de_tenis[1]="Converse"
        marca_de_tenis[2]="vans"
        Imprimir_ASC(marca_de_tenis)
        Imprimir_DESC(marca_de_tenis)
        
        #modificar = float(input("Cúal vas a modificar: "))
        #if(modificar == 1):
        #o1 = string ("nombre ") 
        #marca_de_tenis[0] = o1

    elif(opción==5):
        marca_de_tenis.clear()
        precio.clear()
        Imprimir_ASC (marca_de_tenis)
        Imprimir_ASC (precio)

    respuesta = input("¿Deseas continuar?: ")

