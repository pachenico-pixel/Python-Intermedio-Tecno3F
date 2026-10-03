# 1. Dividir dos números - ZeroDivisionError

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    resultado = numero1 / numero2

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")


# 2. Sumar un número y una cadena - TypeError

try:
    numero = 10
    texto = "Hola"

    resultado = numero + texto

    print("Resultado:", resultado)

except TypeError:
    print("Error: no se puede sumar un número con una cadena.")


# 3. Acceder a una clave que no existe - KeyError

try:
    persona = {
        "nombre": "Nicolas",
        "edad": 20
    }

    print(persona["direccion"])

except KeyError:
    print("Error: la clave no existe en el diccionario.")


# 4. Abrir un archivo que no existe - FileNotFoundError

try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()

    print(contenido)

    archivo.close()

except FileNotFoundError:
    print("Error: el archivo no existe.")

    archivo = open("archivo.txt", "w")
    archivo.close()

    print("El archivo fue creado correctamente.")


# 5. Dividir dos números - ZeroDivisionError y ValueError

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    resultado = numero1 / numero2

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

except ValueError:
    print("Error: debe ingresar números válidos.")
