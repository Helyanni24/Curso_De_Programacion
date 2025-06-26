#bucles
#for
for x in range (0, 5):
    print("Hola el numero de X es: ", x)

for x in "Hola":
    print(x)

#while

import math
numero = int(input("Digite un numero: "))

while numero<0:
    print("Errror -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))