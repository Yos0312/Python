#Ejercicio 6 numero par o inpar

#Entrada de datos 

número = float(input("Escribe un número: "))

#procesos
residuo = número % 2

if(residuo == 0 ):
    print ("PAR")
else:
    print ("IMPAR")