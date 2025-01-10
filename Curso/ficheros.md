   
# Curso de Python para Principiantes: Trabajo con Ficheros  
   
## Introducción  
Este curso está diseñado para aquellos que están comenzando a aprender Python y desean comprender cómo trabajar con ficheros. Aprenderemos a abrir, leer, escribir y cerrar archivos, así como algunas prácticas recomendadas y errores comunes a evitar.  
   
### Objetivos del Curso  
Al finalizar este curso, los estudiantes serán capaces de:  
1. Entender los conceptos básicos de manejo de ficheros en Python.  
2. Leer y escribir archivos de texto.  
3. Trabajar con archivos CSV.  
4. Utilizar el manejo de errores para asegurar que los ficheros se cierren correctamente.  
5. Aplicar buenas prácticas al trabajar con ficheros.  
   
## 1. Introducción a los Ficheros en Python  
   
### 1.1. ¿Qué es un fichero?  
Un fichero es una colección de datos almacenados en un dispositivo de almacenamiento, como un disco duro. Los ficheros pueden contener diferentes tipos de datos, como texto, imágenes, videos, etc.  
   
- **Ficheros de texto**: Contienen datos en formato de texto plano, que pueden ser leídos y editados con cualquier editor de texto.  
- **Ficheros binarios**: Contienen datos en un formato binario, que solo pueden ser leídos y entendidos por programas específicos.  
   
### 1.2. Por qué es importante trabajar con ficheros  
Trabajar con ficheros es fundamental porque:  
- Permite almacenar datos de manera persistente, es decir, los datos no se pierden cuando se cierra el programa.  
- Facilita el intercambio de datos entre diferentes aplicaciones o sistemas.  
- Permite manejar grandes cantidades de datos de manera eficiente.  
   
## 2. Operaciones Básicas con Ficheros  
   
### 2.1. Abrir y Cerrar Archivos  
Para trabajar con un fichero, primero debemos abrirlo. En Python, utilizamos la función `open()` para abrir un archivo. Es importante cerrar los archivos después de usarlos para liberar los recursos del sistema. La función `close()` se utiliza para cerrar un archivo.  
   
- **Modos de apertura de archivos**:  
  - `'r'`: Lectura (por defecto). El archivo debe existir.  
  - `'w'`: Escritura. Crea un archivo nuevo o sobreescribe uno existente.  
  - `'a'`: Añadir. Escribe al final del archivo.  
  - `'b'`: Modo binario.  

#### Ejercicio 1:  
Abre un archivo llamado `mi_archivo.txt` en modo lectura y cierra el archivo después.

```python  
file = open('archivo.txt', 'r')  
# Realizar operaciones con el archivo  
file.close()  
```  

### 2.2. Uso del Context Manager (`with`)  
El uso de `with` para abrir archivos es una práctica recomendada ya que se asegura de que los archivos se cierren correctamente incluso si ocurre una excepción.  
   
```python  
with open('archivo.txt', 'r') as file:  
    # Realizar operaciones con el archivo  
```  
   
#### Ejercicio 2:  
Abre el archivo `mi_archivo.txt` usando `with` y asegúrate de que se cierre automáticamente.  
   
## 3. Leer Ficheros  
   
### 3.1. Leer el contenido completo  
La función `read()` lee todo el contenido del archivo y lo devuelve como una cadena.  
   
```python  
with open('archivo.txt', 'r') as file:  
    content = file.read()  
    print(content)  
```  
   
#### Ejercicio 3:  
Crea un archivo llamado `datos.txt` con algunos textos. Luego, escribe un programa que lea y muestre el contenido completo del archivo.  
   
### 3.2. Leer línea por línea  
Leer línea por línea es útil cuando trabajamos con archivos grandes y no queremos cargar todo el contenido en memoria a la vez.  
   
- **`readline()`**: Lee una línea del archivo.  
- **`readlines()`**: Lee todas las líneas del archivo y las devuelve como una lista de cadenas.  
   
```python  
with open('archivo.txt', 'r') as file:  
    for line in file:  
        print(line, end='')  # Evita la doble línea en la salida  
```  
   
#### Ejercicio 4:  
Escribe un programa que lea `datos.txt` línea por línea y muestre cada línea.  
   
## 4. Escribir en Ficheros  
   
### 4.1. Escribir datos  
La función `write()` permite escribir cadenas en un archivo.  
   
```python  
with open('archivo.txt', 'w') as file:  
    file.write('Este es un ejemplo de escritura.\n')  
```  
   
#### Ejercicio 5:  
Crea un programa que escriba "Hola, Mundo!" en un archivo llamado `saludo.txt`.  
   
### 4.2. Añadir datos  
El modo de apertura `'a'` permite añadir datos al final del archivo sin sobrescribir el contenido existente.  
   
```python  
with open('archivo.txt', 'a') as file:  
    file.write('Añadiendo una nueva línea.\n')  
```  
   
#### Ejercicio 6:  
Escribe un programa que añada "Esta es una nueva línea." al final de `saludo.txt`.  
   
## 5. Trabajo con Archivos CSV  
   
### 5.1. Introducción a CSV  
Un archivo CSV (Comma Separated Values) es un archivo de texto que utiliza comas para separar valores. Es comúnmente usado para almacenar datos tabulares.  
   
- La librería `csv` de Python proporciona funcionalidades para trabajar con archivos CSV.  
   
### 5.2. Leer archivos CSV  
El método `csv.reader()` permite leer archivos CSV.  
   
```python  
import csv  
   
with open('archivo.csv', 'r') as file:  
    reader = csv.reader(file)  
    for row in reader:  
        print(row)  
```  
   
#### Ejercicio 7:  
Crea un archivo CSV llamado `datos.csv` con las siguientes filas:  
```  
nombre,edad,ciudad  
Juan,28,Madrid  
Ana,22,Barcelona  
Luis,35,Valencia  
```  
Luego, escribe un programa que lea y muestre el contenido de `datos.csv`.  
   
### 5.3. Escribir archivos CSV  
El método `csv.writer()` permite escribir datos en un archivo CSV.  
   
```python  
import csv  
   
with open('archivo.csv', 'w', newline='') as file:  
    writer = csv.writer(file)  
    writer.writerow(['nombre', 'edad', 'ciudad'])  
    writer.writerow(['Juan', '28', 'Madrid'])  
```  
   
#### Ejercicio 8:  
Escribe un programa que cree un archivo CSV llamado `nuevos_datos.csv` y añada las siguientes filas:  
```  
nombre,edad,ciudad  
Marta,30,Sevilla  
Carlos,25,Zaragoza  
```  
   
## Reto Final  
   
### Reto: Gestor de Contactos  
Crea un programa que gestione una lista de contactos utilizando un archivo CSV. El programa debe permitir las siguientes operaciones:  
1. **Agregar contacto**: Solicita el nombre, la edad y la ciudad y añade el contacto al archivo.  
2. **Ver contactos**: Lee y muestra todos los contactos del archivo.  
3. **Buscar contacto**: Solicita un nombre y muestra los detalles del contacto si se encuentra en el archivo.  
4. **Eliminar contacto**: Solicita un nombre y elimina el contacto del archivo si existe.  
   
#### Pistas

- Utiliza `csv.DictReader` y `csv.DictWriter` para trabajar con archivos CSV utilizando diccionarios, lo cual facilita el manejo de los datos.  
- Asegúrate de manejar correctamente los casos en los que el archivo no existe o está vacío.  
- Implementa un menú para que el usuario pueda seleccionar las diferentes operaciones.  

### Explicación del código

1. **Acciones de agregar, ver, buscar y eliminar contactos**:  
   - `agregar_contacto`: Solicita al usuario el nombre, la edad y la ciudad del contacto, y luego agrega esta información al archivo CSV utilizando `csv.DictWriter`.  
   - `ver_contactos`: Lee y muestra todos los contactos del archivo CSV utilizando `csv.DictReader`. Si el archivo no existe, muestra un mensaje de error.  
   - `buscar_contacto`: Solicita al usuario el nombre del contacto que desea buscar y muestra los detalles del contacto si se encuentra en el archivo.  
   - `eliminar_contacto`: Solicita al usuario el nombre del contacto que desea eliminar. Si el contacto se encuentra en el archivo, se elimina y se actualiza el archivo CSV.  
   
2. **Función `main`**:  
   - La función `main` proporciona un menú interactivo para que el usuario seleccione las diferentes operaciones (agregar, ver, buscar, eliminar o salir).  
   - Utiliza un bucle `while` para mantener el programa en ejecución hasta que el usuario elija salir.  
   
### Ejercicio Final:  
Implementa el programa completo siguiendo la estructura y las funciones proporcionadas. Asegúrate de probar todas las funcionalidades (agregar, ver, buscar y eliminar contactos) para asegurarte de que el programa funciona correctamente.  
   
#### Recomendaciones:  
- Asegúrate de que las operaciones de escritura y lectura en el archivo CSV manejen correctamente los casos en los que el archivo está vacío o no existe.  
- Utiliza el manejo de excepciones (`try-except`) para capturar y manejar errores como el archivo no encontrado.  
- Valida la entrada del usuario para asegurarte de que los datos ingresados sean correctos y completos.  
   
### Conclusión  
Trabajar con ficheros es una habilidad esencial en la programación. Este curso te ha proporcionado una base sólida para leer, escribir y manipular archivos en Python. Con los conocimientos adquiridos, puedes manejar datos de manera eficiente y persistente en tus proyectos.

Aquí tienes el código del reto final sin utilizar funciones. Todo el código se encuentra en el bloque principal y se organiza utilizando un bucle y estructuras condicionales:

```python  
import csv  
   
filename = 'contactos.csv'  
   
while True:  
    print("\nGestor de Contactos")  
    print("1. Agregar Contacto")  
    print("2. Ver Contactos")  
    print("3. Buscar Contacto")  
    print("4. Eliminar Contacto")  
    print("5. Salir")  
      
    opcion = input("Selecciona una opción: ")  
      
    if opcion == '1':  
        nombre = input("Introduce el nombre: ")  
        edad = input("Introduce la edad: ")  
        ciudad = input("Introduce la ciudad: ")  
          
        with open(filename, 'a', newline='') as file:  
            writer = csv.DictWriter(file, fieldnames=['nombre', 'edad', 'ciudad'])  
            # Escribir el encabezado solo si el archivo está vacío  
            file.seek(0)  
            if file.tell() == 0:  
                writer.writeheader()  
            writer.writerow({'nombre': nombre, 'edad': edad, 'ciudad': ciudad})  
        print("Contacto agregado exitosamente.")  
      
    elif opcion == '2':  
        try:  
            with open(filename, 'r') as file:  
                reader = csv.DictReader(file)  
                contactos = list(reader)  
                if contactos:  
                    for row in contactos:  
                        print(f"Nombre: {row['nombre']}, Edad: {row['edad']}, Ciudad: {row['ciudad']}")  
                else:  
                    print("No hay contactos para mostrar.")  
        except FileNotFoundError:  
            print("El archivo no existe. Agrega un contacto primero.")  
      
    elif opcion == '3':  
        nombre_buscar = input("Introduce el nombre del contacto a buscar: ")  
        try:  
            with open(filename, 'r') as file:  
                reader = csv.DictReader(file)  
                encontrado = False  
                for row in reader:  
                    if row['nombre'] == nombre_buscar:  
                        print(f"Nombre: {row['nombre']}, Edad: {row['edad']}, Ciudad: {row['ciudad']}")  
                        encontrado = True  
                        break  
                if not encontrado:  
                    print("Contacto no encontrado.")  
        except FileNotFoundError:  
            print("El archivo no existe. Agrega un contacto primero.")  
      
    elif opcion == '4':  
        nombre_eliminar = input("Introduce el nombre del contacto a eliminar: ")  
        contactos = []  
        contacto_encontrado = False  
          
        try:  
            with open(filename, 'r') as file:  
                reader = csv.DictReader(file)  
                for row in reader:  
                    if row['nombre'] == nombre_eliminar:  
                        contacto_encontrado = True  
                    else:  
                        contactos.append(row)  
              
            if contacto_encontrado:  
                with open(filename, 'w', newline='') as file:  
                    writer = csv.DictWriter(file, fieldnames=['nombre', 'edad', 'ciudad'])  
                    writer.writeheader()  
                    writer.writerows(contactos)  
                print("Contacto eliminado exitosamente.")  
            else:  
                print("Contacto no encontrado.")  
        except FileNotFoundError:  
            print("El archivo no existe. Agrega un contacto primero.")  
      
    elif opcion == '5':  
        print("Saliendo del gestor de contactos...")  
        break  
      
    else:  
        print("Opción no válida. Inténtalo de nuevo.")  
```
