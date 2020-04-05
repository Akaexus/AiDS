from bst.tree import Tree


def wprowadzenie_cyfry(tekst):
    n = input(tekst)
    if n.isnumeric() == 1:
        return n
    else:
        return wprowadzenie_cyfry(tekst)

while True:
    print("[1] Wprowadź dane z klawiatury.\n"
          "[2] Wygeneruj losowe drzewo.")
    n = wprowadzenie_cyfry("Wybór: ")

    if n == "1":
        drzewo = []
        ile = int(wprowadzenie_cyfry("Podaj liczbę danych: "))
        for i in range(1, ile + 1):
            drzewo.append(int(wprowadzenie_cyfry("Podaj cyfrę: ")))
        print("Oto nasza lista: {}".format(drzewo))
        print(Tree.build_from_data(drzewo))
        break

    if n == "2":
        drzewo = Tree.build_random(int(wprowadzenie_cyfry("Ile elementów ma liczyć drzewo? ")))
        print(drzewo)
        break

    else:
        print("Wprowadź odpowiednią cyfrę!")

while True:
    print("                                            ⋆⋆⋆ M E N U ⋆⋆⋆\n"
          "[1] Wyszukanie w drzewie elementu o najmniejszej wartości i wypisanie ścieżki poszukiwania.\n"
          "[2] Wyszukanie w drzewie elementu o największej wartości i wypisanie ścieżki poszukiwania.\n"
          "[3] Usuwanie elementów drzewa...\n"
          "[4] Wypisanie wszystkich elementów drzewa w porządku rosnącym (in-order).\n"
          "[5] Wypisanie wszystkich elementów drzewa w porządku pre-order.\n"
          "[6] Usunięcie całego drzewa element po elemencie metodą post-order.\n"
          "[7] Wypisanie w porządku pre-order poddrzewa według podanego korzenia (klucza).\n"
          "[8] Równoważenie drzewa...\n"
          "[9] Podgląd drzewa\n"
          "[10] Wyjście" )
    n = wprowadzenie_cyfry("Wybór: ")


    if n == "1":
        print(Tree.find_min(drzewo))

    if n == "2":
        print(Tree.find_max(drzewo))

    if n == "3":
        ile = int(wprowadzenie_cyfry("Ile węzłów usunąć: "))
        for i in range(1, ile + 1):
            klucz = int(wprowadzenie_cyfry("Podaj wartość klucza nr {}: ".format(i)))
            Tree.delete_node(drzewo, klucz)
            print("{}\n".format(drzewo))

    if n == "4":
        print(Tree.in_order(drzewo))

    if n == "5":
        print(Tree.pre_order(drzewo))

    if n == "6":
        print(Tree.delete_post_order(drzewo))

    if n == "7":
        print("jest 7")

    if n == "8":
        while True:
            print("[1] przez rotację.\n"
                  "[2] przez usuwanie korzenia.")
            m = wprowadzenie_cyfry("Wybór: ")
            if m == str(1):
                print(m)
                break
            if m == str(2):
                print(m)
                break
            print("Wprowadź odpowiednią cyfrę!")

    if n == "9":
        print(drzewo)

    if n == "10":
        break
    else:
        continue
