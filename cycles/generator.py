import random
def generateGraph(n=10, saturation=0.5, directed=False):
    edges = {}
    for i in range(1, n+1):
        edges[i] = {}
    notUsedArcs = {}
    for v in range(1, n+1):
        for u in range(1, n+1):
            if v != u:
                if random.random() <= saturation:
                    if directed:
                        edges[v][u] = 1
                    else:
                        if v not in edges[u]:
                            edges[u][v] = 1
    numberOfEdges = 0
    output = ''
    for v in edges:
        numberOfEdges += len(edges[v])
        for u in edges[v].keys():
            output += '{} {}\n'.format(v, u)
    return '{} {}\n'.format(n, numberOfEdges) + output

generateGraph(n=10000, saturation=0.5, directed=False)

