"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""
from arista import Arista
from nodo import Nodo


"""
Clase Grafo, contiene principalmente un conjunto de nodos y un conjunto de aristas
"""


class Grafo:

    def __init__(self):
        self.nombre = 'Graph'
        self.nodos = set(())
        self.aristas = set(())
        self.dirigido = False
        self.auto = False

    """
    Verificar que exista la arista con cierto nombre
    """
    def existearista(self, nombre):
        for n in self.aristas:
            if n.id == nombre:
                return 1
        return 0

    """
    Incrementar en 1 el grado de un nodo
    """
    def incrementagradoalnodo(self, id):
        for n in self.nodos:
            if id == int(n.id):
                n.grado += 1
                return 1
        return 0

    """
    Agregar una arista entre dos nodos
    """
    def agregaarista(self, source, target):
        id = str(source) + " -- " + str(target)
        idx = id
        # Si no es dirigido comprobar que no existe la arista en ambos sentidos
        if not self.dirigido:
            idx = str(target) + " -- " + str(source)
        if self.existearista(id) == 1 or self.existearista(idx) == 1:
            # print(" ya existe arista " + id + " or " + idx)
            agregada = 0
        else:
            # Si no existe la arista, verificar que sí existen los nodos
            if self.existenodo(source) == 0 or self.existenodo(target) == 0:
                # print(" no existe el nodo " + str(source) + " o el nodo " + str(target))
                agregada = 0
            else:
                # Crear la arista y agregarla al conjunto de aristas del grafo
                nuevaarista = Arista(id, str(source), str(target))
                self.aristas.add(nuevaarista)
                agregada = 1
                # Incrementar el grado de los vértices de la arista
                self.incrementagradoalnodo(source)
                self.incrementagradoalnodo(target)
        # Devolver si la arista fue o no agregada
        return agregada

    """
    Verificar que existe el nodo
    """
    def existenodo(self, name):
        for n in self.nodos:
            if n.id == name:
                return 1
        return 0

    """
    Agregar un nodo al grafo
    """
    def agreganodo(self, nombre):
        # Verificar que no se duplique el nodo
        if self.existenodo(nombre) == 1:
            agregado = 0
        else:
            # Crear un nuevo nodo y agregarlo al conjunto de nodos del grafo
            nuevonodo = Nodo(nombre)
            self.nodos.add(nuevonodo)
            agregado = 1
        # Regresar si el nodo fue agregado o no
        return agregado

    """
    Obtener el nodo, según su fila y columna
    """
    def obtenernodo(self, i, j):
        nombrenodo = i*j + j
        for n in self.nodos:
            if n.id == nombrenodo:
                return n
    """
    Obtener un nodo por su id
    """
    def obtenernodo(self, i):
        for n in self.nodos:
            if n.id == i:
                return n

    """
    Obtener una arista por su id
    """
    def obtenerarista(self, idx):
        i = 0
        for a in self.aristas:
            if i == idx:
                return a
            i += 1

    """
    Mostrar el conjunto de nodos del grafo
    """
    def muestranodos(self):
        print("   nodos{")
        for n in self.nodos:
            print("   " + str(n.id) + ",")
        print("   }")

    """
    Mostrar los nodos con sus posiciones: 
    nodo0 [pos="x,y"]... nodon [pos="x,y"];
    """
    def muestranodospos(self):
        for n in self.nodos:
            print("   " + str(n.id) + " [pos=\"" + str(n.x) + ", " + str(n.y) + "\",];")

    """
    Mostrar el conjunto de aristas del grafo
    """
    def muestraaristas(self):
        print("   aristas{")
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("   }")

    """
    Mostrar el grafo: Nombre { nodos {} aristas {} }
    """
    def muestragrafo(self):
        print(self.nombre + "{")
        self.muestranodos()
        self.muestraaristas()
        print("}")

    """
    Mostrar el formato gv: graph { arista0; ... aristan; }
    """
    def muestragv(self):
        print("graph{")
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("}")

    """
    Mostrar el formato gv con nodos x,y: graph { nodo0 [pos="x,y",];...arista0; ... aristan; }
    """
    def muestragvpos(self):
        print("graph{")
        self.muestranodospos()
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("}")

    """
    Crear el archivo GraphViz gv
    """
    def archivogv(self, nombrealgoritmo):
        f = open("" + nombrealgoritmo + str(len(self.nodos)) + ".gv", "w")
        f.write("graph{\r\n")
        for a in self.aristas:
            f.write("   " + str(a.id) + ";\r\n")
        f.write("}")

    """
    Crear el archivo GraphViz gv incluyendo posiciones de los nodos
    """
    def archivogvpos(self, nombrealgoritmo):
        f = open("" + nombrealgoritmo + str(len(self.nodos)) + ".gv", "w")
        f.write("graph{\r\n")
        for n in self.nodos:
            f.write("   " + str(n.id) + " [pos=\"" + str(n.x * 1000) + ", " + str(n.y * 1000) + "\",];\r\n")
        for a in self.aristas:
            f.write("   " + str(a.id) + ";\r\n")
        f.write("}")
