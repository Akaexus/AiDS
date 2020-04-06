from bst.tree import Tree
import random


def wprowadzenie_cyfry(tekst):
    n = input(tekst)
    if n.isnumeric() == 1:
        return n
    else:
        return wprowadzenie_cyfry(tekst)


while True:
    print("[1] Wprowadź dane z klawiatury.\n"
          "[2] Wygeneruj losowy ciąg.")
    lista = []
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":
        ile = int(wprowadzenie_cyfry("Podaj liczbę danych: "))
        for i in range(ile):
            lista.append(int(wprowadzenie_cyfry("Podaj cyfrę (jeszcze {}): ".format(ile - i))))
        break

    if n == "2":
        ile = (int(wprowadzenie_cyfry("Ile elementów ma liczyć drzewo? ")))
        for i in range(ile):
            lista.append(random.randint(0, 64))
        break

while True:
    print("[1] Zbuduj drzewo AVL.\n"
          "[2] Zbuduj losowe drzewo BST.")
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":
        break

    if n == "2":
        drzewo = Tree()
        for i in range(ile):
            drzewo.add(lista[i])
        break

print(drzewo)
while True:
    print("                                            ⋆⋆⋆ M E N U ⋆⋆⋆\n"
          "[1] Wyszukanie w drzewie elementu o najmniejszej wartości i wypisanie ścieżki poszukiwania.\n"
          "[2] Wyszukanie w drzewie elementu o największej wartości i wypisanie ścieżki poszukiwania.\n"
          "[3] Usuwanie elementów drzewa...\n"
          "[4] Wypisanie wszystkich elementów drzewa w porządku rosnącym (in-order).\n"
          "[5] Wypisanie wszystkich elementów drzewa w porządku pre-order.\n"
          "[6] Usunięcie całego drzewa element po elemencie metodą post-order.\n"
          "[7] Wypisanie w porządku pre-order poddrzewa według podanego korzenia (klucza).\n"
          "[8] Równoważenie drzewa przez rotację.\n"
          "[9] Podgląd drzewa.\n"
          "[10] Wyjście." )
    n = wprowadzenie_cyfry("Wybór: ")


    if n == "1":
        print(Tree.find_min(drzewo))
        print(drzewo)

    if n == "2":
        print(Tree.find_max(drzewo))
        print(drzewo)

    if n == "3":
        ile = int(wprowadzenie_cyfry("Ile węzłów usunąć: "))
        for i in range(1, ile + 1):
            klucz = int(wprowadzenie_cyfry("Podaj wartość klucza nr {}: ".format(i)))
            Tree.delete_node(drzewo, klucz)
            print("{}\n".format(drzewo))

    if n == "4":
        print(Tree.in_order(drzewo))
        print(drzewo)

    if n == "5":
        print(Tree.pre_order(drzewo))
        print(drzewo)

    if n == "6":
        print(Tree.delete_post_order(drzewo))

    if n == "7":
        klucz = int(wprowadzenie_cyfry("Podaj klucz: "))
        print(Tree.pre_order(drzewo, klucz))
        print(drzewo)

    if n == "8":
        print(Tree.balance(drzewo))
        print(drzewo)

    if n == "9":
        print(drzewo)

    if n == "10":
        break
    else:
        continue
