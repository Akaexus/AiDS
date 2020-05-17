from graphs import *

xd = """6 9
1 2
2 3
2 5
3 1
3 4
4 6
5 3
5 4
6 1
"""

graph = AdjacencyMatrix.load(xd)
print(graph.getHamiltonianCycle())
graph = SuccessorList.load(xd)
print(graph.getHamiltonianCycle())
# print(' -> '.join(map(str, graph.getHamiltonianCycle())))