from graphs import *

xd = """8 10
1 2
2 3
3 1
3 5
4 3
4 8
5 7
6 4
7 4
8 6
"""

graph = AdjacencyMatrix.load(xd)
print(graph)
print(graph.getEulerCycle())
graph = SuccessorList.load(xd)
print(graph)
print(graph.getEulerCycle())
# print(' -> '.join(map(str, graph.getHamiltonianCycle())))