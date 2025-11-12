#Primer código del curso
print ("Hola Mundo")

# Esto es una variable

A = "Letra"
B = 20
print ("La palabra es", A, "y el número es", B)

# Imprime los números pares desde el 0 hasta n
n = int(input("Elige un número"))
for i in range (n + 1):
    if i % 2 == 0:
        print(i)
    else:
        print (f"{i} (Impar)")

