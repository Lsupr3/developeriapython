tareas=[]
seleccion = ""

while seleccion != "S":
    def agregar(tareas):
        tarea ={
            "Titulo": "",
            "Descripcion": "",
            "Prioridad": "Alta",
            "Estado": "Nueva"
            }
        tarea["Titulo"] = input("Introduce el título de la Tarea: ")
        tarea["Descripcion"] = input("Introduce la descripción de la tarea: ")
        tarea["Prioridad"] = input("Introduce la prioridad de la tarea (Alta/Media/Baja): ")
        tarea["Estado"] = "Nueva"
        #validación de los datos de la tarea

        tareas.append(tarea)
        return tareas

    def borrar(tareas):
         titulo = input("Introduce el título de la Tarea: ")
         for tarea in tareas:
              if tarea["Titulo"] == titulo:
                   tareas.remove(tarea)


    def imprime_tareas(tareas):
        if tareas:
            for tarea in tareas:
                    print(tarea)
        else:
             print("No hay ninguna tarea pendiente")

    seleccion=input("[A]gregar, [B]orrar, [L]istar, [S]alir: ")

    if seleccion == "A":
        resultado = agregar(tareas)
    if seleccion == "B":
         resultado = borrar(tareas)
    if seleccion == "L":
        imprime_tareas(tareas)