def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Renunciar")

def main():
    cesta_de_la_compra = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            elemento = input("Ingrese el nombre del elemento a agregar: ")
            cesta_de_la_compra.append(elemento)
            print(f"Elemento '{elemento}' agregado a la cesta.")
        
        elif opcion == '2':
            if cesta_de_la_compra:
                print("Contenido de la cesta de la compra:")
                for item in cesta_de_la_compra:
                    print(f"- {item}")
            else:
                print("La cesta de la compra está vacía.")
        
        elif opcion == '3':
            elemento = input("Ingrese el nombre del elemento a eliminar: ")
            if elemento in cesta_de_la_compra:
                cesta_de_la_compra.remove(elemento)
                print(f"Elemento '{elemento}' eliminado de la cesta.")
            else:
                print(f"El elemento '{elemento}' no se encuentra en la cesta.")
        
        elif opcion == '4':
            precios = {
                "manzana": 0.5,
                "banana": 0.3,
                "naranja": 0.4,
                "leche": 1.0,
                "pan": 1.5
            }
            total = sum(precios.get(item, 0) for item in cesta_de_la_compra)
            print(f"El total de la cesta de la compra es: ${total:.2f}")
        
        elif opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
