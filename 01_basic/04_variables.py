###
# 04-Variables
# variables son contenedores de informacion
# Python es un lenguaje de tipado dinamico y fuerte
###

a = 10
b = 20

print(a + b)
age = 30
my_name = "Javier"
print(my_name)
# las variables se pueden reasignar
my_name = "Pepe"
print(my_name)
# al igual que js tiene tipado dinámico
# el tipo de dato se define en tiempo de ejecucion
# no tiene que ser declarado explícitamente
my_name=10
print(my_name)

# es de tipado fuerte, no realiza conversiones automaticas
# print(10 + "10") # da error

# f-string (literales de cadena )
print(f"Hola {my_name}, tengo {age + 5} años")

# forma no recomendada de asignar variables
name, age, city = "Javier", 30, "Cusco"

# convecion de nombres de variables (snake_case) ✅
mi_nombre = "Javier"
# formas no recomendadas ❌
MiNombreDeVariable = "Pepe" # PascalCase
miNombreDeVariable= "Pepe" # camelCase


# python no tiene constantes, pero se pueden definir de manera similar a las variables
PI = 3.141516
MI_CONSTANTE=3.14 # UPPER_CASE, de esta forma se entiende que es una constante, pero de igual forma se puede reasignar
MI_CONSTANTE="False"

# errores al nombrar
# mi-nombre="Pepe"
# mi nombre="Pepe"

# palabras reservadas
# False, await, global, finally, lambda, nonlocal, not, try, etc.

# documentacion de variables
is_user_logged: bool = True
print(is_user_logged)
# pero aun asi se pueden reasignar
is_user_logged=20
print(is_user_logged)

# una forma de no permitir esto es cambiando la configuracion de nuestro editor en typecheck - cambiar a strict y ahora nos da error el ejemplo anterior (el error solo lo marca el editor, no el interprete)