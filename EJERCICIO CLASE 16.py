#   escribir un archivo llamado palabras.txt que tiene una palabra en cada linea
#   escribir otro archivo llamado frases.txt que tine una frase en cada linea
#   desarrollar un codigo python que localiza cuantas veces aparece cada palabra de la lista que esta en el archivo
#   palabras.txt, en las frases de la lista de frases que esta en el archivo frases.txt
#   el resultado ha de ser: un diccionario con un campo por cada palabra. el valor de cada campo del diccionario ha de
#   ser una lista, en la que cada elemento es el numero de veces que aparace la palabra en la frase correspondiente:
#   en la posicion 0 de la lista cuantas veces aparece la palabra en la priemra frase y asi sucesivamente
#   escribir el resultado por pantalla

"""cuenta de palabras en frases"""

PALABRAS = "palabras.txt"
FRASES = "frases.txt"

archivo = open(PALABRAS, "r")

palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []
print("lista de palabras: \n", palabras)

archivo = open(FRASES, "r")
frases = []
for frase in archivo:
    frases.append(frase.strip())
    for palabra in palabras:
        palabras[palabra].append (frase().count(palabra))
archivo.close()
print("frases: \n", frases)
print("palabras en frases: \n", palabras)
