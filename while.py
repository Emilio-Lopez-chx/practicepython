# dia = 0
# semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

# while dia < 7:
#     print("Hoy es: "+ semana[dia])
#     dia += 1    

# contador = 1
# while contador <=5:
#     print(contador)
#     contador += 1

# contador = 1
# while (contador <= 5):
#     contador = contador + 1
#     print("Iteracion numero ",contador)

# contador = 0
# while contador  < 15:
#     contador += 1
#     print("Iteracion ", contador)
#     if contador == 5:
#         break
#     print("Fin")

#Escribe un programa en Python que use un bucle while para sumar
# números ingresados por el usuario hasta que se ingrese un número 
# negativo. Luego, muestra la suma total.

# suma = 0
# while True:
#     numero = float(input("Ingrese el primer numero a sumar(si quiere salir ingrese un numero negativo): "))
#     if numero < 0:
#         break
#     suma += numero 

# print("la suma total es: ",suma)    


#Escribe un programa en Python que utilice un bucle while para 
# encontrar y mostrar el primer número divisible por 7 en el rango del 1 al 100.


# num = 4

# while  num <= 100:
#     if num % 7 == 0:
#         print("El numero divisible por 7 en el rango es ",num)
#         break
#     num += 1
# '''
# #Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
# #cuántos tienen notas mayores o iguales a 7 y cuántos menores.
# '''

# nota_mayores = 0
# notas_menores = 0
# i = 1
# while i <= 10:
#     nota = float(input(f"Ingrese la nota{i}: "))
#     if nota >= 7 and nota <= 10:
#         nota_mayores += 1
#     else:
#         notas_menores += 1
#     i += 1

# print("La cantidad de notas del estudiante mayores a 7 son: ",nota_mayores)  
# print("La cantidad de notas del estudiante menores a 7 son: ",notas_menores)      

#crear un programa donde cuente de forma desendente 10 segundos para que explote una bomba
#print("!BOOMMMMMMMMMMMMMMMMMM!!!!!")


# contador = 10

# while contador > 0:
#     print("La bomba explotara en: ",contador, "segundos")
#     contador -= 1
# print("!BOOMMM!!!")


# Árbol de navidad en Python. Imprime un árbol de navidad formado 
# con * haciendo uso del while y de la multiplicación de un entero 
# por una cadena, cuyo resultado en Python es replicar la cadena.


# tree = 9
# i = 1
# while tree > 0:
#     print(" "* tree + "*" * i +  "" * tree)
#     tree += 2
#     i -= 1



#Escribe un programa en Python que use un bucle while para calcular el 
# factorial de un número ingresado por el usuario. El factorial de un
#  número n es el producto de todos los números enteros positivos menores
#  o iguales a n (es decir, n! = n * (n-1) * (n-2) * ... * 1).


# factorial = 0

# while True:
#     numero = float(input("Ingrese un numero"))
    
