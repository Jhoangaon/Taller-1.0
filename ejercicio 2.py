continuar = "si"
while continuar == "si":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if num1 < num2:
        print("El primer número es menor.")
    elif num2 < num1:
        print("El segundo número es menor.")
    else:
        print("Ambos números son iguales.")
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()