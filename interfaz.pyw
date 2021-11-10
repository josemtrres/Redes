from inspect import FullArgSpec
import random, math, csv, os, sys, webbrowser, time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *
from interfaz_ui import *

#---
#--- pyuic5 -x interfaz.ui -o interfaz_ui.py
#---
contador = 0
inicial = time.time()
final = time.time()
def generar_matriz(n):
    aristas = []
    matriz_dispersa = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i != j:
                aristas.append([j, i])

    for i in range(len(aristas)):
        a = random.choice(aristas)
        aristas.remove(a)
        c = random.randrange(1,16)
        matriz_dispersa.append([a[0], a[1], c])

    return matriz_dispersa

class Window(QWidget):

    def __init__(self, panrent = None):
        QtWidgets.QWidget.__init__(self, panrent)
        self.ui = Ui_LinkState()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.setMaximum(50)
        self.ui.horizontalSlider.setMinimum(15)
        self.ui.horizontalSlider.setValue(32)
        
        self.ui.textEdit.setPlainText("Inserte Archivo .CSV")
        
        self.ui.pushButton.clicked.connect(self.Generar_aleatorio)
        self.ui.pushButton_2.clicked.connect(self.Abrir_Archivo)
        self.ui.pushButton_3.clicked.connect(self.sorpresa)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Nodo A', 'Nodo B', 'Peso'])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def Generar_aleatorio(self):
        global contador
        contador == 0
        inicial = time.time()
        nodos = self.ui.horizontalSlider.value()
        string = ("Generando grafo aleatorio de "+ str(nodos) + " nodos.")
        self.ui.label.setText("LINK-STATE")
        self.ui.label_11.setText("0")
        self.ui.label_3.setText(str(string))
        self.ui.label_2.setText("Grafo cargado por archivo \'.csv\'.")

        l = []
        ll = []
        vertices = []
        color_map = []
        tabla = []
    
        G = nx.DiGraph()
        
        for i in range(1, self.ui.horizontalSlider.value()+1):
            G.add_node(i)
            vertices.append(i)
            contador += 1
        
        matriz = generar_matriz(self.ui.horizontalSlider.value())
        
        for i in matriz:
            G.add_edge(i[0], i[1], weight=i[2])
            contador += 1
        
        origen = matriz[0][0]

        dijk = nx.shortest_path(G, source=origen)
     
        for key in dijk:
            l.append(dijk[key])
            contador += 1
        for i in range(len(l)):
            if i == 0:
                ll.append(l[0][0])
            else:
                ll.append(l[i][1])
            contador += 1
        for i in l:
            if G.has_edge(i[0], i[len(i)-1]):
                a = i[0]
                b = i[len(i)-1]
                c = G[a][b]["weight"]
                tabla.append([a, b, c])
            else:
                for j in range(len(i)):
                    if G.has_edge(i[j], i[len(i)-1]):
                        a = i[j]
                        b = i[len(i)-1]
                        c = G[a][b]["weight"]
                        tabla.append([a, b, c])
                    contador += 1
            contador += 1
        
        self.tabla(tabla)

        for node in G:
            if node in ll:
                color_map.append('red')
            else:
                color_map.append('blue')
            contador += 1
       
        pos = nx.spring_layout(G)
        valor = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
        
        plt.clf()
        
        plt.title('Grafo Aleatorio')
        
        self.dibujar_final(G, pos, valor, color_map)
        
        self.ui.label_8.setText(str(contador))
        
        
        final = time.time()
        self.ui.label_11.setText(str(final-inicial))
        
    def Abrir_Archivo(self):
        global contador
        contador == 0
        Matriz_csv = []
        Nodos = []
        Nodo_A = []
        Nodo_B = []
        peso = []

        filename  = self.ui.textEdit.toPlainText()

        D = nx.DiGraph()
        try:
            self.ui.label.setText("LINK-STATE")
            self.ui.label_3.setText("Grafo aleatorio entre 15 y 50 nodos.")
            self.ui.label_11.setText("0")
            self.ui.label_2.setText("Grafo cargado")
            inicial = time.time()
            with open(filename, 'r') as csv_file:
                csv_lec = csv.reader(csv_file)
                next(csv_lec)
                for line in csv_lec:
                    line_split=line[0].split(sep=";")
                    Nodo_A.append(int(line_split[0])), Nodo_B.append(int(line_split[1])), peso.append(int(line_split[2]))
                    Nodos.append(int(line_split[0])), Nodos.append(int(line_split[1]))
                    Matriz_csv.append([int(line_split[0]), int(line_split[1]), int(line_split[2])])
                    contador += 1
                    
            for i in Nodos:
                D.add_nodes_from(Nodos)
                contador += 1
                

            for i in Matriz_csv:
                D.add_edge(i[0], i[1], weight= i[2])
                contador += 1

            origen = Matriz_csv[0][0]
            dijk = nx.shortest_path(D, source=origen)
            l = []
            for key in dijk:
                if len(dijk[key]) != 1:
                    l.append(dijk[key])
                contador += 1

            tabla = []
            for i in l:
                if D.has_edge(i[0], i[len(i)-1]):
                    a = i[0]
                    b = i[len(i)-1]
                    c = D[a][b]["weight"]
                    tabla.append([a, b, c])
                else:
                    for j in range(len(i)):
                        if D.has_edge(i[j], i[len(i)-1]):
                            a = i[j]
                            b = i[len(i)-1]
                            c = D[a][b]["weight"]
                            tabla.append([a, b, c])
                        contador += 1
                contador += 1
                    
            self.tabla(tabla)
            ll = []
            for i in l:
                if len(i) ==2:
                    ll.append(i[0])
                    ll.append(i[1])
                else:
                    ll.append(i[len(i)-1])
                contador += 1

            color_map = []
            for node in D:
                if node in ll:
                    color_map.append('red')
                else:
                    color_map.append('blue')
                contador += 1
                
            pos_csv = nx.spring_layout(D)
            valor_csv = dict([((u, v,), d['weight']) for u, v, d in D.edges(data=True)])
                    
            plt.clf()
            plt.title('Grafo cargado')
            self.dibujar_final(D, pos_csv, valor_csv, color_map)
            self.ui.label_8.setText(str(contador))
            final = time.time()
            self.ui.label_11.setText(str(final-inicial))
        except FileNotFoundError:
                self.ui.label.setText("E R R O R (x-x)")

    def dibujar_final(self, G, pos, valor, color_map):
        nx.draw(G, node_color=color_map, pos=pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=valor)
        plt.show()
    
    def tabla(self, tabla):
        global contador
        
        self.ui.tableWidget.setRowCount(len(tabla))
        for i in range (len(tabla)):
            for j in range(3):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(tabla[i][j])))
                contador += 1
            contador += 1
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def sorpresa(self): #La mejor forma de programar es con una sonrisa :D
        c = random.randrange(0,2)
        if c == 1:
            webbrowser.open_new("https://github.com/josemtrres/Redes")
            self.ui.pushButton_3.disconnect()
        else:
            webbrowser.open_new("https://www.youtube.com/watch?v=PyoRdu-i0AQ")
            self.ui.pushButton_3.disconnect()
    
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    app = Window()
    app.show()
    sys.exit(aplicacion.exec_())
