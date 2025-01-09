# Introducción a los Bucles en Python  
   
## ¿Qué es un Bucle?  
   
Un bucle es una estructura de control que permite ejecutar un bloque de código repetidamente mientras se cumpla una condición determinada. En Python, los bucles son esenciales para automatizar tareas repetitivas y manejar colecciones de datos de manera eficiente.  
   
Python proporciona dos tipos principales de bucles:  
1. **Bucle `while`**  
2. **Bucle `for`**  
   
## Bucle `while`  
   
El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.  
   
### Sintaxis  
   
```python  
while condición:  
    # Bloque de código que se ejecuta mientras la condición sea verdadera  
```  
   
### Ejemplo  
   
```python  
contador = 0  
   
while contador < 5:  
    print("El contador es:", contador)  
    contador += 1  
```  
   
En este ejemplo, el bucle `while` continuará ejecutándose mientras el valor de `contador` sea menor que 5. En cada iteración, el valor de `contador` se incrementa en 1.  
   
## Bucle `for`  
   
El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de caracteres).  
   
### Sintaxis  
   
```python  
for variable in secuencia:  
    # Bloque de código que se ejecuta para cada elemento en la secuencia  
```  
   
### Ejemplo  
   
```python  
frutas = ["manzana", "banana", "cereza"]  
   
for fruta in frutas:  
    print("Me gusta comer", fruta)  
```  
   
En este ejemplo, el bucle `for` itera sobre cada elemento de la lista `frutas` y ejecuta el bloque de código para cada fruta.  
   
## La Función `range()`  
   
La función `range()` se utiliza comúnmente con los bucles `for` para generar una secuencia de números.  
   
### Sintaxis  
   
```python  
range(inicio, fin, paso)  
```  
   
- `inicio` (opcional): El valor inicial de la secuencia. Por defecto es 0.  
- `fin` (obligatorio): El valor final de la secuencia (no incluido en la secuencia).  
- `paso` (opcional): El valor en el que la secuencia se incrementa. Por defecto es 1.  
   
### Ejemplo  
   
```python  
for i in range(5):  
    print(i)  
```  
   
Este bucle imprimirá los números del 0 al 4.  
   
## Declaraciones `break` y `continue`  
   
### Declaración `break`  
   
La declaración `break` se utiliza para salir de un bucle de manera anticipada.  
   
### Ejemplo  
   
```python  
for i in range(10):  
    if i == 5:  
        break  
    print(i)  
```  
   
Este bucle imprimirá los números del 0 al 4 y luego se detendrá cuando `i` sea igual a 5.  
   
### Declaración `continue`  
   
La declaración `continue` se utiliza para saltar la iteración actual y continuar con la siguiente iteración del bucle.  
   
### Ejemplo  
   
```python  
for i in range(10):  
    if i % 2 == 0:  
        continue  
    print(i)  
```  
   
Este bucle imprimirá solo los números impares del 0 al 9.  
   
## Bucle `for` con Diccionarios  
   
Puedes iterar sobre los elementos de un diccionario utilizando un bucle `for`.  
   
### Ejemplo  
   
```python  
estudiantes = {"Alice": 25, "Bob": 22, "Charlie": 23}  
   
for nombre, edad in estudiantes.items():  
    print(nombre, "tiene", edad, "años")  
```  
   
En este ejemplo, el bucle `for` itera sobre los pares clave-valor del diccionario `estudiantes`.  
## Bucle `while` y `for` con `else`  
   
En Python, tanto los bucles `while` como los `for` pueden tener una cláusula `else`. El bloque de código dentro del `else` se ejecuta cuando el bucle termina normalmente (es decir, cuando la condición del `while` se vuelve falsa o el `for` ha terminado de iterar sobre la secuencia), pero no se ejecuta si el bucle se interrumpe con una declaración `break`.  
   
### Ejemplo con `while`  
   
```python  
contador = 0  
   
while contador < 5:  
    print("El contador es:", contador)  
    contador += 1  
else:  
    print("El bucle while ha terminado")  
```  
   
En este ejemplo, el bloque `else` se ejecuta después de que el bucle `while` termine normalmente.  
   
### Ejemplo con `for`  
   
```python  
for i in range(5):  
    print(i)  
else:  
    print("El bucle for ha terminado")  
```  
   
En este caso, el bloque `else` se ejecuta después de que el bucle `for` termine de iterar sobre la secuencia.  
   
## Anidamiento de Bucles  
   
Los bucles pueden anidarse, es decir, puedes colocar un bucle dentro de otro bucle. Esto es útil para trabajar con estructuras de datos multidimensionales o realizar operaciones complejas.  
   
### Ejemplo  
   
```python  
for i in range(3):  
    for j in range(3):  
        print(f"i: {i}, j: {j}")  
```  
   
En este ejemplo, el bucle externo `for` se ejecuta tres veces y, dentro de cada iteración del bucle externo, el bucle interno `for` también se ejecuta tres veces. Esto resulta en un total de 9 combinaciones de valores para `i` y `j`.  
   
## Práctica y Ejercicios  
   
Para familiarizarte con los bucles en Python, aquí tienes algunos ejercicios:  
   
1. **Suma de Números**:  
    Escribe un programa que calcule la suma de los primeros 10 números naturales utilizando un bucle `for`.  
  
    ```python  
    suma = 0  
  
    for i in range(1, 11):  
        suma += i  
  
    print("La suma de los primeros 10 números naturales es:", suma)  
    ```  
   
2. **Tabla de Multiplicar**:  
    Escribe un programa que imprima la tabla de multiplicar de un número dado utilizando un bucle `while`.  
  
    ```python  
    numero = int(input("Introduce un número: "))  
    multiplicador = 1  
  
    while multiplicador <= 10:  
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")  
        multiplicador += 1  
    ```  
   
3. **Contar Vocales**:  
    Escribe un programa que cuente el número de vocales en una cadena de texto utilizando un bucle `for`.  
  
    ```python  
    texto = "Hola Mundo"  
    vocales = "aeiouAEIOU"  
    contador_vocales = 0  
  
    for letra in texto:  
        if letra in vocales:  
            contador_vocales += 1  
  
    print("El número de vocales en la cadena es:", contador_vocales)  
    ```  
   
4. **Números Primos**:  
    Escribe un programa que imprima todos los números primos entre 1 y 50 utilizando bucles anidados.  
  
    ```python  
    for num in range(2, 51):  
        es_primo = True  
        for i in range(2, num):  
            if num % i == 0:  
                es_primo = False  
                break  
        if es_primo:  
            print(num)  
    ```  
   
## Conclusión  
   
Los bucles son herramientas fundamentales en la programación que te permiten ejecutar bloques de código repetidamente, lo que es esencial para manejar tareas repetitivas y trabajar con colecciones de datos. En Python, los bucles `while` y `for` son las estructuras básicas que te permitirán implementar esta funcionalidad.  
   
### Resumen de Conceptos:  
   
1. **Bucle `while`**:  
    - Ejecuta un bloque de código mientras una condición sea verdadera.  
    - Puede incluir una cláusula `else` que se ejecuta cuando el bucle termina normalmente.  
   
2. **Bucle `for`**:  
    - Itera sobre una secuencia (lista, tupla, diccionario, conjunto, cadena de caracteres).  
    - Comúnmente se usa con la función `range()` para generar secuencias numéricas.  
    - Puede incluir una cláusula `else` que se ejecuta cuando el bucle termina normalmente.  
   
3. **Declaraciones `break` y `continue`**:  
    - `break`: Interrumpe el bucle de manera anticipada.  
    - `continue`: Salta la iteración actual y continúa con la siguiente.  
   
4. **Anidamiento de Bucles**:  
    - Permite colocar un bucle dentro de otro para manejar estructuras de datos más complejas o realizar operaciones anidadas.  
   
### Ejercicios Prácticos:  
   
La práctica es clave para dominar cualquier habilidad de programación. Aquí tienes algunos ejercicios adicionales para seguir practicando:  
   
1. **Números Pares**:  
    Escribe un programa que imprima todos los números pares del 1 al 20 utilizando un bucle `for`.  
  
    ```python  
    for num in range(1, 21):  
        if num % 2 == 0:  
            print(num)  
    ```  
   
2. **Factorial de un Número**:  
    Escribe un programa que calcule el factorial de un número dado utilizando un bucle `while`.  
  
    ```python  
    numero = int(input("Introduce un número: "))  
    factorial = 1  
    contador = 1  
  
    while contador <= numero:  
        factorial *= contador  
        contador += 1  
  
    print(f"El factorial de {numero} es: {factorial}")  
    ```  
   
3. **Encontrar el Máximo en una Lista**:  
    Escribe un programa que encuentre el número máximo en una lista de números utilizando un bucle `for`.  
  
    ```python  
    numeros = [3, 7, 2, 8, 5, 10, 6]  
    maximo = numeros[0]  
  
    for numero in numeros:  
        if numero > maximo:  
            maximo = numero  
  
    print("El número máximo en la lista es:", maximo)  
    ```  
   
4. **Imprimir un Patrón**:  
    Escribe un programa que imprima el siguiente patrón utilizando bucles anidados:  
  
    ```  
    *  
    **  
    ***  
    ****  
    *****  
    ```  
  
    ```python  
    for i in range(1, 6):  
        for j in range(i):  
            print("*", end="")  
        print()  # Nueva línea después de cada fila  
    ```  
   
### Recursos Adicionales:  
   
Para profundizar más en los bucles y otras estructuras de control en Python, considera consultar la documentación oficial de Python y otros recursos educativos en línea. Aquí hay algunos enlaces útiles:  
   
- [Documentación Oficial de Python](https://docs.python.org/3/)  
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)  
- [Python for Everybody (Coursera)](https://www.coursera.org/specializations/python)  
   
### Palabras Finales:  
   
Los bucles son una de las primeras grandes herramientas que aprenderás en programación y son fundamentales para muchos algoritmos y estructuras de datos. Al comprender cómo funcionan los bucles

   
### Reto: Juego de Adivinanza de Números  
   
**Descripción:**  
El objetivo de este juego es que el usuario adivine un número secreto generado aleatoriamente por el programa. El juego le dará pistas al usuario indicando si su suposición es demasiado alta o demasiado baja. El juego termina cuando el usuario adivina el número o decide rendirse.  
   
**Instrucciones:**  
   
1. El programa debe generar un número secreto aleatorio entre 1 y 100.  
2. El usuario debe tener un número limitado de intentos para adivinar el número.  
3. Después de cada intento, el programa debe indicar si el número ingresado por el usuario es mayor o menor que el número secreto.  
4. Si el usuario adivina el número, el programa debe felicitarlo y mostrar cuántos intentos tomó.  
5. El usuario puede rendirse en cualquier momento ingresando un valor específico (por ejemplo, "0").  
6. Si el usuario se rinde o agota sus intentos, el programa debe revelar el número secreto.  
   
**Pistas:**  
- Usa la biblioteca `random` para generar el número aleatorio.  
- Utiliza un bucle `while` para permitir múltiples intentos.  
- Usa variables para contar el número de intentos.  
- Utiliza condicionales para verificar las suposiciones del usuario y proporcionar retroalimentación.  
- Usa una lista para almacenar los intentos del usuario (opcional, pero puede ser útil para mostrar un historial de intentos).  
   
Aquí tienes una versión de codificación del reto de adivinanza de números. Esta versión utiliza variables, operadores aritméticos y booleanos, colecciones, condicionales y bucles, tal como especificaste.  
   
```python  
import random  
   
# Generar un número secreto aleatorio entre 1 y 100  
numero_secreto = random.randint(1, 100)  
intentos = 0  
max_intentos = 10  
historial_intentos = []  
   
print("¡Bienvenido al juego de adivinanza de números!")  
print(f"Adivina el número entre 1 y 100. Tienes {max_intentos} intentos. Ingresa '0' para rendirte.")  
   
# Bucle principal del juego  
while intentos < max_intentos:  
    intento = int(input("Ingresa tu adivinanza: "))  
    if intento == 0:  
        print(f"Te has rendido. El número secreto era {numero_secreto}.")  
        break  
  
    intentos += 1  
    historial_intentos.append(intento)  
  
    if intento < numero_secreto:  
        print("Demasiado bajo. Inténtalo de nuevo.")  
    elif intento > numero_secreto:  
        print("Demasiado alto. Inténtalo de nuevo.")  
    else:  
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")  
        break  
   
if intento != numero_secreto:  
    print(f"Lo siento, has agotado tus {max_intentos} intentos. El número secreto era {numero_secreto}.")  
    print("Historial de intentos:", historial_intentos)  
```  
   
Este código contiene todos los elementos necesarios:  
   
- **Variables:** `numero_secreto`, `intentos`, `max_intentos`, `historial_intentos`, `intento`.  
- **Operadores aritméticos y booleanos:** `+=`, `<`, `>`, `==`.  
- **Colecciones:** `historial_intentos` (una lista que almacena los intentos del usuario).  
- **Condicionales:** `if`, `elif`, `else` para verificar las suposiciones del usuario y proporcionar retroalimentación.  
- **Bucles:** `while` para permitir múltiples intentos de adivinanza.  
   
Espero que este reto sea desafiante y educativo para tus alumnos. ¡Buena suerte!