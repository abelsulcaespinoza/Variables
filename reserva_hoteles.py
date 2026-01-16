print("**** Sistema de Reserva de Hoteles ****")

# Definimos las variables
nombre_cliente = "Ana Pérez"
dias_estancia = 5
tarifa_diaria = 120.90
vista_al_mar = True

# Mostramos la información de la reserva
print(f"Cliente: {nombre_cliente}")
print(f"Días de estancia: {dias_estancia}")
print(f"Tarifa diaria: S/ {tarifa_diaria:.2f}")
if vista_al_mar:
    print("El cliente ha solicitado una habitación con vista al mar.")
else:
    print("El cliente no ha solicitado una habitación con vista al mar.")
# Calculamos el costo total
costo_total = dias_estancia * tarifa_diaria
print(f"Costo total: {costo_total:.2f}")
print("Gracias por reservar con nosotros.")

# Modificando Valores
print("\n**** Modificación de Reserva ****")
# Nuevos valores
dias_estancia = 7
tarifa_diaria = 150.75
vista_al_mar = False

# Mostramos la información actualizada de la reserva
print(f"Cliente: {nombre_cliente}")
print(f"Días de estancia: {dias_estancia}")
print(f"Tarifa diaria: S/ {tarifa_diaria:.2f}")
if vista_al_mar:
    print("El cliente ha solicitado una habitación con vista al mar.")
else:
    print("El cliente no ha solicitado una habitación con vista al mar.")
# Calculamos el costo total
costo_total = dias_estancia * tarifa_diaria
print(f"Costo total: {costo_total:.2f}")
print("Gracias por reservar con nosotros.")
