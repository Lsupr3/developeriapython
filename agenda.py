agenda = {"Alice": "539-645-789", "Pedro":"654-356-236", "Ana":"675-898-876"}
print(agenda)
operacion = input("[A]gregar, [B]orrar, [C]ambiar, [L]istar: ")

if operacion in ["A", "B", "C", "L"]:
    print("La operación escogida es:  " + operacion)
    if operacion == "A":
        nuevoContacto = input ("Introduzca el nombre del nuevo contácto: ")
        if nuevoContacto in agenda:
            print("Ya existe un contácto con ese nombre")
        else:
            telefono = input("Introduzca el teléfono para " + nuevoContacto + ": ")
            agenda[nuevoContacto] = telefono
            print(agenda)
    elif operacion == "B":
        contacto = input("Introduzca el nombre del contácto que quiere borrar: ")
        if contacto in agenda:
            del agenda[contacto]
            print(agenda)
        else:
            print("No existe ninguna persona con ese nombre en la agenda.")
    elif operacion == "C":
        contacto = input("Introduzca el nombre del contácto del que quiere cambiarle el teléfono: ")
        if contacto in agenda:
            telefono = input("Introduzca el nuevo teléfono: ")
            # Hacer validación del teléfono
            agenda[contacto] = telefono
            print(agenda)
        else:
            print("No existe ninguna persona con ese nombre en la agenda.")
    elif operacion == "L":
        print(agenda)
else:
    print("Operación no permitida")