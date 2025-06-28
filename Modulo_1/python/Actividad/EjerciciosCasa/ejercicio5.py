print("\nCalcular el descuento en una Compra")
while True:
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el porcentaje descuento del producto (solo el numero): "))
    prefinal = precio - (precio * descuento / 100)
    
    print(f"\nEl precio final con descuento es: {prefinal: .2f}")