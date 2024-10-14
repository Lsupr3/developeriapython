import os
os.system("cls")

def genera_reporte(main_tank, external_tank, hidrogen_tank):
    return f"""Fuel Report:
        Main Tank:     {main_tank}
        External Tank: {external_tank}
        Hydrogen Tank: {hidrogen_tank} """

print(genera_reporte(30, 40, 50))