# numero = 5 
# if numero > 1:
#     print("Es mayor que uno")

# else 

# edad = 16
# altura = 170
# if (edad > 14 and altura > 150):
#     print("Puede salir a la fiesta")

# numero = 4
# if numero < 3:
#     print("Es menor que 3")
# elif numero <= 6:
#     print("El numero esta entre 3 y 5")
# else:
#     print("El es mayor o igual a 6")


# edad = int(input("Ingrese su edad "))

# if edad >= 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

# Enunciado del Ejercicio:
# Título: Determinar el tipo de triángulo

# Escribe un programa en Python que solicite al usuario ingresar las longitudes de los tres lados de un triángulo. El programa debe determinar e imprimir el tipo de triángulo basado en las siguientes condiciones:

# Triángulo equilátero: Todos los lados son iguales.
# Triángulo isósceles: Dos lados son iguales y uno es diferente.
# Triángulo escaleno: Todos los lados son diferentes.
# No es un triángulo: Si la suma 
# Si el usuario ingresa los valores 5, 5, 5, el programa debería imprimir: Es un triángulo equilátero.
# Si el usuario ingresa los valores 5, 5, 8, el programa debería imprimir: Es un triángulo isósceles.
# Si el usuario ingresa los valores 3, 4, 5, el programa debería imprimir: Es un triángulo escaleno.
# Si el usuario ingresa los valores 1, 2, 3, el programa debería imprimir: No es un triángulo.
# Pistas:
# Recuerda que para que tres lados formen un triángulo, la suma de las longitudes de dos lados cualesquiera debe ser mayor que la longitud del tercer lado.
# Utiliza condicionales if-else anidados para verificar las condiciones mencionadas.

print("Tipo de triangulo")

longitud1 = float(input("Ingrese el primer lado: "))
longitud2 = float(input("Ingrese el segundo lado: "))
longitud3 = float(input("Ingrese el tercer lado: "))

if (longitud1 + longitud2 > longitud3) and (longitud1 + longitud3 > longitud2) and (longitud2 + longitud3 > longitud1):
    if (longitud1 == longitud2 == longitud3):
        print("Es un triángulo equilátero.")
    elif (longitud1 == longitud2 or longitud1 == longitud3 or longitud2 == longitud3):
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("No es un triángulo.")


















# if (longitud1 == 5) and (longitud2 == 5) and (longitud3 == 5):
#     print("Es un triángulo equilátero.")

# elif (longitud1 == 5) and (longitud2 == 5) and (longitud3 == 8):
#     print("Es un triángulo isósceles.")
# elif (longitud1 == 3) and (longitud2 == 4) and (longitud3 == 5):
#     print("Es un triángulo escaleno.")
# elif (longitud1 == 1) and (longitud2 == 2) and (longitud3 == 3):
#     print("No es un triángulo.")
# else: 
#     print()  




