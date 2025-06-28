#conjuntos

miconjunto = {2, 4, 8, 10, 12}
print("Conjunto original:", miconjunto)


miconjunto.add(6)
print("Conjunto después de añadir el número 6:", miconjunto)

for elemento in miconjunto:
    print("Elemento del conjunto:", elemento)

otroconjunto = {1, 3, 5, 7}
print("¿mi_conjunto es igual a otro_conjunto?", miconjunto == otroconjunto)