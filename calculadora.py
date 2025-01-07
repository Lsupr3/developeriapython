import os
os.system('clear')

numero1 = input("Introduce el primer número: ")
operacion = input("Introduce la operación aritmética deseada: ")
numero2 = input("Introduce el segundo número: ")


# Comprobar los datos de entrada y hacer las conversiones
if numero1.isdigit() and numero2.isdigit():
    int1 = int(numero1)
    int2 = int(numero2)

    # Comprobar si la operación es válida
    if operacion == "+":
        print(int1 + int2)
    elif operacion == "-":
        print(int1 - int2)
    elif operacion == "*":
        print(int1 * int2)
    else:
        print("Operación no válida. Solo pueden ser '+', '-' o '*'")
else:
    print("Alguno de los números no es válido")


