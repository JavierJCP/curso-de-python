###
# sentencias condicionales(if, elif, else)
###

import os # modulo de python para poder limpiar la pantalla
os.system('clear')

print('\n Sentencia simple condicional')
edad = 18
if edad >= 18:
  print('Eres mayor de edad') # el bloque de codigo afectado por la condicion debe estar con tabulacion

edad = 15
if edad <= 18:
  print('Eres menor de edad') 


print('\n Sentencia condicional con else')
edad = 15
if edad <= 18:
  print('Eres menor de edad') 
else:
  print('Eres mayor de edad')


print('\n Sentencia condicional con elif')
nota = 7
if nota >= 9:
  print('Excelente')
elif nota >= 7:
  print('Muy bien')
elif nota >= 5:
  print('Bien')
else:
  print('Insuficiente')


  ### operadores logicos
print("\n Operador condicional and")
edad= 50
tiene_carnet= False
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("Llamar a la policia 🚓")

print("\n Operador condicional or")
edad= 50
tiene_carnet= False 
if edad >= 18 or tiene_carnet:
  print("Puedes conducir 🚗 en Peru ")
else:
  print("Llamar a la policia 🚓")

print("\n Operador condicional not")
es_fin_de_semana = False
if not es_fin_de_semana:
  print("No es fin de semana")
else:
  print("Es fin de semana")

print("\n anidar condicionales")
edad=18
tiene_dinero= False
if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la disco 🎉")
  else:
    print("Quedate en casa 🏠")
else:
  print("No puedes ir a la disco 🥲")

