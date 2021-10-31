import random, math, csv, os, sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from interfaz_ui import *

nodos = random.randrange(15, 51)
#nodos = 5

arcos =  math.ceil(nodos + (nodos/2))

vertices = []
aristas = []
matriz = []
matriz_dispersa = []

Matriz_csv = []

Nodos = []
Nodo_A = []
Nodo_B = []
peso = []

def generar_matriz(n, m):
  for i in range(1, n+1):
    for j in range(1, i +1):
      if i != j:
        aristas.append([i, j])

  for i in range(m):
    a = random.choice(aristas)
    c = random.randrange(1,16)
    aristas.remove(a)
    matriz_dispersa.append([a[0], a[1], c])

  return matriz_dispersa

class Window(QWidget):
    def __init__(self, panrent = None):
        QtWidgets.QWidget.__init__(self, panrent)
        self.ui = Ui_LinkState()
        self.ui.setupUi(self)
        if self.ui.radioButton.isChecked() == False:
            self.ui.pushButton.clicked.connect(self.Generar_aleatorio)
        else:
            pass

        filename  = self.ui.archivo.toPlainText()
        if filename != " ":
            self.ui.pushButton.clicked.connect(self.Abrir_Archivo)

    def Generar_aleatorio(self):
        matriz = generar_matriz(nodos, arcos)

        G = nx.DiGraph()
        for i in range(1, nodos+1):
            G.add_node(i)
            vertices.append(i)

        for i in matriz:
            G.add_edge(i[0], i[1], weight=i[2])
        pos = nx.spring_layout(G)
        valor = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
        nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=valor)

        plt.show()

    def Abrir_Archivo(self):
        D = nx.DiGraph()

        filename  = self.ui.archivo.toPlainText()

        with open(filename, 'r') as csv_file:  
            csv_lec = csv.reader(csv_file)
            next(csv_lec)
            for line in csv_lec:
                line_split=line[0].split(sep=";")
                Nodo_A.append(int(line_split[0])), Nodo_B.append(int(line_split[1])), peso.append(int(line_split[2]))
                Nodos.append(int(line_split[0])), Nodos.append(int(line_split[1]))
                Matriz_csv.append([int(line_split[0]), int(line_split[1]), int(line_split[2])])

        for i in Nodos:
            D.add_nodes_from(Nodos)

        for i in Matriz_csv:
            D.add_edge(i[0], i[1], weight= i[2])
        pos_csv = nx.spring_layout(D)
        valor_csv = dict([((u, v,), d['weight']) for u, v, d in D.edges(data=True)])
        nx.draw(D, pos=pos_csv, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(D, pos=pos_csv, edge_labels=valor_csv)

        plt.show()

    
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    app = Window()
    app.show()
    sys.exit(aplicacion.exec_())
