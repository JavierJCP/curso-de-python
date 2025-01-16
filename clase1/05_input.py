###
# 05 - input
# entrada de datos
###

# print("¿Cómo te llamas?")
# nombre = input()

# print(f"Hola {nombre}! 👋🏻 ")

nombre = input("¿Cómo te llamas?\n")
print(f"Hola {nombre}!")

age = input("¿Cuántos años tienes?\n") # input siempre devuelve un str
print(f"Dentro de 20 años tendrás {int(age) + 20} años")


# obtener multiples valores
country, city = input("Ingresa tu pais y ciudad\n").split(" ") # separar por espacios en blanco
print(f"Tu país es {country} y tu ciudad es {city}")