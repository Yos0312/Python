#EJERCICIO 5 CALCULAR FORMULA GENERAL 
#libreria 
import math

#DATOS DE ENTRADA
valor_a = float(input("valor de a: "))

valor_b = float(input("valor de b: "))

valor_c = float(input("valor de c: "))

# PROCESOS
#raíz_cuadrada_1 = math.sqrt(9)


#x1 = ((-valor_b)- math.sqrt((valor_b ** 2)-(4*(valor_a * valor_c)))

valor_x1 = (-valor_b - (math.sqrt((valor_b ** 2)- (4* valor_a * valor_c)))) / (2 * valor_a)
valor_x2 = (-valor_b + (math.sqrt((valor_b ** 2) - (4 * valor_a * valor_c)))) / (2 * valor_a)



# SALIDA DE DATOS 

print("x 1 = ", round(valor_x1,4))

print("x 2 = ", round(valor_x2,4))