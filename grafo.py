"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""

from collections import OrderedDict
from arista import Arista
from nodo import Nodo
import random


"""
Clase Grafo, contiene principalmente un conjunto de nodos y un conjunto de aristas
"""
class Grafo:

    def __init__(self):
        self.nombre = 'Graph'
        self.nodos = set()
        self.nodost = set()
        self.aristas = set(())
        self.aristast = OrderedDict()
        self.dirigido = False
        self.auto = False
        self.discovered = list()
        self.layer = list()
        self.s = set()
        self.ss = set()
        self.q = OrderedDict()

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
    Agregar una arista entre dos nodos, para agregarla deben existir ambos nodos.
    Si no es dirigido, comprobar que no exista la arista en uno u otro sentido
    """
    def agregaarista(self, source, target):
        id = str(source) + " -- " + str(target)
        idx = id
        # Si no es dirigido comprobar que no existe la arista en uno u otro sentidos
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
    Agregar una arista entre dos nodos, para agregarla deben existir ambos nodos.
    Si no es dirigido, comprobar que no exista la arista en uno u otro sentido
    """
    def agregaaristacosto(self, source, target, cost):
        id = str(source) + " -- " + str(target)
        idx = id
        # Si no es dirigido comprobar que no existe la arista en uno u otro sentidos
        if not self.dirigido:
            idx = str(target) + " -- " + str(source)
        if self.existearista(id) == 1 or self.existearista(idx) == 1:
            #print(" ya existe arista " + id + " or " + idx)
            agregada = 0
        else:
            # Si no existe la arista, verificar que sí existen los nodos
            if self.existenodo(source) == 0 or self.existenodo(target) == 0:
                # print(" no existe el nodo " + str(source) + " o el nodo " + str(target))
                agregada = 0
            else:
                # Crear la arista y agregarla al conjunto de aristas del grafo
                nuevaarista = Arista(id, str(source), str(target), str(cost))
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
    Agregar un nodo con un nombre al grafo
    """
    def agreganodo(self, nombre):
        # Verificar que no se duplique el nodo
        if self.existenodo(nombre) == 1:
            agregado = 0
        else:
            # Crear un nuevo nodo y agregarlo al conjunto de nodos del grafo
            nuevonodo = Nodo(nombre)
            # nuevonodo.atrib.ATTR_ESTILO.ESTILO_Color = (1, 1, 1)
            self.nodos.add(nuevonodo)
            agregado = 1
        # Regresar si el nodo fue agregado o no
        return agregado

    """
    Agregar un nodo de la clase Nodo al grafo 
    """
    def agreganodon(self, nodo):
        # Verificar que no se duplique el nodo
        if self.existenodo(nodo.id) == 1:
            agregado = 0
        else:
            # Crear un nuevo nodo y agregarlo al conjunto de nodos del grafo
            # nuevonodo = Nodo(nombre)
            # nuevonodo.atrib.ATTR_ESTILO.ESTILO_Color = (1, 1, 1)
            self.nodos.add(nodo)
            agregado = 1
        # Regresar si el nodo fue agregado o no
        return agregado

    """
    Obtener el nodo, según su fila y columna
    
    def obtenernodo(self, i, j):
        nombrenodo = i*j + j
        for n in self.nodos:
            if n.id == nombrenodo:
                return n
    """
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
    Verifica si el nodo está en la arista.
    Devuelve el otro nodo de la arista o -1 si la arista no contiene al nodo.
    """
    def nodoenarista(self, nodo, arista):
        if arista.src == str(nodo):
            return arista.trg
        elif arista.trg == str(nodo):
            return arista.src
        else:
            return -1

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
    Mostrar los nodos con sus distancias (DIJKSTRA): 
    nodo0 [label="nodo0(2)"]... nodon [label="nodon(17)"];
    """
    def muestranodosdis(self):
        for n in self.nodos:
            print("   " + str(n.id) + " [label=\"" + str(n.id) + "(" + str(n.d) + ")\"];")

    """
    Mostrar el conjunto de aristas del grafo
    """
    def muestraaristas(self):
        print("   aristas{")
        for a in self.aristas:
            print("   " + str(a.id) + ";")
        print("   }")

    """
    Mostrar el conjunto de aristas del grafo con su costo
    """
    def muestraaristascosto(self):
        #print("   aristas{")
        for aa in self.aristas:
            print("   " + str(aa.id) + " [label=\"" + str(aa.cost) + "\"];")
        #print("   }")

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
    Mostrar el grafo en formato gv con distancias y costos (DIJKSTRA)
    """
    def muestragrafodijkstra(self):
        print("graph{")
        self.muestranodosdis()
        self.muestraaristascosto()
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

    """
    Crear el archivo GraphViz gv incluyendo distancias y costos (DIJKSTRA)
    """
    def archivogvdijkstra(self, nombrealgoritmo):
        f = open("" + nombrealgoritmo + str(len(self.nodos)) + ".gv", "w")
        f.write("graph{\r\n")
        for n in self.nodos:
            f.write("   " + str(n.id) + " [label=\"" + str(n.id) + "(" + str(n.d) + ")\"];\r\n")
        for a in self.aristas:
            f.write("   " + str(a.id) + " [label=\"" + str(a.cost) + "\"];\r\n")
        f.write("}")

    """
    Obtener todas las aristas incidentes al nodo n
    """
    def aristasincidentes(self, n):
        aristasi = []
        for a in self.aristas:
            if int(a.src) == int(n) or int(a.trg) == int(n):
                aristasi.append(a)
        return aristasi

    """
    Limpiar la lista de nodos descubiertos y la lista de capas del árbol.
    Marcar al nodo fuente como descubierto y todos los demás como no descubiertos.
    """
    def rstarbol(self, s):
        self.discovered.clear()
        self.layer.clear()
        for v in range(len(self.nodos)):
            self.discovered.append(False)
        if self.existenodo(s):
            self.discovered[s] = True

    """
    Calcular el árbol BFS del grafo a partir del nodo fuente s
    """
    def arbol_bfs(self, s):
        if not self.existenodo(s):
            return 0
        # Reiniciar el árbol, marcando el nodo fuente s como descubierto y los demás como no descubiertos
        self.rstarbol(s)
        # i indica el índice de la capa
        i = 0
        # Agregar el nodo fuente s a la lista de capas
        self.layer.append([s])
        # Crear el arbolbfs y agregar el nodo fuente
        arbolbfs = Grafo()
        arbolbfs.agreganodo(s)
        tamlayer = len(self.layer[i])
        # Mientras la capa i no esté vacía
        while 0 < tamlayer:
            agregado = 0
            # Para cada nodo n en la capa i, buscar las aristas n-m incidente
            for n in self.layer[i]:
                aristasi = self.aristasincidentes(n)
                m = int(n)
                # Para cada nodo incidente verificar si no ha sido descubierto.
                for ai in aristasi:
                    if int(n) == int(ai.trg):
                        m = int(ai.src)
                    elif int(n) == int(ai.src):
                        m = int(ai.trg)
                    # Si el nodo incidente no ha sido descubierto, marcarlo, agregar el nodo y la arista a la capa
                    if not self.discovered[m]:
                        self.discovered[m] = True
                        if agregado == 0:
                            self.layer.append([m])
                        else:
                            self.layer[i+1].append(m)
                        arbolbfs.agreganodo(m)
                        arbolbfs.agregaarista(n, m)
                        agregado += 1
            # Si al menos se agregó un nodo a la capa siguiente, continuar el ciclo de búsqueda, de lo contrario terminar
            if agregado > 0:
                i += 1
                tamlayer = len(self.layer[i])
            else:
                tamlayer = 0
        # Devolver el árbol BFS calculado
        return arbolbfs

    """
    Función recursiva para calcular el árbol DFS
    """
    def funcionrec(self, arboldfsr, u):
        # Marcar el nodo como descubierto
        self.discovered[int(u)] = True
        # Obtener las aristas incidentes al nodo u
        aristasi = self.aristasincidentes(int(u))
        # Para cada arista incidenta a u, obtener el nodo vecino
        for a in aristasi:
            v = u
            if u == int(a.src):
                v = a.trg
            elif u == int(a.trg):
                v = a.src
            # Si el nodo vecino no ha sido descubierto, marcarlo, agregar el nodo y la arista al árbol y repetir
            if not self.discovered[int(v)]:
                arboldfsr.agreganodo(int(v))
                arboldfsr.agregaarista(int(u), int(v))
                # Llamar a la misma función en forma recursiva, para el nodo vecino v
                self.funcionrec(arboldfsr, int(v))

    """
    Calcular el árbol DFS del grafo, mediante una función RECURSIVA, a partir del nodo fuente s
    """
    def arbol_dfs_r(self, s):
        # Reiniciar el árbol DFSr, marcando el nodo fuente s como descubierto y los demás como no descubiertos
        self.rstarbol(s)
        # Crear el árbol DFS recursivo y agregar el nodo fuente
        arboldfsr = Grafo()
        arboldfsr.agreganodo(int(s))
        # Llamar a la función recursiva para calcular el árbol DFS a partir del nodo fuente s
        self.funcionrec(arboldfsr, int(s))
        # Devolver el árbol DFS calculado
        return arboldfsr

    """
    Calcular el árbol DFS del grafo, mediante una función ITERATIVA, a partir del nodo fuente s
    """
    def arbol_dfs_i(self, s):
        if not self.existenodo(s):
            return 0
        # Reiniciar el árbol, marcando el nodo fuente s como descubierto y los demás como no descubiertos
        self.rstarbol(s)
        # Crear el árbol DFS iterativo, la pila y la lista de aristas incidentes.
        arboldfsi = Grafo()
        stack = []
        aristasi = list
        # Agregar el nodo fuente al árbol DFS iterativo
        arboldfsi.agreganodo(s)
        # Agregar las aristas incidentes al nodo fuente a la pila
        aristasi = self.aristasincidentes(s)
        stack.extend(aristasi)
        # Mientras la pila no esté vacía, sacar el último elemento
        while len(stack) > 0:
            a = stack.pop()
            # Si el nodo vecino no ha sido descubierto, marcarlo, agregarlo al árbol y buscar sus aristas incidentes.
            aristasi = []
            if not self.discovered[int(a.trg)]:
                self.discovered[int(a.trg)] = True
                arboldfsi.agreganodo(int(a.trg))
                aristasi = self.aristasincidentes(a.trg)
            elif not self.discovered[int(a.src)]:
                self.discovered[int(a.src)] = True
                arboldfsi.agreganodo(int(a.src))
                aristasi = self.aristasincidentes(a.src)
            # Si el nodo vecino ya ha sido descubierto no hacer nada, continuar el ciclo
            else:
                continue
            # Agregar la arista al árbol y agregar a la pila todas las aristas incidentes.
            arboldfsi.agregaarista(int(a.src), int(a.trg))
            stack.extend(aristasi)
        # Devolver el árbol DFS calculado
        return arboldfsi

    """
    Calcular el camino más corto mediante
    el Algoritmo de DIJKSTRA   
    """
    def Dijkstra(self, s):
        arboldijkstra = Grafo()
        # Agrega a q los nodos n con prioridad dn=infinito (muy alta)
        for n in self.nodos:
            self.q[n.id] = 1000000
        # Actualizar en q al nodo s con prioridad ds=0
        self.q[s] = 0
        # Ordenar q
        for key, _ in sorted(self.q.items(), key=lambda item: item[1]):
            self.q.move_to_end(key)
        v = 0
        # Mientras q no esté vacía
        while len(self.q) > 0:
            # Sacar el primer elemento de q, u es el nodo, du es la prioridad
            item = (self.q.popitem(False))
            u = item[0]
            du = item[1]
            # Agregar a s el nodo u
            su = str(u) + "[" + str(du) + "]"
            self.ss.add(su)  # ss tiene nodos con distancia
            self.s.add(u)    # s tiene solo el nodo
            # Para cada arista u - v saliente de u
            for a in self.aristasincidentes(u):
                l = random.randint(1, 5)     # distancia aleatoria
                v = int(self.nodoenarista(u, a))
                # Si v no pertenece a s
                if v not in self.s:
                    dv = int(self.q[v])
                    # Si dv > du + l
                    if dv > (du + l):
                        # Actualizar en q al nodo v con prioridad dv=du+l
                        self.q[v] = (du + l)
                        # Ordenar q
                        for key, _ in sorted(self.q.items(), key=lambda item: item[1]):
                            self.q.move_to_end(key)
                        arista = Arista(a.id, u, v, du+l)
                        self.aristast[v] = arista
                        nu = Nodo(u)
                        nu.d = du
                        agregadou = arboldijkstra.agreganodon(nu)
                        nv = Nodo(v)
                        nv.d = du + l
                        agregadov = arboldijkstra.agreganodon(nv)
                        if len(self.s) > 1:
                            if (not agregadou and agregadov) or (not agregadov and agregadou):
                                print("arista agregada" + a.id)
                                arboldijkstra.agregaaristacosto(u, v, l)
                            else:
                                print("arista no agregada" + a.id)
                        elif len(self.s) <= 1:
                            arboldijkstra.agregaaristacosto(u, v, l)
                            print("arista agregada q<2" + a.id)
        return arboldijkstra