import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getReati=DAO.getReati()
        self.getMesi=DAO.getMesi()
        self.grafo = nx.Graph()
        self._idMap = {}
        self.pesoMedio=0

    def creaGrafo(self, reato, mese):
        self.nodi = DAO.getNodi(reato,mese)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(reato,mese)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, reato,mese):
        somma=0
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(mese,reato)
        for connessione in allEdges:
            nodo1 =connessione.v1
            nodo2 = connessione.v2
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)
                    somma+=connessione.peso
        self.pesoMedio=somma/len(self.grafo.edges)
    def analisi(self):
        lista=[]
        for arco in self.grafo.edges:
            if self.grafo[arco[0]][arco[1]]["weight"]>self.pesoMedio:
                lista.append((arco[0],arco[1],self.grafo[arco[0]][arco[1]]["weight"]))
        return lista



