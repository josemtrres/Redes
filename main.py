import random, math
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.components.biconnected import articulation_points
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.traversal import breadth_first_search
import numpy as np
from numpy.typing import _128Bit, _256Bit

#nodos = random.randrange(15, 51)
nodos = 5

arcos =  math.ceil(nodos + (nodos/2))

vertices = []
aristas = []
aristas_random = []
matriz = []

print(type(matriz))

def generar_matriz(n, m):
  
  matriz_dispersa = []

  for i in range(1, n+1):
    for j in range(1, i +1):
      if i != j:
        aristas.append([i, j])

  for i in range(m):
    a = random.choice(aristas)
    c = random.randrange(1,16)
    aristas.remove(a)
    aristas_random.append(a)
    matriz_dispersa.append([a[0], a[1], c])

  return matriz_dispersa

def Generacion_Radom(n, m):
  G = nx.DiGraph()
  print("Generando un grafo con " , n , " vertices y " , m , " arcos dirigidos\n")

  for i in range(1, n+1):
    G.add_node(i)
    vertices.append(i)

  matriz = generar_matriz(n, m)

  print(matriz)  
  for i in matriz:

    G.add_edge(i[0], i[1], weight=i[2])
  return G


G = Generacion_Radom(nodos, arcos)
pos = nx.spring_layout(G)
valor = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=valor)
plt.show()


