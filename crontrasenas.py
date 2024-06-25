import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pasword = ""
rango = int(input("cuantos caracteres tendra la contrasena: "))

for i in range(rango):
    pasword += random.choice(caracteres)

print("-----------------------------")
print(pasword)    
print("-----------------------------")


