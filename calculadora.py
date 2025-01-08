import os
os.system('clear')
import sys

#numero1 = input("Introduce el primer número: ")
#operacion = input("Introduce la operación aritmética deseada: ")
#numero2 = input("Introduce el segundo número: ")

numero1 = sys.argv[1]
operacion = sys.argv[2]
numero2 = sys.argv[3]

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
    elif operacion == "/":
        if int2 != 0:
            print(int1 / int2)
        else:
            print("No se puede realizar una división por cero")
    else:
        print("Operación no válida. Solo pueden ser '+', '-', '*' o '/'")
else:
    print("Alguno de los números no es válido")