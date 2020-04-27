from graph import *
from node import Node

def wprowadzenie_cyfry(tekst, min, max):
    n = input(tekst)
    if n.isnumeric() and min <= int(n) <= max:
        return n
    else:
        return wprowadzenie_cyfry(tekst, min, max)

def verifyEdge(e):
    try:
        e = [int(x) for x in e.split()]
        return len(e) == 2
    except Exception:
        return False

def inputEdge(index):
    while True:
        edge = input('{}> '.format(index))
        if verifyEdge(edge):
            return edge


print("[1] Wprowadź dane z klawiatury.\n"
      "[2] Wczytaj dane z pliku.")
n = wprowadzenie_cyfry("Wybór: ", 1, 2)
input_string = ""
if n == "1":
    v, e = [int(x) for x in input("Wprowadź liczbę wierzchołków i krawędzi: ").split()]
    input_string += "{} {}".format(v, e)
    for i in range(e):
        input_string += '\n' + inputEdge(i)

elif n == "2":
    path = input('sciezka> ')
    with open(path) as f:
        input_string = f.read()

print("Wybierz interpretację grafu: \n"
      "[1] Macierz sąsiedztwa.\n"
      "[2] Lista następników.\n"
      "[3] Macierz grafu.")
n = wprowadzenie_cyfry("Wybór: ", 1, 3)

graph_classes = {
    "1": AdjacencyMatrix,
    "2": SuccessorList,
    "3": GraphMatrix
}

graph = AdjacencyMatrix.load(input_string)
if graph.checkForCycles():
    import sys
    print('Wykryto cykle!')
    sys.exit()

graph = graph_classes[n].load(input_string)
print(graph)
while True:
    print("Wybierz metodę sortowania topologicznego: \n"
          "[1] Procedura przechodzenia wgłąb(DFS).\n"
          "[2] Usuwaniem wierzchołków o zerowym stopniu wejściowym(DEL).\n"
          "[3] Exit")

    n = wprowadzenie_cyfry("Wybór: ", 1, 3)

    if n == "1":
        print(graph.dfs_sort())

    if n == "2":
        print(graph.khan_sort())
    if n == "3":
        break


# from graph import *
# from node import Node
# # string = """10 16
# # 0 1
# # 1 2
# # 1 6
# # 2 3
# # 0 9
# # 9 5
# # 3 5
# # 7 5
# # 7 3
# # 7 8
# # 6 5
# # 5 8
# # 9 4
# # 4 1
# # 4 6
# # 6 7
# # 6 8
# # """
#
# string = """10 16
# 1 2
# 2 3
# 2 7
# 3 4
# 1 10
# 10 6
# 4 6
# 8 6
# 8 4
# 8 9
# 7 6
# 6 9
# 10 5
# 5 2
# 5 7
# 7 8
# 7 9
# """
# x = GraphMatrix.load(string)
# print(x)
# print(x.dfs_sort())
# print(x.khan_sort())
