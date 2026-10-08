continuar = "si"
while continuar == "si":
    fecha = input("Ingrese la fecha (ejemplo: Lunes, 15/05): ")
    
    partes = fecha.split(",") 
    dia_semana = partes[0].strip().lower() 
    
    numeros = partes[1].strip().split("/") 
    dia = int(numeros[0])
    mes = int(numeros[1])

    if dia > 31 or mes > 12 or (dia_semana != "lunes" and dia_semana != "martes" and dia_semana != "miercoles" and dia_semana != "jueves" and dia_semana != "viernes" and dia_semana != "sabado" and dia_semana != "domingo"):
        print("Se produjo un error.")
        break 
    else:
        if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles":
            hubo_examen = input("¿Hubo exámenes? (si/no): ").lower()
            if hubo_examen == "si":
                aprobados = int(input("Alumnos aprobados: "))
                reprobados = int(input("Alumnos no aprobados: "))
                total = aprobados + reprobados
                porcentaje = (aprobados / total) * 100
                print("Porcentaje de aprobados:", porcentaje, "%")
                
        elif dia_semana == "jueves":
            asistencia = float(input("Porcentaje de asistencia (%): "))
            if asistencia > 50:
                print("asistió la mayoría")
            else:
                print("no asistió la mayoría")
                
        elif dia_semana == "viernes":
            if dia == 1 and (mes == 1 or mes == 7):
                print("Comienzo de nuevo ciclo")
                alumnos = int(input("Cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Arancel en $ por cada alumno: "))
                ingreso_total = alumnos * arancel
                print("El ingreso total en $ es:", ingreso_total)
                
    continuar = input("¿Deseas procesar otra fecha? (si/no): ").lower()