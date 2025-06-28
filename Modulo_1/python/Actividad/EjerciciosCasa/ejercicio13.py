print("Combinacion de operadores lógicos y relacionales")
numero = int(input("Introduce un número: "))

es_par = numero % 2 == 0
en_rango = 20 <= numero <= 50

if es_par and en_rango:
    print("El número es par y está entre 20 y 50.")
else:
    print("No cumple ambas condiciones.")