continuar = "si"
while continuar == "si":
    candidato = input("Elige un candidato (A, B o C): ").upper()

    if candidato == "A":
        print("Usted ha votado por el partido rojo")
    elif candidato == "B":
        print("Usted ha votado por el partido verde")
    elif candidato == "C":
        print("Usted ha votado por el partido azul")
    else:
        print("Opción errónea")
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()