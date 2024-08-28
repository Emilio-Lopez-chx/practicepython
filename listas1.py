frutas = ["manzanas", "peras", "uvas", "banano"]
numeros = [89,87,53,65,34]

frutas.append("sandia") #para agregar un elemento a la lista
frutas.insert(0,"papaya")# para agregar un elemento en una posicion especifica de la
frutas.extend(["mango", "kiwi", "lulo"])#Agregar multiples elementos a la lista
frutas[8] = "mora" #editar un elemento de la lista
frutas.remove("papaya")#Para remover un elemento de la lista

del frutas[7]#para eliminar un elemento de la lista con el numero del elemento
del frutas[0:4]#Eliminar por rangos

frutas.clear()
# frutaEliminar = frutas.pop(0)#me saca de la lista un elemento y lo agrega a una variable

print(frutas)
# print(frutas)
# print(frutaEliminar)

#Escribe un programa en Python que permita al usuario crear una lista de compras. 
# El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno 
# y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, 
# el programa debe imprimir la lista completa de compras en orden.

# Requisitos:

# El programa debe permitir al usuario ingresar productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa 
# de compras.

# lista = []

# while True:
#     compras = input("Ingrese un producto a la lista de compras: ")

#     lista.append(compras)

#     preguntar = input("¿Quiere agregar otro producto? (si/no): ").lower() #

#     if preguntar == "no":
#         break

# print("\n Tu lista de compras es:")

# for i in lista:
#     print(f"-{i}")

# lista = []

# while True:
#      entero = input("Ingrese un numero entero: ")

#      lista.append(entero)

#      preguntar = input("¿Quiere agregar otro numero? (si/no): ").lower() #

#      if preguntar == "no":
#          break

# print("\n La lista de numeros es: ")

# for i in lista:
#     print(f"-{i}")











