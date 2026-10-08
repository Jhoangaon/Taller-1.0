continuar = "si"
while continuar == "si":
    numero = int(input("Ingresa un número: "))

    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()