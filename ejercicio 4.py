continuar = "si"
while continuar == "si":
    numero = int(input("Ingresa un número entero: "))

    if numero < 0:
        valor_absoluto = numero * -1
    else:
        valor_absoluto = numero

    print("El valor absoluto es:", valor_absoluto)
    
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()