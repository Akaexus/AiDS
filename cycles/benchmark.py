from graphs import *
import time
import random


def generator(n=10, saturation=0.1, directed=False):
    cycle = list(range(1, n+1))
    random.shuffle(cycle)
    cycle.append(cycle[0])
    print(cycle)
    edges = {}
    numberOfEdges = 0
    for i in range(1, n+1):
        edges[i] = {}
    for i in range(1, len(cycle)):
        numberOfEdges += 1
        edges[cycle[i-1]][cycle[i]] = 1
    finalNumberOfEdges = int(((n*(n-1)) if directed else int((n*(n-1))/2)) * saturation)
    candidateEdges = []
    for v in edges:
        for u in range(1, n+1):
            if u!=v and u not in edges[v]:
                if [v, u] not in candidateEdges:
                    candidateEdges.append([u, v])
    random.shuffle(candidateEdges)
    for i in candidateEdges[:(finalNumberOfEdges-numberOfEdges)]:
        edges[i[0]][i[1]] = 1
    output = ''
    for v in edges:
        for u in edges[v].keys():
            output += '{} {}\n'.format(v, u)
    return '{} {}\n'.format(n, numberOfEdges) + output


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


nasycenia = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
wierzchołki = [10, 12, 14, 16, 18, 20]

NS_Euler = []
NS_Hamilton = []
S_Euler = []
S_Hamilton = []


for s in nasycenia:
    for n in wierzchołki:
        for i in range(10):
            dane = generator(n, s, True)

            # graf = AdjacencyMatrix.load(dane)
            # start = time.time()
            # graf.getEulerCycle()
            # finish = time.time()
            # NS_Euler.append(finish - start)
            #
            # start = time.time()
            # graf.getHamiltonianCycle()
            # finish = time.time()
            # NS_Hamilton.append(finish - start)

            graf = SuccessorList.load(dane)
            start = time.time()
            graf.getEulerCycle()
            finish = time.time()
            S_Euler.append(finish - start)

            start = time.time()
            graf.getHamiltonianCycle()
            finish = time.time()
            S_Hamilton.append(finish - start)
        print("Liczba wierzchołków: {} , nasycenie: {}".format(n, s))
        #print("Graf nieskierowany - Cykl Hamiltona: średnio {}s , odchylenie {}s".format(srednia(NS_Hamilton), odchylenie(NS_Hamilton)))
        #print("Graf nieskierowany - Cykl Eulera: średnio {}s , odchylenie {}s".format(srednia(NS_Euler), odchylenie(NS_Euler)))
        print("Graf skierowany - Cykl Hamiltona: średnio {}s , odchylenie {}s".format(srednia(S_Hamilton), odchylenie(S_Hamilton)))
        print("Graf skierowany - Cykl Eulera: średnio {}s , odchylenie {}s".format(srednia(S_Euler), odchylenie(S_Euler)))
        print("----------------------------------------------------------------------------------------------------")
        NS_Euler.clear()
        NS_Hamilton.clear()
        S_Euler.clear()
        S_Hamilton.clear()
