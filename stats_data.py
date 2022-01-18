"""clase para definir datos estadisticos de una lista"""

import statistics

class StatsData:

    def __init__(self, lista):
        self.l_data = lista
        self.media = statistics.mean(lista)
        self.mediana = statistics.median(lista)
        self.varianza = statistics.variance(lista)