# Ejercicio 1: Calcular el mayor de dos números
# usando un operador ternario

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mayor = num1 if num1 > num2 else num2

print("El mayor es:", mayor)


# ==========================================
# Ejercicio 2: Buscar una palabra en una lista
# usando *args y un operador ternario

def buscar_palabra(palabra, *args):
    mensaje = "La palabra está en la lista" if palabra in args else "La palabra no está en la lista"
    print(mensaje)


palabra_buscada = input("\nIngrese la palabra que desea buscar: ")
cantidad = int(input("¿Cuántas palabras desea ingresar?: "))

palabras = []

for i in range(cantidad):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    palabras.append(palabra)

buscar_palabra(palabra_buscada, *palabras)


# ==========================================
# Ejercicio 3: Determinar si un número
# es par o impar

numero = int(input("\nIngrese un número entero: "))

resultado = "Par" if numero % 2 == 0 else "Impar"

print("El número es:", resultado)


# ==========================================
# Ejercicio 4: Calcular el promedio de una lista
# de números usando *args y un operador ternario

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else None

    if promedio is not None:
        print("El promedio es:", promedio)
    else:
        print("Error: no se ingresaron números.")


cantidad_numeros = int(input("\n¿Cuántos números desea ingresar?: "))

numeros = []

for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

calcular_promedio(*numeros)


# ==========================================
# Ejercicio 5: Imprimir un mensaje de error
# si no se pasan suficientes argumentos

def mostrar_datos(nombre, edad, *args):
    if nombre and edad is not None:
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Argumentos adicionales:", args)
    else:
        print("Error: faltan argumentos.")


# Ejemplo de llamada correcta
mostrar_datos("Juan", 25, "Estudiante")

# Ejemplo de llamada con argumentos insuficientes
try:
    mostrar_datos("Juan")
except TypeError:
    print("Error: no se pasaron suficientes argumentos.")

