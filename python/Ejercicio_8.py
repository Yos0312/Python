#Ejercicio 8



from re import I


numero = float(input("Insterte número:"))

if ( numero < 0 and numero > -100 ):
    for i in range(-1, -100, -2):
        print(i)

elif ( numero > 0 and numero < 100 ):
    j = 2
    while (j <= 100):
        print(j)
        j = j + 2
     
else :
     print("No válido")


   




