import os
os.system("cls")

def genera_reporte(**fueltank):
    for name, value in fueltank.items():
        print (f"{name}: {value}")

genera_reporte(main=50, external=80, hidrogen=40)

def funcion(*parametro):
    print()

funcion()