"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""

from grafo import Grafo
import random
import math


# Modelo Gm,n de malla. Crear m*n nodos. Para el nodo ni,j crear una arista con el nodo ni+1,j
# y otra con el nodo ni,j+1, para i<m y j<n
def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    g = Grafo()
    if m <= 1 or n <= 1 or m > 99 or n > 99:
        print("Solo valores mayores que 1 y menores que 100 para m y n")
        return 0
    print("Malla(" + str(m) + ", " + str(n) + ")")
    for i in range(m):
        for j in range(n):
            #nombrenodo = "\"" + str(i) + "," + str(j) + "\""
            nombrenodo = j * m + i
            g.agreganodo(nombrenodo)
    for i in range(m):
        for j in range(n):
            # nombrenodo = "\"" + str(i) + "," + str(j) + "\""
            nombrenodo = j * m + i
            if(i < m-1):
                #nombrenodosigi = "\"" + str(i+1) + "," + str(j) + "\""
                nombrenodosigi = j*m + i + 1
                g.agregaarista(nombrenodo, nombrenodosigi)
            if(j < n-1):
                #nombrenodosigj = "\"" + str(i) + "," + str(j+1) + "\""
                nombrenodosigj = (j+1)*m + i
                g.agregaarista(nombrenodo, nombrenodosigj)
    return g


# Modelo Gn,m de Erdös y Rényi. Crear n nodos y elegir uniformemente al azar
# m distintos pares de distintos vértices.
def grafoErdosRenyi(n, m, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    g = Grafo()
    if n <= 0 or m < n-1:
        print("Solo valores n>0 y m>=n-1")
        return 0
    print("ErdosRenyi(" + str(n) + "," + str(m) + ")")
    for i in range(n):
        g.agreganodo(i)
    i = 0
    while i < m:
        nodo1 = random.randrange(0, n)
        nodo2 = random.randrange(0, n)
        #print(str(i))
        agregada = 0
        if nodo1 != nodo2:
            agregada = g.agregaarista(nodo1, nodo2)
            if agregada == 0:
                i -= 1
            #print(str(i) + ": " + str(nodo1) + " -- " + str(nodo2) + " Agregado: " + str(agregada))
        else:
            #print(str(i) + ": " + str(nodo1) + " -- " + str(nodo2) + " Agregado: " + str(agregada))
            i -= 1
        i += 1
        #print(str(i))
    return g


# Modelo Gn,p de Gilbert. Crear n nodos y poner una arista entre cada par
# independiente y uniformemente con probabilidad p.
def grafoGilbert(n, p, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    g = Grafo()
    if n <= 0 or p<0 or p>1:
        print("Solo valores n>0 y 0<=p<=1")
        return 0
    print("Gilbert(" + str(n) + ", " + str(p) + ")")
    for nodo in range(n):
        g.agreganodo(nodo)
    for u in range(n):
        for v in range(n):
            if random.random() <= p and u != v:
                agregada = g.agregaarista(u, v)
            else:
                agregada = 0
            #print(str(u) + " -- " + str(v) + " agregada " + str(agregada))
    return g


def distancia(n1, n2):
    return math.sqrt((n2.x - n1.x)**2 + (n2.y - n1.y)**2)


# Modelo Gn,r geográfico simple. Colocar n nodos en un rectángulo unitario
# con coordenadas uniformes (o normales) y colocar una arista entre cada par
# que queda en distancia r o menor.
def grafoGeografico(n, r, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    g = Grafo()
    if n <= 0 or r < 0 or r > 1:
        print("Solo valores n>0 y 0<=r<=1")
        return 0
    print("GeograficoSimple(" + str(n) + "," + str(r) + ")")
    for i in range(n):
        if g.agreganodo(i) == 1:
            nodo = g.obtenernodo(i)
            nodo.x = random.random()
            nodo.y = random.random()
            #print(str(nodo.id) + " " + str(nodo.x) + "," + str(nodo.y))

    for i in range(n):
        for j in range(n):
            if i != j:
                d = distancia(g.obtenernodo(i), g.obtenernodo(j))
                #print("Distancia " + str(i) + "," + str(j) + ": " + str(d))
                if d <= r:
                    g.agregaarista(i, j)
    return g


# Variante del modelo Gn,d Barabási-Albert. Colocar n nodos uno por uno,
# asignando a cada uno d aristas a vértices distintos de tal manera que
# la probabilidad de que el vértice nuevo se conecte a un vértice existente
# v es proporcional a la cantidad de aristas que v tiene actualmente -
# los primeros d vértices se conecta todos a todos.
def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :param auto: permitir auto-ciclos?
    :return: grafo generado
    """
    g = Grafo()
    if n<=0 or d<=1:
        print("Solo valores n>0 y d>1")
        return 0
    print("BarabasiAlbert(" + str(n) + ", " + str(d) + ")")
    for i in range(n):
        j = 0
        g.agreganodo(i)
        #print(str(i) + "agregado")
        if i >= d:
            di = 0
            while di < d:
                for j in range(i):
                    k = g.obtenernodo(j)
                    #print("j=" + str(k.id) + ": p=" + str(k.grado) + "/" + str(len(g.aristas) * 2) )
                    p = k.grado / (len(g.aristas) * 2)
                    r = random.random()
                    #print(str(r) + " <= " + str(p) + "?")
                    if r <= p:
                        if g.agregaarista(i, j) == 1:
                            di += 1
                            #print(str(di) + "=di aristas agregadas a i=" + str(i))
                    if di == d:
                        break
        else:
            if i > 0:
                for j in range(i):
                    #print("i:" + str(i) + ">0  < d=" + str(d) + " j=" + str(j))
                    g.agregaarista(i, j)
                    m = g.obtenernodo(i)
                    o = g.obtenernodo(j)
                    #print("grado i=" + str(m.grado) + " grado j=" + str(o.grado))
            #else:
                #print("sin arista i=" + str(i) + "<=0 or i<d=" + str(d) + " j=" + str(j))
    return g


# Modelo Gn Dorogovtsev-Mendes. Crear 3 nodos y 3 aristas formando un triángulo.
# Después, para cada nodo adicional, se selecciona una arista al azar y se crean aristas
# entre el nodo nuevo y los extremos de la arista seleccionada.
def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    g = Grafo()
    if n < 3:
        print("Solo valores n>=3")
        return 0
    print("DorogovtsevMendes(" + str(n) + ")")
    for i in range(3):
        g.agreganodo(i)
    g.agregaarista(0, 1)
    g.agregaarista(0, 2)
    g.agregaarista(1, 2)
    for i in range(3, n):
        g.agreganodo(i)
        idx = random.randrange(0, i)
        a = g.obtenerarista(idx)
        g.agregaarista(i, int(a.src))
        g.agregaarista(i, int(a.trg))
    return g





