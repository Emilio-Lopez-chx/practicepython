#Que es un diccionario de datos?

#Lista

# lista = ["juan","maria","carlos"]

# diccionario = {
#     "nombre": "Diego", 
#     "edad":25, 
#     "profesion":"profesor"
#     }

# productos = {
#     "televisor":15.000,
#     "celular":  30.000,
#     "portatil": 160.000
# }


# nombres = {"nombre": "carlos", "edad": 20, "cursos": ["Python", "Javascript","Nodejs" ]}
# print (nombres)

# print (nombres["cursos"])
# print (nombres["cursos"][1])

# notas_estudiantes = {
#     "Juan":[2.5, 3, 4.6],
#     "Ana": [3.5, 4.6, 4.9],
#     "Luis": [4, 2.5, 3.9]
# }

#print(notas_estudiantes["juan"])
#--------------Agregar datos aun diccionario-----

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30
#     }

# miDiccionario["profesion"] = "instructora"

# print(miDiccionario)

#------------------Editar datos a un diccionario-----------
# miDiccionario["edad"] = 31

# print(miDiccionario)

#------------------Eliminar datos a un diccionario-----------

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30,
#     "profesion": "instructora"
#     }

# print(miDiccionario)

# # del miDiccionario ["profesion"]
# # print(miDiccionario)

# prof = miDiccionario.pop("profesion")

# print(prof)
# print(miDiccionario)

#------------------Agregar multiples valores-------------------

miDiccionario = {
     "nombre": "Sara", 
     "edad": 30,
     "profesion": "instructora"
     }

nuevosDatos = {
    "ciudad": "Cali",
    "dni":  3455475,
    "telefono": "5654654"

}

print(nuevosDatos)

for clave, valor in nuevosDatos.items():
    miDiccionario[clave] = valor

print(miDiccionario)    