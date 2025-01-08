# Introducción a las Listas, Tuplas, Sets y Diccionarios en Python  
   
## Introducción  
   
En Python, las colecciones son tipos de datos que permiten almacenar múltiples valores en una sola variable. Las colecciones en Python incluyen listas, tuplas, sets y diccionarios. Cada una de estas colecciones tiene características y usos específicos. En este documento, aprenderás sobre cada una de estas colecciones y cómo utilizarlas en tus programas.  
   
## Listas  
   
Las listas son colecciones ordenadas y mutables, lo que significa que puedes cambiar su contenido después de haberlas creado. Se definen utilizando corchetes `[]` y pueden contener elementos de diferentes tipos.  
   
### Creación de Listas  
   
```python  
mi_lista = [1, 2, 3, 4, 5]  
otra_lista = ["manzana", "banana", "cereza"]  
lista_mixta = [1, "hola", 3.14, True]  
```  
   
### Acceso a Elementos  
   
```python  
print(mi_lista[0])  # Imprime 1  
print(otra_lista[1])  # Imprime "banana"  
```  
   
### Modificación de Elementos  
   
```python  
mi_lista[2] = 10  
print(mi_lista)  # Imprime [1, 2, 10, 4, 5]  
```  
   
### Métodos Comunes  
   
```python  
mi_lista.append(6)  # Añade 6 al final de la lista  
mi_lista.remove(2)  # Elimina el primer 2 que encuentra en la lista  
longitud = len(mi_lista)  # Devuelve la longitud de la lista  
```  
   
### Ejemplo Completo  
   
```python  
frutas = ["manzana", "banana", "cereza"]  
frutas.append("naranja")  
frutas.remove("banana")  
print(frutas)  # Imprime ["manzana", "cereza", "naranja"]  
```  
   
## Tuplas  
   
Las tuplas son colecciones ordenadas e inmutables, lo que significa que no puedes cambiar su contenido después de haberlas creado. Se definen utilizando paréntesis `()`.  
   
### Creación de Tuplas  
   
```python  
mi_tupla = (1, 2, 3, 4, 5)  
otra_tupla = ("manzana", "banana", "cereza")  
tupla_mixta = (1, "hola", 3.14, True)  
```  
   
### Acceso a Elementos  
   
```python  
print(mi_tupla[0])  # Imprime 1  
print(otra_tupla[1])  # Imprime "banana"  
```  
   
### Métodos Comunes  
   
```python  
longitud = len(mi_tupla)  # Devuelve la longitud de la tupla  
```  
   
### Ejemplo Completo  
   
```python  
frutas = ("manzana", "banana", "cereza")  
print(frutas)  # Imprime ("manzana", "banana", "cereza")  
```  
   
## Sets (Conjuntos)  
   
Los sets son colecciones desordenadas de elementos únicos. Se definen utilizando llaves `{}` o la función `set()`.  
   
### Creación de Sets  
   
```python  
mi_set = {1, 2, 3, 4, 5}  
otro_set = {"manzana", "banana", "cereza"}  
set_vacio = set()  
```  
   
### Añadir y Eliminar Elementos  
   
```python  
mi_set.add(6)  # Añade 6 al set  
mi_set.remove(3)  # Elimina el 3 del set  
```  
   
### Métodos Comunes  
   
```python  
union = mi_set.union({6, 7, 8})  # Unión de sets  
interseccion = mi_set.inter

```python  
interseccion = mi_set.intersection({4, 5, 6})  # Intersección de sets  
diferencia = mi_set.difference({4, 5})  # Diferencia de sets  
```  
   
### Ejemplo Completo  
   
```python  
frutas = {"manzana", "banana", "cereza"}  
frutas.add("naranja")  
frutas.remove("banana")  
print(frutas)  # Imprime {"manzana", "cereza", "naranja"}  
```  
   
## Diccionarios  
   
Los diccionarios son colecciones desordenadas de pares clave-valor. Se definen utilizando llaves `{}` con pares clave-valor separados por dos puntos `:`.  
   
### Creación de Diccionarios  
   
```python  
mi_diccionario = {"nombre": "Alice", "edad": 25, "ciudad": "Nueva York"}  
otro_diccionario = {1: "uno", 2: "dos", 3: "tres"}  
diccionario_vacio = {}  
```  
   
### Acceso a Elementos  
   
```python  
print(mi_diccionario["nombre"])  # Imprime "Alice"  
print(otro_diccionario[2])  # Imprime "dos"  
```  
   
### Modificación de Elementos  
   
```python  
mi_diccionario["edad"] = 26  
print(mi_diccionario)  # Imprime {"nombre": "Alice", "edad": 26, "ciudad": "Nueva York"}  
```  
   
### Añadir y Eliminar Elementos  
   
```python  
mi_diccionario["ocupacion"] = "Ingeniera"  # Añade un nuevo par clave-valor  
del mi_diccionario["ciudad"]  # Elimina el par clave-valor con clave "ciudad"  
```  
   
### Métodos Comunes  
   
```python  
claves = mi_diccionario.keys()  # Devuelve una lista de las claves  
valores = mi_diccionario.values()  # Devuelve una lista de los valores  
items = mi_diccionario.items()  # Devuelve una lista de los pares clave-valor  
```  
   
### Ejemplo Completo  
   
```python  
persona = {"nombre": "Bob", "edad": 30, "ciudad": "San Francisco"}  
persona["ocupacion"] = "Doctor"  
del persona["ciudad"]  
print(persona)  # Imprime {"nombre": "Bob", "edad": 30, "ocupacion": "Doctor"}  
```  
   
## Comparación de Colecciones  
   
| Característica    | Listas                    | Tuplas                    | Sets                      | Diccionarios              |  
|-------------------|---------------------------|---------------------------|---------------------------|---------------------------|  
| Orden             | Ordenadas                 | Ordenadas                 | Desordenadas              | Desordenadas              |  
| Mutabilidad       | Mutables                  | Inmutables                | Mutables                  | Mutables                  |  
| Elementos Duplicados | Permitidos               | Permitidos               | No permitidos             | Claves únicas             |  
| Sintaxis de Creación | `[1, 2, 3]`              | `(1, 2, 3)`              | `{1, 2, 3}`               | `{"clave": "valor"}`      |  
| Acceso a Elementos   | Por índice               | Por índice               | No aplica (uso de `in`)   | Por clave                 |  
   
## Conclusión  
   
Las colecciones en Python (listas, tuplas, sets y diccionarios) son herramientas poderosas que te permiten almacenar y manipular grupos de datos de manera eficiente. Cada tipo de colección tiene sus propias características y usos, por lo que es importante comprender cuándo usar cada una.  
   
### Resumen de Conceptos:  
   
1. **Listas**:  
    - Colección ordenada y mutable.  
    - Permite elementos duplicados.  
- Uso común: Almacenar secuencias de datos que pueden cambiar a lo largo del tiempo.  
   
2. **Tuplas**:  
    - Colección ordenada e inmutable.  
    - Permite elementos duplicados.  
    - Uso común: Almacenar datos que no deben cambiar, como coordenadas o registros constantes.  
   
3. **Sets (Conjuntos)**:  
    - Colección desordenada de elementos únicos.  
    - No permite elementos duplicados.  
    - Uso común: Almacenar datos únicos y realizar operaciones de conjuntos, como unión, intersección y diferencia.  
   
4. **Diccionarios**:  
    - Colección desordenada de pares clave-valor.  
    - Claves únicas, valores pueden ser duplicados.  
    - Uso común: Almacenar datos que se acceden por claves únicas, como registros de datos, configuraciones o mapeos.  
   
## Ejercicios Prácticos  
   
Para solidificar tu comprensión, aquí tienes algunos ejercicios prácticos que puedes intentar:  
   
1. **Lista de Estudiantes**:  
    Crea una lista con los nombres de cinco estudiantes. Añade un nuevo estudiante al final de la lista, luego elimina el tercer estudiante. Imprime la lista resultante.  
  
    ```python  
    estudiantes = ["Alice", "Bob", "Charlie", "David", "Eve"]  
    estudiantes.append("Frank")  
    estudiantes.pop(2)  
    print(estudiantes)  
    ```  
   
2. **Tupla de Fechas**:  
    Crea una tupla que contenga tres fechas importantes (como cumpleaños o aniversarios). Intenta modificar una de las fechas y observa el error que se genera.  
  
    ```python  
    fechas = ("2023-01-01", "2023-05-15", "2023-08-20")  
    # fechas[1] = "2023-06-15"  # Esto generará un error porque las tuplas son inmutables  
    print(fechas)  
    ```  
   
3. **Set de Colores**:  
    Crea un set con los nombres de cuatro colores. Añade un nuevo color y luego elimina uno de los colores existentes. Imprime el set resultante.  
  
    ```python  
    colores = {"rojo", "azul", "verde", "amarillo"}  
    colores.add("naranja")  
    colores.remove("azul")  
    print(colores)  
    ```  
   
4. **Diccionario de Precios**:  
    Crea un diccionario que contenga tres productos como claves y sus respectivos precios como valores. Actualiza el precio de uno de los productos y añade un nuevo producto con su precio. Imprime el diccionario resultante.  
  
    ```python  
    precios = {"manzana": 0.50, "banana": 0.30, "cereza": 0.20}  
    precios["banana"] = 0.35  
    precios["naranja"] = 0.40  
    print(precios)  
    ```  
   
## Recursos Adicionales  
   
Para seguir aprendiendo sobre las colecciones en Python, aquí tienes algunos recursos adicionales:  
   
- [Documentación Oficial de Python sobre Listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)  
- [Documentación Oficial de Python sobre Tuplas](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)  
- [Documentación Oficial de Python sobre Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)  
- [Documentación Oficial de Python sobre Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  
- [Real Python - Listas y Tuplas en Python](https://realpython.com/python-lists-tuples/)  
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)  
   
## Palabras Finales  
   
Las colecciones en Python son esenciales para el manejo de datos en tus programas. Comprender las diferencias entre listas, tuplas, sets y diccionarios te permitirá elegir la mejor herramienta para cada tarea y escribir código más eficiente y claro.  
   
### Resumen de Conceptos:  
   
1. **Listas**:  
    - Ordenadas y mutables.  
    - Útiles para datos que cambian frecuentemente.  
    - Permiten elementos duplicados.  
   
2. **Tuplas**:  
    - Ordenadas e inmutables.  
    - Útiles para datos que no deben cambiar.  
    - Permiten elementos duplicados.  
   
3. **Sets (Conjuntos)**:  
    - Desordenados y mutables.  
    - Útiles para datos únicos y operaciones de conjuntos.  
    - No permiten elementos duplicados.  
   
4. **Diccionarios**:  
    - Desordenados y mutables.  
    - Útiles para pares clave-valor, como registros de datos.  
    - Claves únicas, valores pueden ser duplicados.  

### Práctica y Exploración:  
   
La mejor manera de aprender a usar las colecciones en Python es a través de la práctica y la exploración. Intenta resolver problemas prácticos y experimenta con los ejemplos proporcionados. No dudes en consultar la documentación oficial y otros recursos en línea para obtener más información y ejemplos.  
   
### Conclusión:  
   
Ahora que tienes una comprensión básica de las listas, tuplas, sets y diccionarios en Python, estás listo para comenzar a utilizarlos en tus proyectos. Estas colecciones son fundamentales para la manipulación de datos y te permitirán escribir programas más eficientes y organizados.  
   
Recuerda que cada tipo de colección tiene sus propias características y ventajas, así que elige la que mejor se adapte a tus necesidades específicas. ¡Buena suerte y sigue practicando!

¡Por supuesto! Te proporcionaré un documento en formato Markdown que cubre el uso de la palabra clave `in` y funciones similares en Python.  
   
### Operadores y Funciones de Pertenencia en Python  
   
#### Tabla de Contenidos  
   
1. [Introducción](#introducción)  
2. [Operador `in`](#operador-in)  
    - [Uso con listas](#uso-con-listas)  
    - [Uso con cadenas](#uso-con-cadenas)  
    - [Uso con diccionarios](#uso-con-diccionarios)  
3. [Función `any`](#función-any)  
4. [Función `all`](#función-all)  
5. [Ejemplos Prácticos](#ejemplos-prácticos)  
6. [Conclusión](#conclusión)  
   
---  
   
### Introducción  
   
En Python, el operador `in` y las funciones `any` y `all` son herramientas poderosas para verificar la pertenencia y evaluar condiciones en colecciones. Este documento proporciona una visión general y ejemplos prácticos de cómo usarlos.  
   
### Operador `in`  
   
El operador `in` se utiliza para verificar si un elemento está presente en una secuencia como una lista, una cadena, un conjunto o un diccionario. Devuelve `True` si el elemento está presente, y `False` en caso contrario.  
   
#### Uso con Listas  
   
```python  
# Ejemplo con listas  
frutas = ["manzana", "banana", "cereza"]  
print("manzana" in frutas)  # True  
print("naranja" in frutas)  # False  
```  
   
#### Uso con Cadenas  
   
```python  
# Ejemplo con cadenas  
saludo = "Hola mundo"  
print("Hola" in saludo)  # True  
print("Adiós" in saludo)  # False  
```  
   
#### Uso con Diccionarios  
   
```python  
# Ejemplo con diccionarios  
contactos = {"Alice": "555-1234", "Bob": "555-5678"}  
print("Alice" in contactos)  # True  
print("Charlie" in contactos)  # False  
```  
   
### Función `any`  
   
La función `any` toma un iterable (como una lista, tupla o conjunto) y devuelve `True` si al menos uno de los elementos es verdadero. De lo contrario, devuelve `False`.  
   
```python  
# Ejemplo con any  
numeros = [0, 1, 2, 3]  
print(any(numeros))  # True, porque hay elementos no cero  
   
# Otro ejemplo con any  
condiciones = [False, False, True]  
print(any(condiciones))  # True, porque al menos una condición es verdadera  
```  
   
### Función `all`  
   
La función `all` toma un iterable y devuelve `True` si todos los elementos son verdaderos. De lo contrario, devuelve `False`.  
   
```python  
# Ejemplo con all  
numeros = [1, 2, 3]  
print(all(numeros))  # True, porque todos los elementos son no cero  
   
# Otro ejemplo con all  
condiciones = [True, True, False]  
print(all(condiciones))  # False, porque no todas las condiciones son verdaderas  
```  
   
### Ejemplos Prácticos  
   
#### Verificar Pertenencia en una Lista  
   
```python  
# Verificar si un elemento está en una lista  
colores = ["rojo", "verde", "azul"]  
color_buscado = "verde"  
if color_buscado in colores:  
    print(f"El color {color_buscado} está en la lista.")  
else:  
    print(f"El color {color_buscado} no está en la lista.")  
```  
   
#### Uso de `any` y `all` con Condiciones  
   
¡Por supuesto! Continuemos con más ejemplos prácticos y la conclusión del documento.  
   
### Ejemplos Prácticos  
   
#### Verificar Pertenencia en una Lista  
   
```python  
# Verificar si un elemento está en una lista  
colores = ["rojo", "verde", "azul"]  
color_buscado = "verde"  
if color_buscado in colores:  
    print(f"El color {color_buscado} está en la lista.")  
else:  
    print(f"El color {color_buscado} no está en la lista.")  
```  
   
#### Uso de `any` y `all` con Condiciones  
   
```python  
# Uso de `any` para verificar si al menos una condición es verdadera  
condiciones = [False, True, False]  
if any(condiciones):  
    print("Al menos una de las condiciones es verdadera.")  
else:  
    print("Ninguna de las condiciones es verdadera.")  
   
# Uso de `all` para verificar si todas las condiciones son verdaderas  
condiciones = [True, True, True]  
if all(condiciones):  
    print("Todas las condiciones son verdaderas.")  
else:  
    print("No todas las condiciones son verdaderas.")  
```  
   
#### Verificación Compleja en Diccionarios  
   
```python  
# Verificar si una clave y un valor específico están en el diccionario  
contactos = {"Alice": "555-1234", "Bob": "555-5678"}  
nombre_buscado = "Alice"  
telefono_buscado = "555-1234"  
   
if nombre_buscado in contactos and contactos[nombre_buscado] == telefono_buscado:  
    print(f"El contacto {nombre_buscado} con teléfono {telefono_buscado} está en la lista.")  
else:  
    print(f"El contacto {nombre_buscado} con teléfono {telefono_buscado} no está en la lista.")  
```  
   
### Conclusión  
   
El operador `in` y las funciones `any` y `all` son herramientas poderosas y versátiles en Python que permiten verificar pertenencia y la claridad de tu código.  
   
Recuerda que:  
   
- El operador `in` es útil para verificar la presencia de un elemento en secuencias como listas, cadenas y dic evaluar condiciones en colecciones de manera eficiente.   
  
- Operador `in`: Permite comprobar si un elemento está presente en una secuencia (como listas,cionarios.  
- La función `any` devuelve `True` si al menos uno de los elementos en un iterable es verdadero.  
- La función `all` devuelve `True` si todos los elementos en un iterable son verdaderos.  
   
Utiliza estas herramientas para escribir código más limpio, eficiente y fácil de entender.  

### Reto: Gestión de Contactos  
**Descripción:**  
Vas a crear un sencillo sistema de gestión de contactos. Este sistema debe permitir agregar contactos, actualizar su número de teléfono, eliminar contactos y mostrar todos los contactos. Cada contacto tendrá un nombre y un número de teléfono.  
**Requisitos:**  

1. **Agregar Contacto:**  
    - El usuario debe poder agregar un contacto especificando el nombre y el número de teléfono.  
    - No debe permitir agregar contactos con el mismo nombre dos veces.  
   
2. **Actualizar Teléfono:**  
    - El usuario debe poder actualizar el número de teléfono de un contacto existente.  
   
3. **Eliminar Contacto:**  
    - El usuario debe poder eliminar un contacto de la lista por su nombre.  
   
4. **Mostrar Contactos:**  
    - El sistema debe poder mostrar una lista de todos los contactos, incluyendo nombre y número de teléfono.  
   
**Ejemplo de Implementación:**  
   
Aquí tienes un ejemplo de cómo implementar esto utilizando solo colecciones, condicionales y variables:  
   
```python  
# Colección para almacenar contactos  
contactos = {}  
   
# Agregar un contacto  
nombre = "Alice"  
telefono = "555-1234"  
   
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = telefono  
    print(f"Contacto {nombre} agregado con éxito.")  
   
# Intentar agregar el mismo contacto nuevamente  
nombre = "Alice"  
telefono = "555-5678"  
   
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = telefono  
    print(f"Contacto {nombre} agregado con éxito.")  
   
# Actualizar el teléfono de un contacto existente  
nombre = "Alice"  
nuevo_telefono = "555-5678"  
   
if nombre in contactos:  
    contactos[nombre] = nuevo_telefono  
    print(f"Teléfono de {nombre} actualizado a {nuevo_telefono}.")  
else:  
    print("El contacto no existe.")  
   
# Eliminar un contacto  
nombre = "Alice"  
   
if nombre in contactos:  
    del contactos[nombre]  
    print(f"Contacto {nombre} eliminado.")  
else:  
    print("El contacto no existe.")  
   
# Mostrar todos los contactos  
if contactos:  
    for nombre, telefono in contactos.items():  
        print(f"Nombre: {nombre}, Teléfono: {telefono}")  
else:  
    print("No hay contactos para mostrar.")  
   
# Intentar mostrar el contacto eliminado  
nombre = "Alice"  
   
if nombre in contactos:  
    print(f"Nombre: {nombre}, Teléfono: {contactos[nombre]}")  
else:  
    print("El contacto no existe.")  
```  
   
### Descripción de la Implementación:  
   
1. **Agregar un Contacto:**  
    - Verifica si el nombre del contacto ya existe en el diccionario `contactos`.  
    - Si no existe, se agrega el contacto con el nombre y el número de teléfono.  
   
2. **Actualizar Teléfono:**  
    - Verifica si el nombre del contacto existe en el diccionario `contactos`.  
    - Si existe, se actualiza el número de teléfono.  
   
3. **Eliminar Contacto:**  
    - Verifica si el nombre del contacto existe en el diccionario `contactos`.  
    - Si existe, se elimina el contacto del diccionario.  
   
4. **Mostrar Contactos:**  
    - Si hay contactos en el diccionario, se imprimen todos.  
    - Si el diccionario está vacío, se muestra un mensaje indicando que no hay contactos.  
   
### Tareas para los Estudiantes:  

1. **Agregar más Contactos:**
    - Practicar agregando más contactos con diferentes nombres y números de teléfono.
   
2. **Actualizar Teléfonos:**  
    - Practicar actualizando los números de teléfono de los contactos existentes.  
   
3. **Eliminar Contactos:**  
    - Practicar eliminando diferentes contactos del diccionario.  
   
4. **Mostrar Contactos:**  
    - Asegurarse de que el sistema puede mostrar correctamente todos los contactos después de varias operaciones de agregar, actualizar y eliminar.  
   
5. **Buscar Contacto:**  
    - Intentar buscar un contacto específico por su nombre y mostrar su información si existe.  
   
Aquí tienes una continuación del ejemplo para mostrar cómo los estudiantes pueden realizar estas tareas:  
   
```python  
# Colección para almacenar contactos  
contactos = {}  
   
# Agregar contactos  
nombre = "Alice"  
telefono = "555-1234"  
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = telefono  
    print(f"Contacto {nombre} agregado con éxito.")  
   
nombre = "Bob"  
telefono = "555-5678"  
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = telefono  
    print(f"Contacto {nombre} agregado con éxito.")  
   
nombre = "Charlie"  
telefono = "555-8765"  
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = telefono  
    print(f"Contacto {nombre} agregado con éxito.")  
   
# Actualizar el teléfono de un contacto existente  
nombre = "Bob"  
nuevo_telefono = "555-0000"  
if nombre in contactos:  
    contactos[nombre] = nuevo_telefono  
    print(f"Teléfono de {nombre} actualizado a {nuevo_telefono}.")  
else:  
    print("El contacto no existe.")  
   
# Eliminar un contacto  
nombre = "Charlie"  
if nombre in contactos:  
    del contactos[nombre]  
    print(f"Contacto {nombre} eliminado.")  
else:  
    print("El contacto no existe.")  
   
# Mostrar todos los contactos  
if contactos:  
    for nombre, telefono in contactos.items():  
        print(f"Nombre: {nombre}, Teléfono: {telefono}")  
else:  
    print("No hay contactos para mostrar.")  
   
# Buscar un contacto específico  
nombre = "Alice"  
if nombre in contactos:  
    print(f"Nombre: {nombre}, Teléfono: {contactos[nombre]}")  
else:  
    print("El contacto no existe.")  
```  
   
### Desafío Adicional  
   
Para añadir un poco más de complejidad y desafío, los estudiantes pueden intentar lo siguiente:  
   
1. **Verificar Datos:**  
    - Asegurarse de que los números de teléfono ingresados sean válidos (por ejemplo, que contengan solo dígitos y tengan una longitud específica).  
   
2. **Manejo de Errores:**  
    - Mejorar la robustez del sistema gestionando posibles errores, como entradas no válidas.  
   
3. **Más Información del Contacto:**  
    - Ampliar el sistema para incluir más información sobre cada contacto, como dirección de correo electrónico, dirección física, etc. Esto requeriría almacenar más datos en el diccionario, posiblemente utilizando una tupla o un diccionario anidado para cada contacto.  
   
### Ejemplo con Información Adicional:  
   
```python  
# Colección para almacenar contactos con información adicional  
contactos = {}  
   
# Agregar contacto con más información  
nombre = "Alice"  
telefono = "555-1234"  
email = "alice@example.com"  
direccion = "Calle 123, Ciudad"  
   
if nombre in contactos:  
    print("El contacto ya existe.")  
else:  
    contactos[nombre] = (telefono, email, direccion)  
    print(f"Contacto {nombre} agregado con éxito.")  
   
# Mostrar todos los contactos con información adicional  
if contactos:  
    for nombre, (telefono, email, direccion) in contactos.items():  
        print(f"Nombre: {nombre}, Teléfono: {telefono}, Email: {email}, Dirección: {direccion}")  
else:  
    print("No hay contactos para mostrar.")  
   
# Actualizar el teléfono de un contacto existente  
nombre = "Alice"  
nuevo_telefono = "555-5678"  
if nombre in contactos:  
    email, direccion = contactos[nombre][1], contactos[nombre][2]  
    contactos[nombre] = (nuevo_telefono, email, direccion)  
    print(f"Teléfono de {nombre} actualizado a {nuevo_telefono}.")  
else:  
    print("El contacto no existe.")  
   
# Eliminar un contacto  
nombre = "Alice"  
if nombre in contactos:  
    del contactos[nombre]  
    print(f"Contacto {nombre} eliminado.")  
else:  
    print("El contacto no existe.")  
   
# Buscar un contacto específico  
nombre = "Alice"  
if nombre in contactos:  
    telefono, email, direccion = contactos[nombre]  
    print(f"Nombre: {nombre}, Teléfono: {telefono}, Email: {email}, Dirección: {direccion}")  
else:  
    print("El contacto no existe.")  
```  
   
### Explicación de la Implementación Adicional:  
   
1. **Agregar Contacto con Más Información:**  
    - Se almacena un contacto con nombre, teléfono, email y dirección en el diccionario `contactos`. La información adicional (teléfono, email y dirección) se almacena en una tupla.  
    - Antes de agregar un contacto, se verifica que el nombre no exista ya en el diccionario.  
   
2. **Mostrar Contactos con Más Información:**  
    - Si el diccionario `contactos` no está vacío, se recorren los elementos del diccionario e imprimen todos los detalles de cada contacto.  
   
3. **Actualizar Teléfono de un Contacto Existente:**  
    - Se verifica si el nombre del contacto existe en el diccionario.  
    - Si existe, se actualiza el número de teléfono manteniendo el email y la dirección.  
   
4. **Eliminar un Contacto:**  
    - Se verifica si el nombre del contacto existe en el diccionario.  
    - Si existe, se elimina el contacto del diccionario.  
   
5. **Buscar un Contacto Específico:**  
    - Se verifica si el nombre del contacto existe en el diccionario.  
    - Si existe, se imprimen todos los detalles del contacto.