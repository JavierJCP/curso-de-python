###
# 02 - boolean
# valores logicos: True y False
###

import os
os.system("clear")

print('\nValores booleanos basicos:')
print(True)
print(False)

# Operadors de comparacion: devuelven un booleano
print("\nOperadores de comparacion:")
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3) # type: ignore
print("5 >= 3:", 5 >= 3)
print("5 <= 3:", 5 <= 3)

print('\nComparacion de strings:')
print("hola" == "hola")
print("hola" == "HOLA") # type: ignore # sensible a las mayusculas
print("manzana < pera:", "manzana" < "pera") # m es mas pequeña que p, esta antes en el alfabeto

# Operadores logicos and, or, not
print("\nOperadores Logicos:")
print("True and True:", True and True)
print("False and True:", False and True)
print("True or False:", True or False)
print("False or True:", True or True)
print("not True:", not True)
print("not False:", not False)