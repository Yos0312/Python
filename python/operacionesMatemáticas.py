#EJEMPLO 2. Operaciones Matemáticas

#IMPORTAR LIBRERÍAS DE FUNCIONES MATEMÁTICAS
#SINTAXIS: 
import math



#ENTRADA DE DATOS
#Crear o declarar variables y constantes
número_1 = float(input("Escribe el 1er número:"))
número_2 = float(input("Escribe el 2do número: "))



#PROCESOS(Cálculos u Operaciones Matemáticas y/o Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1,número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2,3) 

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cubica_3 = pow(27,1/3)

módulo_residuo = número_1 % número_2






#SALIDA DE DATOS
print("La suma es igual a",suma)
print("La suma es igual a " + str(suma)) #CONCATENACIÓN (unión de texto)
print("La resta es igual a ",round(resta,2))
print("La multiplicación es igual a", multiplicación)
print("La división  es igual a", división)
print("La potencia de 10 a la 2 es igual a", potencia_1)
print("La potencia de 10 a la 2 es igual a", potencia_2)
print("el cuadrado de 10 es", cuadrado)
print( "el cubo es igual a", cubo)
print("La raíz cuadrada es igual a", raíz_cuadrada_1)
print("La raíz cuadrada  es igual a", raíz_cuadrada_2)
print("La raíz cuabica es igual a", raíz_cubica_3)
print("el residuo es igual a", módulo_residuo)