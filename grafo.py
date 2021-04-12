"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""
from arista import Arista
from nodo import Nodo


class Grafo:

    def __init__(self):
        self.nombre = 'Graph'
        self.nodos = set(())
        self.aristas = set(())
        self.dirigido = False
        self.auto = False

    def existearista(self, nombre):
        for n in self.aristas:
            if n.id == nombre:
                return 1
        return 0

    def incrementagradoalnodo(self, id):
        for n in self.nodos:
            if id == int(n.id):
                n.grado += 1
                #print("grado de: " + str(id) + "=" + str(n.grado))
                return 1
        return 0

    def agregaarista(self, source, target):
        id = str(source) + " -- " + str(target)
        idx = id
        #Si no es dirigido comprueba que no exista la arista en ambos sentidos
        if self.dirigido == False:
            idx = str(target) + " -- " + str(source)
        if self.existearista(id) == 1 or self.existearista(idx) == 1:
            print(" ya existe arista " + id + " or " + idx )
            agregada = 0
        else:
            if self.existenodo(source) == 0 or self.existenodo(target) == 0:
                print(" no existe el nodo " + str(source) + " o el nodo " + str(target))
                agregada = 0
            else:
                nuevaarista = Arista(id, str(source), str(target))
                #print(nuevaarista.src + " -- " + nuevaarista.trg + ";")
                self.aristas.add(nuevaarista)
                agregada = 1
                self.incrementagradoalnodo(source)
                self.incrementagradoalnodo(target)
            #print("aristas: "  + str(self.aristas))
        return agregada

    def existenodo(self, name):
        for n in self.nodos:
            if n.id == name:
                return 1
        return 0

    def agreganodo(self, nombre):
        #print(nombre)
        if self.existenodo(nombre) == 1:
            #print("ya existe nodo " + str(nombre))
            agregado = 0
        else:
            nuevonodo = Nodo(nombre)
            self.nodos.add(nuevonodo)
            agregado = 1
            #print("nodo agregado " + str(nombre))
        #print("nodos: " + str(self.nodos))
        return agregado

    def obtenernodo(self, i, j):
        nombrenodo = i*j + j
        for n in self.nodos:
            if n.id == nombrenodo:
                return n

    def obtenernodo(self, i):
        for n in self.nodos:
            if n.id == i:
                return n

    def obtenerarista(self, idx):
        i=0
        for a in self.aristas:
           if i == idx:
               return a
           i += 1

    def muestranodos(self):
        print("   nodos{")
        for n in self.nodos:
            print("   " + str(n.id) + ",")
        print("   }")

    def muestraaristas(self):
        print("   aristas{")
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("   }")

    def muestragrafo(self):
        print(self.nombre + "{")
        self.muestranodos()
        self.muestraaristas()
        print("}")

    def muestragv(self):
        print("graph{")
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("}")

    def archivogv(self, nombrealgoritmo):
        f = open("" + nombrealgoritmo + str(len(self.nodos)) + ".gv", "w")
        f.write("graph{\r\n")
        for a in self.aristas:
            f.write("   " + str(a.id) + ";\r\n")
        f.write("}")

