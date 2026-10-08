continuar = "si"
while continuar == "si":
    numero = int(input("Ingresa un número entre 10 y 50: "))
    if numero == 30:
        print("Ganaste un premio")
    else:
        print("Perdiste")
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()