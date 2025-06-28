print("Tres números en orden descendente")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > b and b > c:
    print("El primer número es mayor que el segundo y el segundo es mayor que el tercero.")
else:
    print("No se cumple la condición.")