import random, math, csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx import linalg
from networkx.algorithms.assortativity.correlation import degree_pearson_correlation_coefficient
from networkx.algorithms.boundary import node_boundary
from networkx.algorithms.components.biconnected import articulation_points
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.similarity import optimize_graph_edit_distance
from networkx.algorithms.traversal import breadth_first_search
import numpy as np
from numpy.lib.function_base import append
from numpy.typing import _128Bit, _256Bit

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
  print("Generando un grafo con " , n , " vertices y " , m , " arcos dirigidos\n")
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

def Generacion_Radom(n, m):
  G = nx.DiGraph()
  for i in range(1, n+1):
    G.add_node(i)
    vertices.append(i)

  matriz = generar_matriz(n, m)
  for i in matriz:
    G.add_edge(i[0], i[1], weight=i[2])

  pos = nx.spring_layout(G)
  valor = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
  nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
  nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=valor)

  plt.show()

def Abrir_Archivo():
  filename = 'Data.csv'
  D = nx.DiGraph()

  with open('Data.csv', 'r') as csv_file:  
    csv_lec = csv.reader(csv_file)
    next(csv_lec)
    for line in csv_lec:
      line_split=line[0].split(sep=";")
      Nodo_A.append(int(line_split[0]))
      Nodo_B.append(int(line_split[1]))
      peso.append(int(line_split[2]))
      Nodos.append(int(line_split[0]))
      Nodos.append(int(line_split[1]))
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

#Generacion_Radom(nodos, arcos)
#Abrir_Archivo()

#dijk = nx.single_source_shortest_path(G, origen)

#for key in dijk:
#  print(dijk[key])


  


