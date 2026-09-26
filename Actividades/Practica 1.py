# Ejercicio 1: Unión de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Elementos que están en A o en B, o en ambos:")
print(A | B)

# Ejercicio 2: Intersección de conjuntos
print("\nElementos que están en A y en B:")
print(A & B)

# Ejercicio 3: Diferencia simétrica
print("\nElementos que están en A o en B, pero no en ambos:")
print(A ^ B)

# Ejercicio 4: Comprobar si A es subconjunto de B
print("\n¿A es subconjunto de B?")
print(A.issubset(B))

# Ejercicio 5: Cantidad de elementos del conjunto A
print("\nNúmero de elementos de A:")
print(len(A))