choras =float(input("Ingrese la cantidad de horas"))

horasCompletas = int(choras) + 1 if choras % 1 !=0 else int (choras)

tarifaHora = 1000

costoTotal = horasCompletas * tarifaHora
print(f"El costo total es: ${costoTotal} ")


