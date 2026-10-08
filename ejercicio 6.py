continuar = "si"
while continuar == "si":
    letra = input("Ingresa una letra: ").lower()

    if len(letra) != 1:
        print("No se puede procesar el dato.")
    elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("es vocal")
    else:
        print("no es vocal")
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()