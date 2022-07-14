#ARREGLOS / LISTAS: Colecciones de valores de un mismo o diferente tipo de datos
#SINTAXIS:
#Declarar o crear un arreglo o lista
#nombre_del_arreglo = [elementos / valores]

#ENTRADA DE DATOS

nombres              =   ["Jocelyn","Eduardo","Juan"]
#'Indice (index)            0             1        2
edad              = [20, 30, 18]
#indice (index)      0   1   2
arreglo_lista = [8, 6.3, "Hola", True]
#                0   1      3      4
#OPERACIONES CON ARREGLOS/LISTA
#Modificar un elemento del arreglo 
nombres[0] = "Jocelyn Lucía"
edad [1] = 35
arreglo_lista[3]= False

#Agregar un elemento un elemento al arreglo 
nombres.append("Paola")
edad.append(10)
arreglo_lista.append("Adios")

#Ordenar los elementos del arreglo de forma alfabética 
nombres.sort()
edad.sort()

#reverse arreglo de forma alfabetica DESCENDENTE
#sort arreglo de forma ACENDENTE 



#SALIDA DE DATOS
print("Nombres: ", nombres)
print("Edades: ", edad)
print("Arreglo o lista: ", arreglo_lista)
