# Funciones y Parámetros en Python  

## 1. Introducción a las Funciones  

Las funciones son una parte fundamental de la programación en Python, ya que permiten encapsular código que realiza una tarea específica, facilitando su reutilización y organización. Una función puede recibir datos de entrada (parámetros), procesarlos, y devolver un resultado.  
   
### 1.1. Sintaxis Básica  
   
La sintaxis básica para definir una función en Python es:  
   
```python  
def nombre_de_la_funcion(parámetros):  
    """  
    Documentación de la función (opcional).  
    """  
    # Cuerpo de la función  
    # Código que realiza la tarea  
    return valor_de_retorno  
```  

- **`def`**: Palabra clave para definir una función.  
- **`nombre_de_la_funcion`**: Nombre descriptivo que sigue las reglas de nomenclatura de identificadores en Python.  
- **`parámetros`**: Variables que se pasan a la función (pueden ser opcionales).  
- **`return`**: Devuelve un valor desde la función.  

### 1.2. Ejemplo Simple  

```python  
def saludar():  
    # Esta función imprime un saludo.  
    print("¡Hola desde la función!")  
   
saludar()  # Llamada a la función  
```  

## 2. Parámetros y Argumentos  

Los parámetros son variables que se declaran en la definición de la función, mientras que los argumentos son los valores reales que se pasan a la función cuando se llama.  
   
### 2.1. Parámetros Posicionales  
   
Los argumentos se pasan en el mismo orden en que se definen los parámetros:  
   
```python  
def presentar(nombre, edad):  
    print(f"Nombre: {nombre}, Edad: {edad}")  
   
presentar("Juan", 30)  
```  

### 2.2. Parámetros con Valores Predeterminados  

Puedes asignar valores predeterminados a los parámetros, permitiendo que se llame a la función sin proporcionar todos los argumentos. Si no se pasa un argumento, se utiliza el valor predeterminado.  

```python  
def presentar(nombre, edad=18):  
    print(f"Nombre: {nombre}, Edad: {edad}")  
   
presentar("Ana")          # Usa el valor predeterminado para edad  
presentar("Carlos", 25)   # Sobrescribe el valor predeterminado  
```  

### 2.3 Parámetros con Nombre (Keyword Arguments)  

Cuando llamas a una función, puedes pasar los argumentos utilizando el nombre del parámetro al que deseas asignar el valor. Esto se conoce como pasar argumentos con nombre o keyword arguments.  

#### Ventajas de los Parámetros con Nombre  

1. **Claridad y Legibilidad**: Al usar el nombre de los parámetros, el código se vuelve más legible y claro, ya que queda explícito qué valor se está asignando a cada parámetro.  

2. **Orden Independiente**: Puedes pasar los argumentos en cualquier orden, siempre y cuando uses los nombres correctos de los parámetros.  

#### Ejemplo Básico  
   
Supongamos que tenemos una función que imprime detalles de una persona:  
   
```python  
def mostrar_detalles(nombre, edad, ciudad):  
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")  
```  
   
Cuando llamamos a esta función, podemos usar keyword arguments:  
   
```python  
# Usando argumentos posicionales (orden importa)  
mostrar_detalles("Luis", 30, "Madrid")  
   
# Usando argumentos con nombre (orden no importa)  
mostrar_detalles(edad=30, ciudad="Madrid", nombre="Luis")  
```  
   
En el ejemplo anterior, al usar argumentos con nombre, no importa el orden en que se pasan los argumentos a la función. Esto puede ser especialmente útil cuando una función tiene muchos parámetros, ya que mejora la legibilidad y reduce la posibilidad de errores al pasar valores en el orden incorrecto.  
   
### Combinación de Argumentos Posicionales y con Nombre  
   
En una llamada a función, puedes combinar argumentos posicionales y con nombre, siempre y cuando los argumentos posicionales se pasen primero:  
   
```python  
def describir_animal(tipo, nombre, edad):  
    print(f"Tipo: {tipo}, Nombre: {nombre}, Edad: {edad}")  
   
# Combinación de argumentos posicionales y con nombre  
describir_animal("Perro", nombre="Rex", edad=5)  
```  
   
En este ejemplo, `"Perro"` se pasa como un argumento posicional, mientras que `nombre` y `edad` se pasan como keyword arguments.  
   
### Restricciones  
   
- Los argumentos posicionales deben ir antes de los argumentos con nombre en una llamada a función.  
- No se pueden repetir argumentos usando ambos métodos en la misma llamada, es decir, no puedes pasar un valor por posición y luego darle un valor diferente usando su nombre.  
   
Utilizar parámetros con nombre es una práctica común para mejorar la claridad del código, especialmente cuando las funciones tienen muchos parámetros o cuando se utilizan valores predeterminados.

### 2.4. Argumentos Arbitrarios  

Cuando no sabes cuántos argumentos se pasarán a la función, puedes usar un asterisco (`*`) para recibir una tupla de argumentos:  
   
```python  
def listar_amigos(*amigos):  
    print("Mis amigos son:")  
    for amigo in amigos:  
        print(amigo)  
   
listar_amigos("Ana", "Juan", "Pedro", "Marta")  
```  

### 2.5. Argumentos Arbitrarios con Nombre  

Similarmente, usando dos asteriscos (`**`), puedes recibir un diccionario de argumentos con nombre:  

```python  
def mostrar_informacion(**kwargs):  
    for clave, valor in kwargs.items():  
        print(f"{clave}: {valor}")  
   
mostrar_informacion(nombre="Luis", edad=29, ciudad="Barcelona")  
```  

Por supuesto, `**kwargs` es una característica poderosa en Python que permite trabajar con un número variable de argumentos con nombre (keyword arguments) en las funciones. Aquí te explico cómo funciona y sus usos más comunes:  
   
### 2.6 ¿Qué es `**kwargs`?  
   
- **`**kwargs`** es una forma de capturar un número arbitrario de argumentos con nombre en un diccionario dentro de una función.  
- `kwargs` es un nombre convencional, pero puedes usar cualquier nombre que prefieras. Lo importante es el doble asterisco (`**`), que indica que se trata de argumentos con nombre.  
   
### Cómo Funciona `**kwargs`  
   
Cuando defines una función con `**kwargs`, puedes pasar cualquier número de argumentos con nombre al llamar a esa función. Estos argumentos se almacenan en un diccionario, donde las claves son los nombres de los argumentos y los valores son los datos pasados.  
   
#### Ejemplo Básico  
   
```python  
def imprimir_informacion(**kwargs):  
    for clave, valor in kwargs.items():  
        print(f"{clave}: {valor}")  
   
# Llamada a la función con diferentes argumentos  
imprimir_informacion(nombre="Ana", edad=28, ciudad="Madrid")  
imprimir_informacion(producto="Laptop", precio=1200, stock=15)  
```  
   
En este ejemplo, la función `imprimir_informacion` puede aceptar cualquier número de argumentos con nombre, y los imprime todos. La función puede ser llamada con diferentes conjuntos de argumentos.  
   
### Usos Comunes de `**kwargs`  
   
1. **Flexibilidad en las Funciones**: Permite a las funciones aceptar argumentos adicionales sin necesidad de definir explícitamente cada uno, lo que puede ser útil en situaciones donde no se conoce de antemano todos los posibles argumentos.  
   
2. **Extensibilidad de Funciones**: Al diseñar APIs o clases donde la flexibilidad es clave, `**kwargs` permite añadir nuevos argumentos sin romper las implementaciones existentes.  
   
3. **Pasar Argumentos a Otras Funciones**: `**kwargs` es útil para pasar conjuntos de argumentos a otras funciones o métodos que también acepten `**kwargs`.  
   
#### Ejemplo de Extensibilidad  
   
```python  
def procesar_datos(obligatorio1, obligatorio2, **kwargs):  
    print(f"Datos obligatorios: {obligatorio1}, {obligatorio2}")  
    for clave, valor in kwargs.items():  
        print(f"Datos adicionales: {clave} = {valor}")  
   
# Llamada a la función con datos obligatorios y adicionales  
procesar_datos(10, 20, opcion1="valor1", opcion2="valor2")  
```  
   
### Consideraciones  
   
- **Orden**: Si combinas `*args` y `**kwargs` en una función, `*args` debe venir antes de `**kwargs`.  
- **Nombres de Argumentos**: No puedes usar el mismo nombre de clave en `kwargs` que un argumento posicional o con nombre ya definido en la función.  
   
### Resumen  
   
`**kwargs` es una herramienta muy útil cuando necesitas diseñar funciones que sean altamente flexibles y capaces de manejar una cantidad indeterminada de argumentos con nombre. Esta capacidad es especialmente importante en el desarrollo de bibliotecas y APIs que necesitan evolucionar con el tiempo.

## 3. Retorno de Valores  
   
Las funciones pueden devolver valores usando la instrucción `return`. Esto es útil cuando necesitas que la función procese datos y devuelva el resultado.  
   
### 3.1. Retorno de un Valor  
   
```python  
def cuadrado(numero):  
    return numero ** 2  
   
resultado = cuadrado(4)  
print(f"El cuadrado de 4 es {resultado}")  
```  
   
### 3.2. Retorno de Múltiples Valores  
   
Puedes devolver múltiples valores separándolos por comas. Python los empaquetará en una tupla:  
   
```python  
def operaciones_basicas(a, b):  
    suma = a + b  
    resta = a - b  
    return suma, resta  
   
resultado_suma, resultado_resta = operaciones_basicas(7, 3)  
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")  
```  
   
## 4. Documentación de Funciones  
   
Es una buena práctica incluir una cadena de documentación (docstring) al inicio de la definición de la función para describir su propósito y cómo usarla.  
   
```python  
def area_rectangulo(base, altura):  
    """  
    Calcula el área de un rectángulo.  
  
    Parámetros:  
    base (float): La base del rectángulo.  
    altura (float): La altura del rectángulo.  
  
    Retorna:  
    float: El área del rectángulo.  
    """  
    return base * altura  
   
# Llamada a la función con documentación  
print(area_rectangulo(5, 3))  
```  
   
## 5. Ejercicios Prácticos Avanzados  
   
Aquí tienes cinco ejercicios prácticos centrados en el uso de funciones en Python, incluyendo el uso de `*args` y `**kwargs`.
   
### Ejercicio 1: Calculadora Simple  
   
**Descripción**: Crea una función llamada `calculadora` que acepte dos números y una operación (suma, resta, multiplicación, división) como argumentos. La función debe realizar la operación y devolver el resultado.  
   
```python  
def calculadora(num1, num2, operacion):  
    if operacion == 'suma':  
        return num1 + num2  
    elif operacion == 'resta':  
        return num1 - num2  
    elif operacion == 'multiplicacion':  
        return num1 * num2  
    elif operacion == 'division':  
        return num1 / num2  
    else:  
        return "Operación no válida"  
   
# Pruebas  
print(calculadora(10, 5, 'suma'))          # Salida: 15  
print(calculadora(10, 5, 'resta'))         # Salida: 5  
print(calculadora(10, 5, 'multiplicacion')) # Salida: 50  
print(calculadora(10, 5, 'division'))      # Salida: 2.0  
```  
   
### Ejercicio 2: Función de Bienvenida  
   
**Descripción**: Crea una función llamada `bienvenida` que acepte un nombre y un saludo opcional. Si no se proporciona el saludo, debe utilizar "Hola" por defecto.  
   
```python  
def bienvenida(nombre, saludo="Hola"):  
    return f"{saludo}, {nombre}!"  
   
# Pruebas  
print(bienvenida("Carlos"))            # Salida: Hola, Carlos!  
print(bienvenida("Ana", "Bienvenida")) # Salida: Bienvenida, Ana!  
```  
   
### Ejercicio 3: Sumar Números Arbitrarios  
   
**Descripción**: Crea una función llamada `sumar_numeros` que acepte un número variable de argumentos y devuelva la suma de todos ellos.  
   
```python  
def sumar_numeros(*args):  
    return sum(args)  
   
# Pruebas  
print(sumar_numeros(1, 2, 3))        # Salida: 6  
print(sumar_numeros(10, 20, 30, 40)) # Salida: 100  
```  
   
### Ejercicio 4: Información Personal  
   
**Descripción**: Crea una función llamada `mostrar_info` que acepte un nombre y cualquier cantidad de información adicional sobre una persona usando `**kwargs`. La función debe imprimir toda la información proporcionada.  
   
```python  
def mostrar_info(nombre, **kwargs):  
    print(f"Nombre: {nombre}")  
    for clave, valor in kwargs.items():  
        print(f"{clave}: {valor}")  
   
# Pruebas  
mostrar_info("Luis", edad=30, ciudad="Madrid", profesion="Ingeniero")  
# Salida:  
# Nombre: Luis  
# edad: 30  
# ciudad: Madrid  
# profesion: Ingeniero  
```  
   
### Ejercicio 5: Filtrar Palabras  
   
**Descripción**: Crea una función llamada `filtrar_palabras` que acepte una lista de palabras y una longitud mínima. La función debe devolver una lista de palabras que tengan al menos esa longitud.  

```python  
def filtrar_palabras(lista_palabras, longitud_minima):  
    return [palabra for palabra in lista_palabras if len(palabra) >= longitud_minima]  
  
# Pruebas  
palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]  
print(filtrar_palabras(palabras, 3)) # Salida: ['Python', 'lenguaje', 'programación']  
```
¡Excelente idea! Un reto final que combine varios aspectos básicos de Python y el uso de funciones puede ser una excelente manera de consolidar el aprendizaje. Aquí te propongo un ejercicio que abarca variables, estructuras de control, listas, diccionarios, funciones, `*args`, `**kwargs`, y manejo de excepciones.  
   
### Reto Final: Sistema de Gestión de Tareas  
   
**Descripción**: Crea un sistema simple de gestión de tareas que permita al usuario agregar, listar, y eliminar tareas. Cada tarea debe tener un título, una descripción opcional, una prioridad, y un estado (pendiente o completada).  
   
**Instrucciones**:  
   
1. Define una función `agregar_tarea(tareas, **kwargs)` que reciba una lista de tareas y cualquier número de argumentos con nombre para crear una nueva tarea. Cada tarea debe ser un diccionario con las claves `título`, `descripción`, `prioridad` y `estado`.  
   
2. Define una función `listar_tareas(tareas)` que imprima todas las tareas con su información.  
   
3. Define una función `eliminar_tarea(tareas, titulo)` que elimine una tarea por su título.  
   
4. Implementa un menú simple que permita al usuario elegir entre las opciones de agregar, listar, y eliminar tareas.  
   
5. Maneja posibles errores, como intentar eliminar una tarea que no existe.  
   
6. Al final, el programa debe poder gestionar múltiples tareas utilizando los conceptos aprendidos en el curso.  
   
**Código de Referencia**:  
   
```python  
def agregar_tarea(tareas, **kwargs):  
    tarea = {  
        "título": kwargs.get("título", "Sin título"),  
        "descripción": kwargs.get("descripción", "Sin descripción"),  
        "prioridad": kwargs.get("prioridad", "baja"),  
        "estado": kwargs.get("estado", "pendiente")  
    }  
    tareas.append(tarea)  
    print(f"Tarea '{tarea['título']}' agregada con éxito.")  
   
def listar_tareas(tareas):  
    if not tareas:  
        print("No hay tareas para mostrar.")  
        return  
    for i, tarea in enumerate(tareas, start=1):  
        print(f"Tarea {i}:")  
        for clave, valor in tarea.items():  
            print(f"  {clave.capitalize()}: {valor}")  
   
def eliminar_tarea(tareas, titulo):  
    for tarea in tareas:  
        if tarea["título"] == titulo:  
            tareas.remove(tarea)  
            print(f"Tarea '{titulo}' eliminada con éxito.")  
            return  
    print(f"No se encontró la tarea con el título '{titulo}'.")  
   
def menu():  
    tareas = []  
    while True:  
        print("\nSistema de Gestión de Tareas")  
        print("1. Agregar tarea")  
        print("2. Listar tareas")  
        print("3. Eliminar tarea")  
        print("4. Salir")  
  
        opcion = input("Elige una opción: ")  
        if opcion == "1":  
            titulo = input("Título de la tarea: ")  
            descripcion = input("Descripción (opcional): ")  
            prioridad = input("Prioridad (alta, media, baja): ")  
            estado = input("Estado (pendiente, completada): ")  
  
            agregar_tarea(  
                tareas,  
                título=titulo,  
                descripción=descripcion,  
                prioridad=prioridad,  
                estado=estado  
            )  
        elif opcion == "2":  
            listar_tareas(tareas)  
        elif opcion == "3":  
            titulo = input("Título de la tarea a eliminar: ")  
            eliminar_tarea(tareas, titulo)  
        elif opcion == "4":  
            print("Saliendo del sistema de gestión de tareas.")  
            break  
        else:  
            print("Opción no válida. Por favor, elige de nuevo.")  
   
# Ejecutar el menú principal  
menu()  
```  
   
Por supuesto, aquí tienes la continuación de la explicación del código del reto final.  
   
### Explicación del Código  
   
1. **Función `agregar_tarea`**:  
   - Utiliza `**kwargs` para aceptar argumentos con nombre, permitiendo al usuario especificar los detalles de la tarea.  
   - Crea un diccionario para representar la tarea, usando `kwargs.get()` para manejar valores predeterminados si ciertos detalles no se proporcionan.  
   - Añade la nueva tarea a la lista de tareas.  
   
2. **Función `listar_tareas`**:  
   - Recorre la lista de tareas y muestra cada una de ellas.  
   - Si no hay tareas, informa al usuario que no hay tareas para mostrar.  
   
3. **Función `eliminar_tarea`**:  
   - Busca una tarea en la lista por su título y la elimina si se encuentra.  
   - Si no se encuentra la tarea, informa al usuario.  
   
4. **Función `menu`**:  
   - Proporciona un menú interactivo para que el usuario elija entre las diferentes opciones: agregar, listar, y eliminar tareas, o salir.  
   - Utiliza un bucle `while` para mantener el menú activo hasta que el usuario elija salir.  
   - Maneja la entrada del usuario y llama a las funciones correspondientes según la opción seleccionada.  
   - Incluye manejo básico de errores al verificar la validez de la opción ingresada.  

### Elementos Clave del Reto  

- **Uso de Diccionarios**: Cada tarea se almacena como un diccionario, aprovechando la estructura de clave-valor para organizar la información de manera clara.  

- **Funciones y Modularidad**: El programa se divide en funciones específicas para cada acción, lo que facilita la comprensión y el mantenimiento del código.  

- **Interacción con el Usuario**: A través del menú, el usuario puede interactuar con el sistema de gestión de tareas, lo que hace que el programa sea dinámico.  

- **Manejo de Errores**: Se incluye un manejo básico de errores para asegurar que el programa sea más robusto frente a entradas inesperadas por parte del usuario.  
   
Este reto final es una excelente manera de consolidar el conocimiento adquirido a lo largo del curso, ya que combina varios conceptos y prácticas esenciales de programación en Python. Los estudiantes deben ser capaces de comprender cómo trabajar con estructuras de datos, manejar funciones con argumentos variables, y crear un flujo de programa interactivo.
