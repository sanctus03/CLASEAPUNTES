#   python tiene incluida una libreria de modulos con muchas utilidades para realizar distintas tareas
#   se llama standard library
#   el modulo os nos permite gestionar comandos del sistema operativo
#   math, statistics y datetime son librerias muy utiles en distintas ocasiones, el metodo para llamarlas es import + nombre de libreria
#   debugger: permite parar la ejecucion del codigo en determinados puntos del mismo ("breakpoints": los puntos rojos de la izquierda)
#             permite ejecutar paso a paso el código y ver el valor de las variables para localizar errores

"""demo numpy arrays"""

import numpy

a = numpy.array(    a: [[1 2], [3 4]]
    [[1, 2],
    [3,4]])
b = numpy.array(    b: [[5 6], [7 8]]
    [[5, 6],
     [7, 8]])
c = []  c: []
print("dimensiones a: ", a.ndim, "dimensiones b: ", b.ndim)
for row in a:
    print("row: ", row)
    c.append(row.tolist())