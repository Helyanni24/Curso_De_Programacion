#diccionario
dicc = {
    "Ariangelina Rincon": 15,
    "Brian Mendez": 10,
    "Carlos Villero": 18,
    "Damian Garcia": 13,
    "Deciel Fernandez": 13,
    "Elias Rivas": 18,
    "Fabian Cardenas": 17,
    "Franklin Vecino": 17,
    "Helyanni Rodriguez": 16,
    "Liliana Rincon": 14,
    "Maria Macias": 16,
    "Over Machado": 16,
    "Paul Moran": 14,
    "Ronald Trujilllo": 12,
    "Yuliexy Dimas": 10
}
print("\nLista Original de los Estudiantes y sus Notas.")
for nombre, nota in dicc.items():
 print(f"\nNombre: {nombre}, Nota: {nota}")  

dicc["Ariangelina Rincon"]= 21
dicc["Over Machado"]= 20
dicc["Brian Mendez"]= 20
dicc["Carlos Villero"]= 21
dicc["Damian Garcia"]=21
dicc["Deciel Fernandez"]= 17
dicc["Elias Rivas"]= 20
dicc["Fabian Cardenas"]= 20
dicc["Franklin Vecino"]= 20
dicc["Helyanni Rodriguez"]= 21
dicc["Liliana Rincon"]= 20
dicc["Maria Macias"]= 24
dicc["Over Machado"]= 20
dicc["Paul Moran"]= 20
dicc["Ronald Trujilllo"]= 20
dicc["Yuliexy Dimas"]= 21

print("\nLista Modificada de los Estudiantes y sus Edades.")
for nombre, edad in dicc.items():
 print(f"\nNombre: {nombre}, Edad: {edad}")  