# Programa: Registro de explorador espacial

# Asignar valores a las variables
nombre_explorador = "Abel Sulca Espinoza"
planeta_origen = "Tierra"
edad_explorador = 26
misiones_completadas = 4
nivel_energia = 87.5

# for = 15  # Esto generará un error de sintaxis porque 'for' es una palabra reservada en Python
Nivel_Energia = 90.5  # Esto es válido, pero no sigue la convención de nombres en minúsculas con guiones bajos
NIVEL_ENERGIA = 100.0  # Esto es válido y se usa comúnmente para constantes
nivel_energía = 75.0  # Esto generará un error debido al carácter especial 'í'

# Imprimir la información del explorador espacial
print("Información del Explorador Espacial:")
print("Nombre:", nombre_explorador)
print("Planeta de Origen:", planeta_origen)
print("Edad:", edad_explorador, "años")
print("Misiones Completadas:", misiones_completadas)
print("Nivel de Energía:", nivel_energia, "%")
