###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\n Ejercicio 1:")
num1= int(input("Introduce el primer numero: "))
num2= int(input("Introduce el segundo numero: "))
if num1 > num2:
  print(f"El primer numero {num1} es mayor que el segundo {num2}")
elif num2 > num1:
  print(f"El segundo numero {num2} es mayor que el primero {num1}")
else:
  print(f"Los numeros {num1} y {num2} son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\n Ejercicio 2:")
num1= int(input("Introduce el primer numero: "))
num2= int(input("Introduce el segundo numero: "))
operacion= input("Introduce la operacion: ")
if operacion == "+":
  print(num1 + num2)
elif operacion == "-":
  print(num1 - num2)
elif operacion == "*":
  print(num1 * num2)
elif operacion == "/":
  if num2 == 0:
    print("No se puede dividir entre 0")
  else:
    print(num1 / num2)
else:
  print("Operacion no valida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\n Ejercicio 3:")
año=int(input("Introduce un año: "))
if ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0):
  print(f"El año {año} es bisiesto")
else:
  print(f"El año {año} no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\n Ejercicio 3:")
edad=int(input("Introduce una edad:"))
if edad <= 2:
  print("Bebe")
elif 3 <= edad <= 12:
  print("Niño")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= 65:
  print("Adulto mayor")
else:
  print("Edad no valida")