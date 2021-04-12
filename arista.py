"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""

"""
Clase Arista, sus propiedades son id y vértices
"""


class Arista:

    def __init__(self, id, source, target):

        self.id = id
        self.src = source
        self.trg = target

    def __str__(self):

        return str(self.id)
