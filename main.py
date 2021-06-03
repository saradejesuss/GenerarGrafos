"""
CIC - IPN
Análisis y diseño de Algoritmos - Dr. Rolando Quintero

Sara De Jesús Sánchez
Mayo 2021
"""

import algoritmos

"""
Programa principal, desde donde se ejecutan las funciones 
para generar grafos mediante los distintos modelos.
"""

if __name__ == '__main__':

    # Grafo con el modelo de Malla para 30 nodos, con cálculo de BFS, DFSr, DFSi, Dijkstra
    gM = algoritmos.grafoMalla(6, 5)
    gM.muestragv()
    """
    gM.archivogv("Malla30")
    gBFS = gM.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Malla30")
    gDFSr = gM.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSR_Malla30")
    gDFSi = gM.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSI_Malla30")
    
    gDjk = gM.Dijkstra(0)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Malla30")
    """
    gKrk = gM.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Malla30")
    gKrk = gM.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskalI_Malla30")
    gPrm = gM.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Malla30")

    # Grafo con el modelo de Malla para 100 nodos, con cálculo de BFS, DFSr y DFSi
    #gM = algoritmos.grafoMalla(10, 10)
    #gM.muestragv()
    """
    gM.archivogv("Malla100")
    gBFS = gM.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Malla100")
    gDFSr = gM.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSR_Malla100")
    gDFSi = gM.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_Malla100")
    """
    # Grafo con el modelo de Malla para 500 nodos, con cálculo de BFS, DFSr y DFSi
    # gM = algoritmos.grafoMalla(25, 20)
    # gM.muestragv()
    """
    gM.archivogv("Malla500")
    gBFS = gM.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Malla500")
    gDFSr = gM.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSR_Malla500")
    gDFSi = gM.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_Malla500")
    """
    # Grafo con el modelo de Erdos y Renyi para 30 nodos y cálculo de BFS, DFSr y DFSi
    gE = algoritmos.grafoErdosRenyi(30, 40)
    gE.muestragv()
    """
    gE.archivogv("ErdosRenyi30")
    gBFS = gE.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_ErdosRenyi30")
    gDFSr = gE.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_ErdosRenyi30")
    gDFSi = gE.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_ErdosRenyi30")
    gDjk = gE.Dijkstra(1)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Erdos30")
    """
    gKrk = gE.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Erdos30")
    gKrk = gE.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskalI_Erdos30")
    gPrm = gE.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Erdos30")
    # Grafo con el modelo de Erdos y Renyi para 100 nodos y cálculo de BFS, DFSr y DFSi
    # gE = algoritmos.grafoErdosRenyi(100, 150)
    # gE.muestragv()
    """
    gE.archivogv("ErdosRenyi100")
    gBFS = gE.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_ErdosRenyi100")
    gDFSr = gE.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_ErdosRenyi100")
    gDFSi = gE.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_ErdosRenyi100")
    """
    # Grafo con el modelo de Erdos y Renyi para 500 nodos y cálculo de BFS, DFSr y DFSi
    # gE = algoritmos.grafoErdosRenyi(500, 700)
    # gE.muestragv()
    """
    gE.archivogv("ErdosRenyi500")
    gBFS = gE.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_ErdosRenyi500")
    gDFSr = gE.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_ErdosRenyi500")
    gDFSi = gE.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_ErdosRenyi500")
    """
    # Grafo con el modelo de Gilbert para 30 nodos y cálculo de BFS, DFSr y DFSi
    gG = algoritmos.grafoGilbert(30, 0.5)
    gG.muestragrafocostos()
    """
    gG.archivogv("Gilbert30")
    gBFS = gG.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Gilbert30")
    gDFSr = gG.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_Gilbert30")
    gDFSi = gG.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_Gilbert30")
    gDjk = gG.Dijkstra(1)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Gilbert30")
    """
    gKrk = gG.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Gilber30")
    gKrk = gG.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskalI_Gilber30")
    gPrm = gG.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Gilbert30")
    # Grafo con el modelo de Gilbert para 100 nodos y cálculo de BFS, DFSr y DFSi
    # gG = algoritmos.grafoGilbert(100, 0.2)
    # gG.muestragv()
    """
    gG.archivogv("Gilbert100")
    gBFS = gG.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Gilbert100")
    gDFSr = gG.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_Gilbert100")
    gDFSi = gG.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_Gilbert100")
    """

    # Grafo con el modelo de Gilbert para 500 nodos y cálculo de BFS, DFSr y DFSi
    # gG = algoritmos.grafoGilbert(500, 0.01)
    # gG.muestragv()
    """
    gG.archivogv("Gilbert500")
    gBFS = gG.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_Gilbert500")
    gDFSr = gG.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_Gilbert500")
    gDFSi = gG.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_Gilbert500")
    """
    # Grafo con el modelo Geográfico simple para 30 nodos y cálculo de BFS, DFSr y DFSi
    gS = algoritmos.grafoGeografico(30, 0.5)
    gS.muestragvpos()
    """
    gS.archivogvpos("GeograficoSimple30")
    gBFS = gS.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_GeograficoSimple30")
    gDFSr = gS.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_GeograficoSimple30")
    gDFSi = gS.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_GeograficoSimple30")
    gDjk = gS.Dijkstra(1)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Geo30")
    """
    gKrk = gS.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Geo30")
    gKrk = gS.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskalI_Geo30")
    gPrm = gS.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Geo30")
    # Grafo con el modelo Geográfico simple para 100 nodos y cálculo de BFS, DFSr y DFSi
    # gS = algoritmos.grafoGeografico(100, 0.2)
    # gS.muestragvpos()
    """
    gS.archivogvpos("GeograficoSimple100")
    gBFS = gS.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_GeograficoSimple100")
    gDFSr = gS.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_GeograficoSimple100")
    gDFSi = gS.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_GeograficoSimple100")
    """
    # Grafo con el modelo Geográfico simple para 500 nodos y cálculo de BFS, DFSr y DFSi
    # gS = algoritmos.grafoGeografico(500, 0.1)
    # gS.muestragvpos()
    """
    gS.archivogvpos("GeograficoSimple500")
    gBFS = gS.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_GeograficoSimple500")
    gDFSr = gS.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_GeograficoSimple500")
    gDFSi = gS.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_GeograficoSimple500")
    """
    # Grafo con el modelo Barabasi-Albert para 30 nodos y cálculo de BFS, DFSr y DFSi
    gB = algoritmos.grafoBarabasiAlbert(30, 2)
    gB.muestragv()
    """
    gB.archivogv("BarabasiAlbert30")
    gBFS = gB.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_BarabasiAlbert30")
    gDFSr = gB.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_BarabasiAlbert30")
    gDFSi = gB.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_BarabasiAlbert30")
    gDjk = gB.Dijkstra(1)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Barabasi30")
    """
    gKrk = gB.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Barabasi30")
    gKrk = gB.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskalI_Barabasi30")
    gPrm = gB.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Barabasi30")
    # Grafo con el modelo Barabasi-Albert para 100 nodos y cálculo de BFS, DFSr y DFSi
    # gB = algoritmos.grafoBarabasiAlbert(100, 2)
    # gB.muestragv()
    """
    gB.archivogv("BarabasiAlbert100")
    gBFS = gB.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_BarabasiAlbert100")
    gDFSr = gB.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_BarabasiAlbert100")
    gDFSi = gB.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_BarabasiAlbert100")
    """
    # Grafo con el modelo Barabasi-Albert para 500 nodos y cálculo de BFS, DFSr y DFSi
    # gB = algoritmos.grafoBarabasiAlbert(500, 2)
    # gB.muestragv()
    """
    gB.archivogv("BarabasiAlbert500")
    gBFS = gB.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_BarabasiAlbert500")
    gDFSr = gB.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_BarabasiAlbert500")
    gDFSi = gB.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_BarabasiAlbert500")
    """
    # Grafo con el modelo Dorogovtsev-Mendes para 30 nodos y cálculo de BFS, DFSr y DFSi
    gD = algoritmos.grafoDorogovtsevMendes(30)
    gD.muestragv()
    """
    gD.archivogv("DorogovtsevMendes30")
    gBFS = gD.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_DorogovtsevMendes30")
    gDFSr = gD.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_DorogovtsevMendes30")
    gDFSi = gD.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_DorogovtsevMendes30")
    gDjk = gD.Dijkstra(1)
    gDjk.muestragrafodijkstra()
    gDjk.archivogvdijkstra("Dijkstra_Dorogovtsev30")
    """
    gKrk = gD.KruskalDir()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("Kruskal_Dorogovtsev30")
    gKrk = gD.KruskalInv()
    gKrk.muestragrafocostos()
    gKrk.archivogvCostos("KruskaIl_Dorogovtsev30")
    gPrm = gD.Prim()
    gPrm.muestragrafocostos()
    gPrm.archivogvCostos("Prim_Dorogovtsev30")
    # Grafo con el modelo Dorogovtsev-Mendes para 100 nodos y cálculo de BFS, DFSr y DFSi
    # gD = algoritmos.grafoDorogovtsevMendes(100)
    # gD.muestragv()
    """
    gD.archivogv("DorogovtsevMendes100")
    gBFS = gD.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_DorogovtsevMendes100")
    gDFSr = gD.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_DorogovtsevMendes100")
    gDFSi = gD.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_DorogovtsevMendes100")
    """
    # Grafo con el modelo Dorogovtsev-Mendes para 500 nodos y cálculo de BFS, DFSr y DFSi
    # gD = algoritmos.grafoDorogovtsevMendes(500)
    # gD.muestragv()
    """
    gD.archivogv("DorogovtsevMendes500")
    gBFS = gD.arbol_bfs(1)
    gBFS.muestragv()
    gBFS.archivogv("BFS_DorogovtsevMendes500")
    gDFSr = gD.arbol_dfs_r(1)
    gDFSr.muestragv()
    gDFSr.archivogv("DFSr_DorogovtsevMendes500")
    gDFSi = gD.arbol_dfs_i(1)
    gDFSi.muestragv()
    gDFSi.archivogv("DFSi_DorogovtsevMendes500")
    """