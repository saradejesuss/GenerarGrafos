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
import math
import numpy as np
import pygame

from pygame.locals import(
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


"""
Clase Grafo, contiene principalmente un conjunto de nodos y un conjunto de aristas
"""
class Grafo:

    def __init__(self):
        self.nombre = 'Graph'
        self.algoritmo = ""
        self.nodos = set()
        self.nodost = set()
        self.aristas = set(())
        # self.aristast = OrderedDict()
        self.dirigido = False
        self.auto = False
        self.discovered = list()
        self.layer = list()
        self.s = set(())
        self.ss = set(())
        self.q = OrderedDict()
        self.l = OrderedDict()

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
    Asignar el costo a una arista
    """
    def asignacostoarista(self, aristaid, cost):
        x = 0
        src = 0
        trg = 0
        for a in self.aristas:
            if a.id == aristaid:
                x = a
        if x:
            self.aristas.remove(x)
            x.cost = cost
            self.aristas.add(x)
            #print("costo=" + str(cost) + " agregado a " + aristaid)

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
            self.asignacostoarista(id, cost)
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
            nuevonodo = Nodo(nombre, 0, 0, 1)
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
    Mostrar el grafo en formato gv con distancias y costos (DIJKSTRA)
    """
    def muestragrafocostos(self):
        print("graph{")
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
    Crear el archivo GraphViz gv incluyendo  costos (Kruskal y Prim)
    """
    def archivogvCostos(self, nombrealgoritmo):
        f = open("" + nombrealgoritmo + str(len(self.nodos)) + ".gv", "w")
        f.write("graph{\r\n")
        for n in self.nodos:
            f.write("   " + str(n.id) + ";\r\n")
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
    Devuelve lista de nodos a partir de las aristas
    """
    def agreganodosdearista(self):
        self.muestranodos()
        for a in self.aristas:
            self.agreganodo(a.src,0,0,0)
            self.agreganodo(a.trg,0,0,0)
        self.muestranodos()

    """
    Calcular el árbol BFS del grafo a partir del nodo fuente s
    """
    def arbol_bfs(self, s):
        if not self.existenodo(s):
            print("no existe el nodo " + str(s))
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
        # for a in arbolbfs.aristas:
        #    print("aristas en arbolbfs=" + a.id)
        # print(len(arbolbfs.nodos))
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
                        # self.aristast[v] = arista
                        nu = Nodo(u)
                        nu.d = du
                        agregadou = arboldijkstra.agreganodon(nu)
                        nv = Nodo(v)
                        nv.d = du + l
                        agregadov = arboldijkstra.agreganodon(nv)
                        if len(self.s) > 1:
                            if (not agregadou and agregadov) or (not agregadov and agregadou):
                                #print("arista agregada" + a.id)
                                arboldijkstra.agregaaristacosto(u, v, l)
                            #else:
                                #print("arista no agregada" + a.id)
                        elif len(self.s) <= 1:
                            arboldijkstra.agregaaristacosto(u, v, l)
                            #print("arista agregada q<2" + a.id)
        return arboldijkstra

    """
    Calcular el árbol de expansión mínima mediante
    el Algoritmo de KRUSKAL Directo
    """
    def KruskalDir(self):
        arbolkruskal = Grafo()
        #Asignar costos aleatorios a las aristas
        for a in self.aristas:
            a.cost = random.randint(1, 5)
            self.q[a] = a.cost
        # Ordenar aristas por su peso en forma ascendente
        for key, _ in sorted(self.q.items(), key=lambda item: item[1]):
            self.q.move_to_end(key)
        # Componente conectado de cada nodo
        compcon = OrderedDict()
        for i in range(len(self.nodos)):
            compcon[i] = i
        # Para cada arista en la lista ordenada
        for a in self.q:
            u = int(a.src)
            v = int(a.trg)
            cost = a.cost
            cu = compcon[u]
            cv = compcon[v]
            # Si los nodos de la arista están en diferentes conjuntos:
            if cu != cv:
                # Combinar a los conjuntos que tienen a u y a v
                for c in compcon:
                    cc = compcon[c]
                    if cv == cc:
                        compcon[c] = cu
                compcon[v] = cu
                #print(compcon)
                # Agregar nodos y arista al árbol de Kruskal
                nu = Nodo(u, 0, 0, 1)
                nu.id = u
                nu.d = 1
                arbolkruskal.agreganodon(nu)
                nv = Nodo(u, 0, 0, 1)
                nv.id = v
                nv.d = 1
                arbolkruskal.agreganodon(nv)
                arbolkruskal.agregaaristacosto(u, v, cost)
            #else:
                #print(a.id + "no agregada")
        return arbolkruskal

    """
    Reiniciar q
    """
    def rstq(self):
        for i in self.q:
            self.q[i] = 0

    """
    Quitar una arista del grafo
    """
    def quitararista(self, aristaid):
        # print(len(self.aristas))
        x = 0
        # Para todas las aristas en el grafo encontrar la arista cuyo id sea el buscado
        for a in self.aristas:
            if a.id == aristaid:
                x = a
        # Si se encontró la arista, quitarla
        if x:
            self.aristas.remove(x)
        # print(len(self.aristas))

    """
    Calcular el árbol de expansión mínima mediante
    el Algoritmo de KRUSKAL Inverso
    """
    def KruskalInv(self):
        arbolkruskal = Grafo()
        self.rstq()
        #print(self.q.items())
        # Asignar costos aleatorios a las aristas
        for a in self.aristas:
            a.cost = random.randint(1, 5)
            self.q[a] = a.cost
            self.asignacostoarista(a.id, a.cost)
        # Copiar el grafo en el árbol de Kruskal
        arbolkruskal = self
        # Ordenar aristas por su peso en forma descendente
        for key, _ in sorted(self.q.items(), key=lambda item: item[1], reverse=True):
            self.q.move_to_end(key)
        # print(self.q.items())
        #Para todas las aristas en el árbol
        for a in self.q:
            # Quitar la arista a
            # print("quitar a.id=" + a.id + " " + str(len(arbolkruskal.aristas)))
            arbolkruskal.quitararista(a.id)
            # print("quitada a.id" + a.id + " " + str(len(arbolkruskal.aristas)))
            # Componente conectado de un nodo
            u = int(a.src)
            v = int(a.trg)
            bfsu = Grafo()
            # bfsv = Grafo()
            #Obtener el componente conectado de uno de los nodos
            bfsu = arbolkruskal.arbol_bfs(u)
            # bfsv = arbolkruskal.arbol_bfs(v)
            # bfsu.muestragrafocostos()
            # bfsu.muestragrafocostos()
            # print("u=" + str(u) + " len(bfsu.nodos)=" + str(len(bfsu.nodos)))
            # print("v=" + str(v) + " len(bfsv.nodos)=" + str(len(bfsv.nodos)))
            # print("nt=" + str(len(arbolkruskal.nodos)))
            # Si al quitar la arista el árbol queda desconectado (si hay menos nodos en el bfs que en el original)
            if len(bfsu.nodos) < len(arbolkruskal.nodos):
                # print("desconectado: nbfs=" + str(len(bfsu.nodos)) + " nt=" + str(len(arbolkruskal.nodos)) + " AGREGAR! a" + a.id)
                # No quitar la arista, volver a ponerla
                arbolkruskal.aristas.add(Arista(a.id, a.src, a.trg, a.cost))
        return arbolkruskal

    """
    Calcular el árbol de expansión mínima
    el Algoritmo de PRIM   
    """
    def Prim(self):
        arbolprim = Grafo()
        # Reiniciar las aristas ordenadas q, los nodos visitados s y las aristas agregadas av
        self.rstq()
        av = OrderedDict()
        arin = set(())
        # Asignar costos aleatorios a las aristas, asignarlo a la cola de prioridades
        for a in self.aristas:
            a.cost = random.randint(1, 5)
            self.q[a] = a.cost
            self.asignacostoarista(a.id, a.cost)
            av[a] = 10000
        # Asignar a los costos de las aristas visitadas un valor->infinito, para indicar que no han sido agregadas
        # Ordenar aristas por su peso en forma ascendente
        for key, _ in sorted(self.q.items(), key=lambda item: item[1]):
            self.q.move_to_end(key)
        while len(self.q) > 0:
            # Sacar el primer elemento de q
            item = (self.q.popitem(False))
            ar = item[0]
            x = item[1]
            u = ar.src
            v = ar.trg
            # Agregar las aristas incidentes del nuevo nodo
            if len(self.s) == 0:
                self.s.add(u)
                arin.update(self.aristasincidentes(u))
            # Para cada arista
            for e in av:
                v = self.nodoenarista(u, e)
                # Si el nodo adyacente no está en s y la arista es adyacente y no estaba
                if v not in self.s and e.cost < av[e] and e in arin:
                    # Agregar los nodos y la arista al árbol y agregar aristas incidentes
                    av[e] = e.cost
                    self.s.add(v)
                    self.s.add(u)
                    arin.update(self.aristasincidentes(u))
                    arin.update(self.aristasincidentes(v))
                    arbolprim.agreganodo(e.src)
                    arbolprim.agreganodo(e.trg)
                    arbolprim.agregaaristacosto(e.src, e.trg, e.cost)
        return arbolprim

    """
    Algoritmo Spring
    """
    def Spring(self):
        c1 = 2
        c2 = 1
        c3 = 1
        c4 = 0.1
        # Asignar posición aleatoria
        for n in self.nodos:
            n.x = random.randint(1, 800)
            n.y = random.randint(1, 600)
        # Establecer bandera de ejecución en Verdadero
        running = True
        # Inicializar pygamme
        pygame.init()
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption(self.algoritmo)
        # Crear un objeto Clock
        clock = pygame.time.Clock()
        # Ciclo de ejecución
        while running:
            clock.tick(15)
            # Cambiar la bandera de ejecución a Falso cuando se presione ESC o se cierre la ventana
            for event in pygame.event.get():
                if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT:
                    running = False
            # Rellenar la pantalla de color negro
            screen.fill([0, 0, 0])
            # Imprimir las líneas de todas las aristas del grafo
            for a in self.aristas:
                ns = self.obtenernodo(int(a.src))
                nt = self.obtenernodo(int(a.trg))
                pygame.draw.line(screen, [255, 30, 25], [ns.x, ns.y], [nt.x, nt.y], 2)
            # Imprimir los círculos de los nodos
            for n in self.nodos:
                pygame.draw.circle(screen, [30, 255, 25], [n.x, n.y], 5)
            # Desplegar lo que se trazó
            pygame.display.flip()
            # Calcular las fuerzas en x, y
            # Para cada nodo en el grafo se establecen las fuerzas en 0
            for u in self.nodos:
                Fx = 0
                Fy = 0
                # Obtener los nodos vecinos
                # Para cada arista incidente al nodo
                for a in self.aristasincidentes(u.id):
                    m = int(u.id)
                    # Obtener el nodo adyacente
                    v = self.obtenernodo(int(self.nodoenarista(u.id, a)))
                    # Calcular fuerza a sumar o restar
                    if v.x > u.x:
                        Fx += c1 * math.log(abs(v.x - u.x)/c2)
                    elif v.x < u.x:
                        Fx -= c1 * math.log(abs(v.x - u.x)/c2)
                    else:
                        Fx += c1
                    if v.y > u.y:
                        Fy += c1 * math.log(abs(v.y - u.y)/c2)
                    elif v.y < u.y:
                        Fy -= c1 * math.log(abs(v.y - u.y)/c2)
                    else:
                        Fy += c1
                # Si la fuerza no es 0 y la posición del nodo es mayor que 0, mover la posición del nodo con la fuerza
                if c4*Fx != 0 and u.x > 0:
                    u.x += int(np.around(c4 * Fx, 0))
                if c4*Fy != 0 and u.y > 0:
                    u.y += int(np.around(c4 * Fy, 0))
