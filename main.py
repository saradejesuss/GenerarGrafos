"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Abril 2021
"""

import algoritmos

"""
Programa principal, desde donde se ejecutan las funciones 
para generar grafos mediante los distintos modelos.
"""

if __name__ == '__main__':

    # Grafo con el modelo de Malla para 30, 100 y 500 nodos
    gM = algoritmos.grafoMalla(6, 5)
    gM.muestragv()
    #gM.archivogv("Malla")
    gM = algoritmos.grafoMalla(10, 10)
    gM.muestragv()
    #gM.archivogv("Malla")
    gM = algoritmos.grafoMalla(25, 20)
    gM.muestragv()
    #gM.archivogv("Malla")

    # Grafo con el modelo de Erdos y Renyi para 30, 100 y 500 nodos
    gE = algoritmos.grafoErdosRenyi(30, 40)
    gE.muestragv()
    #gE.archivogv("ErdosRenyi")
    gE = algoritmos.grafoErdosRenyi(100, 150)
    gE.muestragv()
    #gE.archivogv("ErdosRenyi")
    gE = algoritmos.grafoErdosRenyi(500, 700)
    gE.muestragv()
    #gE.archivogv("ErdosRenyi")
    
    # Grafo con el modelo de Gilbert para 30, 100 y 500 nodos
    gG = algoritmos.grafoGilbert(30, 0.5)
    gG.muestragv()
    #gG.archivogv("Gilbert")
    gG = algoritmos.grafoGilbert(100, 0.2)
    gG.muestragv()
    #gG.archivogv("Gilbert")
    gG = algoritmos.grafoGilbert(500, 0.01)
    gG.muestragv()
    #gG.archivogv("Gilbert")

    # Grafo con el modelo Geográfico simple para 30, 100 y 500 nodos
    gS = algoritmos.grafoGeografico(30, 0.5)
    gS.muestragvpos()
    #gS.archivogvpos("GeograficoSimple")
    gS = algoritmos.grafoGeografico(100, 0.2)
    gS.muestragvpos()
    #gS.archivogvpos("GeograficoSimple")
    gS = algoritmos.grafoGeografico(500, 0.1)
    gS.muestragvpos()
    #gS.archivogvpos("GeograficoSimple")

    # Grafo con el modelo Barabasi-Albert para 30, 100 y 500 nodos
    gB = algoritmos.grafoBarabasiAlbert(30, 2)
    gB.muestragv()
    #gB.archivogv("BarabasiAlbert")
    gB = algoritmos.grafoBarabasiAlbert(100, 2)
    gB.muestragv()
    #gB.archivogv("BarabasiAlbert")
    gB = algoritmos.grafoBarabasiAlbert(500, 2)
    gB.muestragv()
    #gB.archivogv("BarabasiAlbert")

    # Grafo con el modelo Dorogovtsev-Mendes para 30, 100 y 500 nodos
    gD = algoritmos.grafoDorogovtsevMendes(30)
    gD.muestragv()
    #gD.archivogv("DorogovtsevMendes")
    gD = algoritmos.grafoDorogovtsevMendes(100)
    gD.muestragv()
    #gD.archivogv("DorogovtsevMendes")
    gD = algoritmos.grafoDorogovtsevMendes(500)
    gD.muestragv()
    #gD.archivogv("DorogovtsevMendes")


