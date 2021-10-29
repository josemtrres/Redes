import random, math
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.traversal import breadth_first_search
import numpy as np


vertices = []
aristas = []
aristas_random = []
dic1  = {}
def Generacion_Radom(n):
  G = nx.DiGraph()
  peso = 0
  m =  math.ceil(n + (n/2))
  print("Generando un grafo con " , n , " vertices y " , m , " arcos dirigidos\n")

  for i in range(1, n+1):
    G.add_node(i)
    vertices.append(i)

  for i in range(1, n+1):
    for j in range(1, i +1):
      if i != j:
        c = random.randrange(1, 16)
        dic1[i, j] = str(c)
        #G.add_edge(i, j, weight = c)
        aristas.append((i, j))

  for i in range(m):
    a = random.choice(aristas)
    aristas.remove(a)
    aristas_random.append(a)

  for i in range(len(aristas_random)):
    c = random.choice(1, 16)
    G.add_edge_from(aristas_random, c)
  
  #G.add_edges_from(aristas_random) #ESTARÁ COMENDATO HASTA SABER SI SI SE ESTÁN AGREGANDO LOS PESOS

  return G

#n = random.randrange(15, 51)

n = 5
G = Generacion_Radom(n)
nx.draw(G, with_labels=True, font_weight='bold')

# DEBUG
#print(G[2][1]["weight"])

#for i in dic1.items():
#  print(i)

# END DEBUG
plt.show()


