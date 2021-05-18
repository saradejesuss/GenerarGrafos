"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""

"""
Clase Nodo, sus propiedades son id, coordenadas y grado, principalmente
"""


class Nodo:

    def __init__(self, nombre, x=0.0, y=0.0, gr=0.0, d=10000):

        self.id = nombre
        self.x = x
        self.y = y
        self.grado = gr
        self.d = d

    def __str__(self):

        return self.id
