#EJERCICIO 9 NÓMINA

#ENTRADA DE DATOS
MES = "enero"
días_laborales = int(input("Días laborales: "))




#PROCESOS

pago_base = 250 * días_laborales
iva_traslado = pago_base * 0.16
subtotal = pago_base + iva_traslado
iva_retenido = (2/3) * iva_traslado
isr_retenido = pago_base * 0.10
Pago_neto = subtotal - iva_retenido - isr_retenido


#SALIDA DE DATOS

print("Mes laboral: ", MES)
print("Pago base: ", round(pago_base,2))
print("Pago neto: ", round(Pago_neto,2))