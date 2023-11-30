# Pedir al usuario que ingrese diferentes tipos de datos
entero = int(input("Ingresa un número entero: "))
flotante = float(input("Ingresa un número flotante: "))
cadena = input("Ingresa una cadena de texto: ")
booleano_str = input("Ingresa un valor booleano (True/False): ")

# Convertir la cadena booleano_str a un valor booleano
booleano = booleano_str.lower() == 'true'

# Imprimir los datos en diferentes formatos
print("\nDatos ingresados:")
print("Entero:", entero)
print("Flotante:", flotante)
print("Cadena:", cadena)
print("Booleano:", booleano)

# Realizar conversiones de tipos y imprimir en diferentes formatos
print("\nConversiones de tipos:")
print("Entero a flotante:", float(entero))
print("Flotante a entero:", int(flotante))
print("Entero a cadena:", str(entero))
print("Booleano a cadena:", str(booleano))
