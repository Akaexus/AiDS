from graph import *
from node import Node

def wprowadzenie_cyfry(tekst):
    n = input(tekst)
    if n.isnumeric() == 1:
        return n
    else:
        return wprowadzenie_cyfry(tekst)


while True:
    print("[1] Wprowadź dane z klawiatury.\n"
          "[2] Wygeneruj losowy ciąg.\n"
          "[3] Wczytaj dane z pliku.")
    graf = []
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":
        v, e = [int(x) for x in input("Wprowadź liczbę wierzchołków i krawędzi: ").split()]
        for i in range(e):
            para = input().split()
            para[0] = int(para[0])
            para[1] = int(para[1])
            graf.append(para)
        break

    if n == "2":

        break

    if n == "3":

        break


while True:
    print("Wybierz interpretację grafu: \n"
          "[1] Macierz sąsiedztwa.\n"
          "[2] Lista następników.\n"
          "[3] Macierz grafu.")
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":

        break

    if n == "2":

        break

    if n == "3":

        break


while True:
    print("Wybierz metodę sortowania topologicznego: \n"
          "[1] Procedura przechodzenia wgłąb(DFS).\n"
          "[2] Usuwaniem wierzchołków o zerowym stopniu wejściowym(DEL).")
    lista = []
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":
        print(lista.dfs_sort())
        break

    if n == "2":
        print(lista.khan_sort())
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
