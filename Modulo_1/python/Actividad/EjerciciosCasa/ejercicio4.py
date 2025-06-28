print("Año Bisiesto")
while True:
    
    año = int(input("Introduce un año: "))
    if (año %4 == 0 and año %100 !=0 ) or (año % 400 == 0):
        print(f"El año es bisiesto")
    else:
        print(f"No es un año bisiesto")