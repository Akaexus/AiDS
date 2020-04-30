import random

def generateGraphData(n=10):
    nodes = list(range(1, n + 1))
    edges = []
    random.shuffle(nodes)
    for i in range(0, n):
        for j in range(i + 1, n):
            if random.randint(0, 1):
                edges.append('{} {}'.format(nodes[i], nodes[j]))
    return '{} {}\n'.format(n, len(edges)) + '\n'.join(sorted(edges))
