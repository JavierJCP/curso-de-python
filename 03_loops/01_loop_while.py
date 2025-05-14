###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0

while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True: # este bucle seria infito
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle infinito, este metodo es muy usado en casos en los que no sabemos cuantas veces debe ejecutarse el bucle por ejemplo:
contador = 0
while contador <= 1000:
  contador += 1
  if contador % 5 == 0:
    print(contador)
    break

# continue, lo que hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else: # solo se ejecuta cuando ha terminado todos los bucles de la condicion while y no se ha ejecutado el break
  print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: "))
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try: # try-except lo mismo que try-catch de js
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except: # ejecutar este codigo cuando haya un error, en este caso no es un numero
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")

