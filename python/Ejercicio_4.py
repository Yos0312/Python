# EJERCICIO 4 CONVERCIÓN DE GRADOS

#ENTRADA DE DATOS
grados = float(input("Grados: "))



#PROCESOS 
kelvin_celsius = grados - 273.15
kelvin_fahrenheit = ((9*(grados - 2723.15))/5) + 32
fahrenheit_celsius = (5*(grados - 32)) / 9
fahrenheit_kelvin = ((5*(grados - 32)) / 9 ) + 273.15
celsius_kelvin = grados + 273.15
celsius_fahrenheit = ((9 * grados) / 5) + 32  




#SALIDA DE DATOS 
print("Grados de K a C: " , round(kelvin_celsius,2))
print("Grados de K a F: " , round(kelvin_fahrenheit,2))
print("Grados de F a C: " ,round(fahrenheit_celsius,2))
print("Grados de F a K: " , round(fahrenheit_kelvin,2))
print("Grados de C a K: " , round(celsius_kelvin,2))
print("Grados de C a F: " , round(celsius_fahrenheit,2))