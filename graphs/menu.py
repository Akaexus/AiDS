from graph import *
from node import Node


string = """10 16
0 1
1 2
1 6
2 3
0 9
9 5
3 5
7 5
7 3
7 8
6 5
5 8
9 4
4 1
4 6
6 7
6 8
"""
x = AdjacencyMatrix.load(string)
print(x)
print(x.dfs_sort())
print(x.khan_sort())
