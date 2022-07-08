# EJERCICIO 1 PROMEDIO 

#ENTRADA DE DATOS
calificación_1 = float(input("1ra Calificación: "))
calificación_2 = float(input("2da Calificación: "))
calificación_3 = float(input("3ra Calificación: "))



#PROCESOS 
suma = calificación_1 + calificación_2 + calificación_3
promedio = suma / 3
if (promedio > 6 and promedio <= 10 ):            # rango >6 y 10
    print("Aprobado ")
elif ( promedio == 6 ) :
    print ("PANSASO")                        #Rango =6
elif(promedio < 6 and promedio >= 0):                          # rango <6 y >=0
    print("Reprobado")
elif(promedio <0 or promedio > 10):    #rango <0 o > 10
    print("ERROR EN PROMEDIO")


#SALIDA DE DATOS 
print("El promedio es ",round(promedio,2))