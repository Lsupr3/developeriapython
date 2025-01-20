tareas=[]
seleccion = ""

def agregar(tareas, tarea={
        "Titulo": "",
        "Descripcion": "",
        "Prioridad": "Alta",
        "Estado": "Nueva"
        }, IsTest=False):
    if not IsTest:
        tarea["Titulo"] = input("Introduce el título de la Tarea: ")
        tarea["Descripcion"] = input("Introduce la descripción de la tarea: ")
        tarea["Prioridad"] = input("Introduce la prioridad de la tarea (Alta/Media/Baja): ")
        tarea["Estado"] = "Nueva"
    #validación de los datos de la tarea

    tareas.append(tarea)
    return tareas

def borrar(tareas, titulo="", IsTest=False):
    if not IsTest:
        titulo = input("Introduce el título de la Tarea: ")
    for tarea in tareas:
        if tarea["Titulo"] == titulo:
            tareas.remove(tarea)
    return tareas

def imprime_tareas(tareas):
    resultado = ""
    if tareas:
        for tarea in tareas:
            resultado = tarea
            print(tarea)
    else:
        resultado = "No hay ninguna tarea pendiente"
        print(resultado)
        
    return resultado            

"""
while seleccion != "S":
    seleccion=input("[A]gregar, [B]orrar, [L]istar, [S]alir: ")

    if seleccion == "A":
        resultado = agregar(tareas)
    if seleccion == "B":
         resultado = borrar(tareas)
    if seleccion == "L":
        imprime_tareas(tareas)
"""