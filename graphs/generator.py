import random
from graph import *
import time

def generator(n=10):
    nodes = list(range(1, n + 1))
    edges = []
    random.shuffle(nodes)
    for i in range(0, n):
        for j in range(i + 1, n):
            if random.randint(0, 1):
                edges.append('{} {}'.format(nodes[i], nodes[j]))
    return '{} {}\n'.format(n, len(edges)) + '\n'.join(sorted(edges))

def srednia(lista):
    x = sum(lista) / len(lista)
    return x

def odchylenie(lista):
    import math
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    srednia = sum(lista)/len(lista)
    gora = 0
    for i in range(len(lista)):
        gora += (lista[i] - srednia)**2
    odchylenie = math.sqrt(gora/len(lista))
    return odchylenie


wierzchołki = [100, 200, 300, 400, 500]
for n in wierzchołki:
    DFS_GraphMatrix = []
    DEL_GraphMatrix = []
    DFS_AdjacencyMatrix = []
    DEL_AdjacencyMatrix = []
    DFS_SuccessorList = []
    DEL_SuccessorList = []
    for i in range(5):
        dane = generator(n)

        graph = GraphMatrix.load(dane)
        start = time.time()
        graph.dfs_sort()
        finish = time.time()
        DFS_GraphMatrix.append(finish-start)
        start = time.time()
        graph.khan_sort()
        finish = time.time()
        DEL_GraphMatrix.append(finish-start)

        graph = AdjacencyMatrix.load(dane)
        start = time.time()
        graph.dfs_sort()
        finish = time.time()
        DFS_AdjacencyMatrix.append(finish-start)
        start = time.time()
        graph.khan_sort()
        finish = time.time()
        DEL_AdjacencyMatrix.append(finish-start)

        graph = SuccessorList.load(dane)
        start = time.time()
        graph.dfs_sort()
        finish = time.time()
        DFS_SuccessorList.append(finish - start)
        start = time.time()
        graph.khan_sort()
        finish = time.time()
        DEL_SuccessorList.append(finish - start)

    print("Macierz grafu: {} elementów: \n"
          "    DFS: {} sekund, odchylenie = {} \n"
          "    DEL: {} sekund, odchylenie = {}".format(n, srednia(DFS_GraphMatrix), odchylenie(DFS_GraphMatrix), srednia(DEL_GraphMatrix), odchylenie(DEL_GraphMatrix)))
    print("Macierz sąsiedztwa: {} elementów: \n"
          "    DFS: {} sekund, odchylenie = {} \n"
          "    DEL: {} sekund, odchylenie = {}".format(n, srednia(DFS_AdjacencyMatrix), odchylenie(DFS_AdjacencyMatrix), srednia(DEL_AdjacencyMatrix), odchylenie(DEL_AdjacencyMatrix)))
    print("Lista nastepników: {} elementów: \n"
          "    DFS: {} sekund, odchylenie = {} \n"
          "    DEL: {} sekund, odchylenie = {}".format(n, srednia(DFS_SuccessorList), odchylenie(DFS_SuccessorList), srednia(DEL_SuccessorList), odchylenie(DEL_SuccessorList)))
