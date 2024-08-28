numero = int(input("Ingrese un numero entero positivo: "))
contador = 1

if numero > 0:
    for i in range(numero):
        print(i)
else:
    print("Incorrecto! Ingrese un numero entero positivo.")