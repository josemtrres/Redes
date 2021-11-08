import random, math, csv, os, sys, time
from PyQt5.QtCore import lowercasebase
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.centrality.group import prominent_group
from networkx.generators.trees import prefix_tree
import numpy as np
import PyQt5

#nodos = random.randrange(15, 51)
nodos = 10

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
    for j in range(1, i+1):
      if i != j:
        aristas.append([j, i])

  for i in range(len(aristas)):
    a = random.choice(aristas)
    aristas.remove(a)
    c = random.randrange(1,16)
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

  origen = matriz[0][0]
  dijk = nx.shortest_path(G, source=origen)
  l = []
  for key in dijk:
    if len(dijk[key]) != 1:
      l.append(dijk[key])


  print(dijk)
  ll = []
  for i in range(len(l)):
    if i == 0:
      ll.append(l[0][0])
    else:
      ll.append(l[i][1])
        
            
  color_map = []
  tabla = []
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

  for node in G:
    if node in ll:
      color_map.append('red')
    else:
      color_map.append('blue')
  
  print(ll)
  
  pos = nx.spring_layout(G)
  valor = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

  nx.draw(G, node_color=color_map, pos=pos, with_labels=True, font_weight='bold')
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
      Nodo_A.append(int(line_split[0])), Nodo_B.append(int(line_split[1])), peso.append(int(line_split[2]))
      Nodos.append(int(line_split[0])), Nodos.append(int(line_split[1]))
      Matriz_csv.append([int(line_split[0]), int(line_split[1]), int(line_split[2])])

  for i in Nodos:
    D.add_nodes_from(Nodos)

  for i in Matriz_csv:
    D.add_edge(i[0], i[1], weight= i[2])

  origen = Matriz_csv[0][0]
  dijk = nx.shortest_path(D, source=origen)
  l = []

  for key in dijk:
    if len(dijk[key]) != 1:
      l.append(dijk[key])
  
  tabla= []
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

  ll = []

  for i in l:
    if len(i) ==2:
      ll.append(i[0])
      ll.append(i[1])
    else:
      ll.append(i[len(i)-1])

  color_map = []
  for node in D:
    if node in ll:
      color_map.append('red')
    else:
      color_map.append('blue')

  pos_csv = nx.spring_layout(D)
  valor_csv = dict([((u, v,), d['weight']) for u, v, d in D.edges(data=True)])
  nx.draw(D, node_color=color_map, pos=pos_csv, with_labels=True, font_weight='bold')
  nx.draw_networkx_edge_labels(D, pos=pos_csv, edge_labels=valor_csv)

  plt.show()

Generacion_Radom(nodos, arcos)

Abrir_Archivo()
