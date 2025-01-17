import csv
import os

try: 
    seguir = True
    while seguir:
        #Limpio la consola
        os.system('clear')

        #Cargo la agenda y la imprimo
        with open("agenda.csv", "r") as csvFile:
            reader = csv.reader(csvFile)
            for contacto in reader:
                print(contacto)
        print("")
        operacion = input("[A]gregar, [B]orrar, [C]ambiar, [S]alir: ")

        if operacion in ["A", "B", "C", "S"]:
            if operacion == "A":
                nuevoNombre = input ("Introduzca el nombre del nuevo contácto: ")
                nuevoApellido = input ("Introduzca el apellido del nuevo contácto: ")
                nuevoedad = int(input ("Introduzca edad del nuevo contácto: "))
                nuevaCiudad = input ("Introduzca la ciudad del nuevo contácto: ")

                with open("agenda.csv", "a") as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow([nuevoNombre,nuevoApellido,nuevoedad,nuevaCiudad])

            elif operacion == "B":
                existeContacto = False
                contacto = input("Introduzca el nombre del contácto que quiere borrar: ")
                #Leo y guardo todas las filas que no tengan como primera columna el nombre del qcontácto que quiero borrar
                with open("agenda.csv", "r") as csvFile:
                    reader = csv.reader(csvFile)
                    contactos = []
                    for fila in reader:
                        if not fila[0] == contacto:
                            contactos.append(fila)
                        else:
                            existeContacto = True
                
                if existeContacto:
                    #Escribo las filas restantes
                    with open("agenda.csv", "w") as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(contactos)
                else:
                    print("No se ha encontrado a ningún contácto con ese nombre")

            elif operacion == "C":
                existeContacto = False
                contacto = input("Introduzca el nombre del contácto al que quiere cambiarle los datos: ")
                with open("agenda.csv", "r") as csvFile:
                    reader = csv.reader(csvFile)
                    contactos = []
                    for fila in reader:
                        if not fila[0] == contacto:
                            contactos.append(fila)
                        else:
                            existeContacto = True

                if existeContacto:
                    nuevoApellido = input ("Introduzca el nuevo apellido del contácto: ")
                    nuevoedad = int(input ("Introduzca la nueva edad del  contácto: "))
                    nuevaCiudad = input ("Introduzca la nueva ciudad del contácto: ")
                    with open("agenda.csv", "w") as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(contactos)
                        
                    with open("agenda.csv", "a") as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([contacto,nuevoApellido,nuevoedad,nuevaCiudad])
                else:
                    print("No hay ningún contácto con ese nombre")
            elif operacion == "S":
                seguir = False
        else:
            print("Operación no permitida")
        
        input("Pulse cualquier tecla para continuar")
except Exception as e:
    print(f"Ha saltado la siguiente excepción: {e}" )