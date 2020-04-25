from graph import *
from node import Node
# string = """10 16
# 0 1
# 1 2
# 1 6
# 2 3
# 0 9
# 9 5
# 3 5
# 7 5
# 7 3
# 7 8
# 6 5
# 5 8
# 9 4
# 4 1
# 4 6
# 6 7
# 6 8
# """

string = """10 16
1 2
2 3
2 7
3 4
1 10
10 6
4 6
8 6
8 4
8 9
7 6
6 9
10 5
5 2
5 7
7 8
7 9
"""
x = GraphMatrix.load(string)
print(x)
# print(x.dfs_sort())
# print(x.khan_sort())
