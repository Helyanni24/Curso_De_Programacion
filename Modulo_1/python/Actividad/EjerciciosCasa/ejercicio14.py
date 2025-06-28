print("Calificación por nota")
nota = int(input("Introduce la calificación numérica (1-100): "))

if 90 <= nota <= 100:
    print("Calificación: A")
elif 80 <= nota < 90:
    print("Calificación: B")
elif 70 <= nota < 80:
    print("Calificación: C")
elif 60 <= nota < 70:
    print("Calificación: D")
elif 0 <= nota < 60:
    print("Calificación: F")
else:
    print("Valor fuera de rango.")