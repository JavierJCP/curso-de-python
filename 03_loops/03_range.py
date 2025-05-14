###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nrange():")
# 👁️ range no crea una lista != [1,2,3]
# genera una secuencia de numeros en un rango 
# y para acceder a estos podemos usar un for
# va creando el numero segun se necesite, por lo tanto es muy optimo para rangos muuy grandes

# Generado una secuencia de números del 0 al 9
for num in range(10):
  print(num)

print("\nRange con inicio y fin: ")
# range(inicio, fin)
for num in range(5, 10):
  print(num)

print("\nRange con inicio, fin y paso: ")
# range(inicio, fin, paso)
for num in range(0, 50, 5):
  print(num)

print("\nRange con inicio negativo: ")
for num in range(-5, 0):
  print(num)

print("\nRange con decremento: ")
for num in range(10, 0, -1):
  print(num)


print("\nTransformar range a list: ") # no es muy recomendable
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

print("\nUsar range en for: ")
# seria para hacerlo cinco veces
for _ in range(5): # el _ es una convencion para indicar que "no" vamos a usar la variable
  print("hacer cinco veces algo")

