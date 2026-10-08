continuar = "si"
while continuar == "si":
    dia = input("Ingresa un día de la semana: ").lower()

    if dia == "lunes":
        print("Inicio la semana")
    elif dia == "viernes":
        print("Por fin es viernes")
    elif dia == "sabado" or dia == "domingo":
        print("Fin de semana de jugar.")
    else:
        print("Dia comun y corriente")
        
    continuar = input("¿Deseas intentar de nuevo? (si/no): ").lower()