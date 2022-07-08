#EJERCICIO 7 AGUA DE UNA CISTERNA 

#ENTRADA
nivel_agua = float(input("Nivel del agua: "))

if (nivel_agua < 0):
    print ("FUGA DE CISTERNA")
elif(nivel_agua == 0):
    print("ENCENDER BOMBA DE AGUA")
elif(nivel_agua > 0 and nivel_agua < 2):
    print("ACELERAR BOMBA DE AGUA")
elif(nivel_agua >= 2 and nivel_agua < 4):
    print("BOMBA TRABAJANDO")
elif(nivel_agua >= 4 and nivel_agua < 6):
    print("DESACELERAR BOMBA")
elif(nivel_agua == 6 ):
    print("APAGAR BOMBA")
elif(nivel_agua > 6 ) :
    print("DESBORDAMIENTO DE AGUA EN CISTERNA" )