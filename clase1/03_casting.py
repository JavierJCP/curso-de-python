###
# 03 - casting de types
# transforma un type en otro
###

print("conversion de types")
print(type("10"))
# python no realiza conversiones automaticas
print(type(int("10")))

print("100" + str(2)) # concatenacion

print(float("3.141516"))
print(int(3.141516))

print(bool(-1))
print(bool(0)) # unico valor que devuelve False
print(bool("False"))
print(bool(""))