print("**** Sistema de Tienda Online ****")
nombre_producto = "Cámara digital"
precio_producto = 399.99
cantidad_inventario = 20
es_disponible = True

# Mostrar información del producto
print(f"Producto: {nombre_producto}")
print(f"Precio: S/ {precio_producto:.2f}")
print(f"Cantidad en inventario: {cantidad_inventario}")
if cantidad_inventario > 0:
    print("El producto está disponible para la venta.")
else:
    print("El producto no está disponible para la venta.")
    es_disponible = False
print("Gracias por visitar nuestra tienda online.")

# Modificando variables
nombre_producto = "Cámara digital avanzada"
precio_producto = 299.99
cantidad_inventario -= 20  # Se vendieron 5 unidades
print("\n**** Actualización del Producto ****")
print(f"Producto: {nombre_producto}")
print(f"Nuevo Precio: S/ {precio_producto:.2f}")
print(f"Nueva Cantidad en inventario: {cantidad_inventario}")
if cantidad_inventario > 0:
    print("El producto está disponible para la venta.")
else:
    print("El producto no está disponible para la venta.")
    es_disponible = False
print("Gracias por visitar nuestra tienda online.")
