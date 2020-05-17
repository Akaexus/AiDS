from graphs import *

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
