from knapsack import *


def wprowadzenie_cyfry(tekst='', min=0, max=10000000):
    n = input(tekst)
    if n.isnumeric() and min <= int(n) <= max:
        return n
    else:
        return wprowadzenie_cyfry(tekst, min, max)


def wprowadzanie_2_cyfr(tekst=''):
    para = input(tekst).split()
    if para == []:
        print("Wprowadź jakiekolwiek dane!")
        return wprowadzanie_2_cyfr(tekst)
    else:
        if para[0].isnumeric() and para[1].isnumeric():
            return int(para[0]), int(para[1])
        else:
            print("Wprowadź poprawne dane!")
            return wprowadzanie_2_cyfr(tekst)


print("[1] Wprowadź dane z klawiatury.\n"
      "[2] Wczytaj dane z pliku.")
n = wprowadzenie_cyfry("Wybór: ", 1, 2)
input_string = ""
if n == "1":
    n, b = wprowadzanie_2_cyfr("Wprowadź liczbę przedmiotów i pojemność plecaka: ")
    input_string += "{} {}".format(n, b)
    for i in range(n):
        r, w = wprowadzanie_2_cyfr("Wprowadź rozmiar i wartość przedmiotu nr {}: ".format(i+1))
        input_string += "\n" + "{} {}".format(r, w)

elif n == "2":
    path = input('sciezka> ')
    with open(path) as f:
        input_string = f.read()

plecaczek = Knapsack.load(input_string)
while True:
    print("Wybierz algorytm: \n"
          "[1] Algorytm programowania dynamicznego APD. \n"
          "[2] Algorytm zachłanny AZ (współczynnik opłacalności). \n"
          "[3] Algorytm wyczerpujący AW. \n"
          "[4] Wyjście")
    n = wprowadzenie_cyfry("Wybór: ", 1, 4)
    if n == "1":
        print("\nAlgorytm programowania dynamicznego APD.")
        print(Knapsack.printBackpack(plecaczek.dynamicAlgorithm()))
    if n == "2":
        print("\nAlgorytm zachłanny AZ (współczynnik opłacalności).")
        print(Knapsack.printBackpack(plecaczek.greedyAlgorithm()))
    if n == "3":
        print("\nAlgorytm wyczerpujący AW")
        print(Knapsack.printBackpack(plecaczek.brutalforce()))
    if n == "4":
        break
