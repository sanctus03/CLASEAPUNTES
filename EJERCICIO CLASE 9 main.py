import json

lista_coche = []

while True:
    marcacoche = input("marca coche: ")
    if marcacoche == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("tipo combustible: ")
    cilindrada = input("cilindrada: ")
    linea= {}
    linea["marca coche: "] = marcacoche
    linea["modelo: "] = modelo
    linea["combustible: "] = combustible
    linea["cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("Lista coche:\n", lista_coche)

json.dump(json.dumps(lista_coche), open("coches.txt", "w"))

lista_coches = []