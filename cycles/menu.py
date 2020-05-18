from graphs import *

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

print("Czego szukamy? \n"
      "[1] Cyklu Hamiltona.\n"
      "[2] Cyklu Eulera.\n"
      "[3] Obu.")
n = wprowadzenie_cyfry("Wybór: ", 1, 3)
if n == "1":
    graph = AdjacencyMatrix.load(input_string)
    print("Graf nieskierowany (macierz sąsiedztwa)")
    print(graph)
    print(graph.getHamiltonianCycle())
    print("---------------------------------------------------")
    graph = SuccessorList.load(input_string)
    print("Graf skierowany (lista nastepników)")
    print(graph)
    print(graph.getHamiltonianCycle())

elif n == "2":
    graph = AdjacencyMatrix.load(input_string)
    print("Graf nieskierowany (macierz sąsiedztwa)")
    print(graph)
    print(graph.getEulerCycle())
    print("---------------------------------------------------")
    graph = SuccessorList.load(input_string)
    print("Graf skierowany (lista nastepników)")
    print(graph)
    print(graph.getEulerCycle())

elif n == "3":
    graph = AdjacencyMatrix.load(input_string)
    print("Graf nieskierowany (macierz sąsiedztwa)")
    print(graph)
    print(graph.getHamiltonianCycle())
    print(graph.getEulerCycle())
    print("---------------------------------------------------")
    graph = SuccessorList.load(input_string)
    print("Graf skierowany (lista nastepników)")
    print(graph)
    print(graph.getHamiltonianCycle())
    print(graph.getEulerCycle())
