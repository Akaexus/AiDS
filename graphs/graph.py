from terminaltables import AsciiTable
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Graph:
    @staticmethod
    def generate():
        pass

class AdjacencyMatrix(Graph):
    matrix = []
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        import copy
        size = len(self.matrix)
        printable_matrix = []
        header = ['\\'] + list(range(size))
        header = list(map(lambda x: '{}{}{}'.format(bcolors.OKBLUE, x, bcolors.ENDC), header))
        printable_matrix.append(header)
        for index in range(1, size+1):
            printable_matrix.append(['{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC)] + list(self.matrix[index].values()))
        table = AsciiTable(printable_matrix)
        return str(table.table)

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        matrix = {}
        for i in range(1, size + 1):
            matrix[i] = {}
            for j in range(1, size + 1):
                matrix[i][j] = 0
        for edge in string[1:]:
            if edge != '':
                i, j = map(int, edge.split())
                matrix[i][j] = 1
                matrix[j][i] = -1

        return AdjacencyMatrix(matrix)

    # poszukaj cykli
    def checkForCycles(self):
        size = len(self.matrix)
        path = []
        # zaincjalizuj tablice statusu odwiedzonego
        visited = {}
        for i in range(1, size + 1):
            visited[i] = False
        stack = []
        while len(path) != size:
            # wybierz pierwszy element do stosu
            for index in visited:
                if not visited[index]:
                    node = index
                    break
            stack.append(node)
            visited[node] = True

            while len(stack):
                found_successor = False
                # znajdz nastepnika
                for index in self.matrix[node]:
                    direction = self.matrix[node][index]
                    if direction == 1 and not visited[index]:
                        # znaleziono następnika
                        found_successor = True
                        node = index
                        stack.append(node)
                        visited[node] = True
                        break
                    elif direction == 1:
                        # znaleziono nastepnika, w którym już byliśmy
                        if index in stack:
                            #znaleziono cykl
                            return True
                if not found_successor:
                    # nie ma nastepników, idź w góre
                    path.append(node)
                    stack.pop()
                    if len(stack):
                        node = stack[-1]
        return False

    # def dfs_sort(self):
    #     visited = [False] * len(self.matrix)
    #     path = []
    #     stack = []
    #     def dfs(node):
    #         if node:
    #             visited[node] = True
    #             stack.append(node)
    #             not_visited_successors = []
    #             for succesor_index, successor_direction in enumerate(self.matrix[node]):
    #                 if successor_direction == 1 and not visited[succesor_index]:
    #                   not_visited_successors.append(succesor_index)
    #             for succesor in not_visited_successors:
    #                 dfs(succesor)
    #     while
    #     dfs(1)
    def dfs_sort(self):
        size = len(self.matrix)
        path = []
        # zaincjalizuj tablice statusu odwiedzonego
        visited = {}
        for i in range(1, size + 1):
            visited[i] = False
        stack = []
        while len(path) != size:
            # wybierz element początkowy
            for index in visited:
                if not visited[index]:
                    node = index
                    break
            stack.append(node)
            visited[node] = True

            while len(stack):
                found_successor = False
                # poszukaj następnika
                for index in self.matrix[node]:
                    direction = self.matrix[node][index]
                    if direction == 1 and not visited[index]:
                        found_successor = True
                        # ustaw następnik jako obecny węzeł
                        node = index
                        # dodaj do stosu
                        stack.append(node)
                        # oznacz jako odwiedzony
                        visited[node] = True
                        break
                if not found_successor:
                    # idz do gory
                    path.append(node)
                    stack.pop()
                    if len(stack):
                        node = stack[-1]
        return path[::-1]

    def khan_sort(self):
        size = len(self.matrix)
        # stworz tablice statusu odwiedzenia
        disabled_nodes = {}
        for i in range(1, size + 1):
            disabled_nodes[i] = False
        # disabled_nodes = [False] * size
        path = []
        node = None
        while len(path) < size:
            for index in self.matrix:
                # znajdź wierzchołek, który nie ma żadnych krawędzi wejściowych
                if -1 not in self.matrix[index].values() and disabled_nodes[index] == False:
                    node = index
                    disabled_nodes[index] = True
                    break
            path.append(node)
            # usuń krawędzie usuniętego wierzchołka
            for successor in self.matrix[node]:
                if self.matrix[node][successor]:
                    self.matrix[node][successor] = 0
                    self.matrix[successor][node] = 0
        return path

class SuccessorList(Graph):
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        array = [
            ['Węzeł',
            'Następniki']
        ]
        for index in self.lst:
            row = ['{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC), self.lst[index]]
            array.append(row)
        table = AsciiTable(array)
        return str(table.table)

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        lst = {}
        for index in range(1, size+1):
            lst[index] = []
        for edge in string[1:]:
            if edge != '':
                i, j = map(int, edge.split())
                lst[i].append(j)
        return SuccessorList(lst)

    def dfs_sort(self):
        size = len(self.lst)
        path = []
        # inicjalizacja listy odwiedzonych
        visited = {}
        for i in range(1, size+1):
            visited[i] = False
        stack = []
        while len(path) != size:
            # poszukaj węzła startowego
            for index in visited:
                if not visited[index]:
                    node = index
                    break
            stack.append(node)
            visited[node] = True
            while len(stack):
                found_successor = False
                # poszukaj dostępnego następnika z listy następników
                for successor in self.lst[node]:
                    if not visited[successor]:
                        found_successor = True
                        node = successor
                        stack.append(node)
                        visited[node] = True
                        break
                if not found_successor:
                    path.append(node)
                    stack.pop()
                    if len(stack):
                        node = stack[-1]
        return path[::-1]

    def khan_sort(self):
        size = len(self.lst)
        # lista z statusem każdego węzła
        nodes_status = {}
        for i in range(1, size + 1):
            nodes_status[i] = True
        path = []
        while len(path) < size:
            # tablica ze statusem poprzednika
            # True jeżeli nie ma poprzednika
            # False jeżeli ma
            predecessor_status = {}
            for i in range(1, size + 1):
                predecessor_status[i] = True

            for index in self.lst:
                # jeżeli węzeł ma jakiegoś następnika, to predecessor_status[następnik] = False
                if nodes_status[index]:
                    for successor in self.lst[index]:
                        predecessor_status[successor] = False
                else:
                    # jeśli został użyty to zostaje oznaczony jako niedostępny
                    predecessor_status[index] = False
            # wyszukaj węzeł bez poprzedników
            for node in predecessor_status:
                if predecessor_status[node]:
                    path.append(node)
                    nodes_status[node] = False
        return path

class GraphMatrix(Graph):
    matrix = []
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        import copy
        size = len(self.matrix)
        printable_matrix = []
        header = ['\\'] + list(range(1, size+4))
        header = list(map(lambda x: '{}{}{}'.format(bcolors.OKBLUE, x, bcolors.ENDC), header))
        printable_matrix.append(header)
        for index in range(1, size+1):
            row = ['{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC)]
            row += self.matrix[index].values()
            row[-3] = '{}{}{}'.format(bcolors.FAIL, row[-3], bcolors.ENDC)
            row[-2] = '{}{}{}'.format(bcolors.OKGREEN, row[-2], bcolors.ENDC)
            row[-1] = '{}{}{}'.format(bcolors.WARNING, row[-1], bcolors.ENDC)
            printable_matrix.append(row)
        table = AsciiTable(printable_matrix)
        return str(table.table)

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        edges = list(filter(lambda e: e!= '', string[1:]))
        matrix = {}
        for i in range(1, size+1):
            matrix[i] = {}
            for j in range(1, size+4):
                    matrix[i][j] = None
        successors_list = {}
        predecessors_list = {}
        no_incident_list = {}
        for i in range(1, size+1):
            successors_list[i] = []
            predecessors_list[i] = []
            no_incident_list[i] = list(range(1, size+1))
        for edge in edges:
            edge = list(map(int, edge.split()))
            successors_list[edge[0]].append(edge[1])
            predecessors_list[edge[1]].append(edge[0])
            no_incident_list[edge[0]].remove(edge[1])
            no_incident_list[edge[1]].remove(edge[0])
        for i in range(1, size+1):
            matrix[i][size + 1] = successors_list[i][0] if len(successors_list[i]) else 0
            matrix[i][size + 2] = predecessors_list[i][0] if len(predecessors_list[i]) else 0
            matrix[i][size + 3] = no_incident_list[i][0] if len(no_incident_list[i]) else 0
            for j in range(1, size+1):
                edge_exists = '{} {}'.format(i, j) in edges
                rev_edge_exists = '{} {}'.format(j, i) in edges
                if edge_exists:
                    if rev_edge_exists:
                        matrix[i][j] = 0
                        pass
                    else:
                        matrix[i][j] = successors_list[i][-1]
                else:
                    if rev_edge_exists:
                        matrix[i][j] = size + predecessors_list[i][-1]
                        pass
                    else:
                        matrix[i][j] = -no_incident_list[i][-1]
                        pass
                # if edge_exists:
                #     matrix[i][j] = successors_list[i][-1] if len(successors_list[i]) else 0
                # if rev_edge_exists:
                #     matrix[i][j] = size + predecessors_list[i][-1]
                # if not edge_exists and not rev_edge_exists:
                #     print(i, j)
                #     matrix[i][j] = -no_incident_list[i][-1]
        return GraphMatrix(matrix)

    def khan_sort(self):
        import copy
        matrix = copy.deepcopy(self.matrix)
        size = len(matrix)
        max_key = size + 3
        # tablica dostępności wierzchołków
        available = [True] * (size+1)
        path = []
        while len(path) < size:
            # poszukaj wierzchołka, który ma drugą dodatkową kolumne równą 0
            for index in matrix:
                if matrix[index][max_key - 1] == 0 and available[index]:
                    path.append(index)
                    available[index] = False
            # przelicz jeszcze raz drugą kolumne dla pozostałych wierzchołków
            for index in matrix:
                if available[index]:
                    matrix[index][max_key - 1] = 0
                    for second_node in range(1, size + 1):
                        if available[second_node]:
                            if size < matrix[index][second_node] <= (2 * size):
                                matrix[index][max_key - 1] = second_node

        return path

    def dfs_sort(self):
        size = len(self.matrix)
        path = []
        # lista dostępnych wierzchołków
        available = {}
        stack = []
        for i in range(1, size+1):
            available[i] = True
        node = None
        while len(path) != size:
            # wybieramy pierwszy element
            for node_index in available:
                if available[node_index]:
                    node = node_index
                    break
            stack.append(node)
            available[node] = False
            while len(stack):
                successor_found = False
                # szukamy następnika
                for successor in range(1, size+1):
                    if 0 < self.matrix[node][successor] <= size and available[successor]:
                        successor_found = True
                        node = successor
                        stack.append(node)
                        available[node] = False
                        break
                if not successor_found:
                    # dodajemy węzeł ścieżki i cofamy się do góry
                    path.append(node)
                    stack.pop()
                    if len(stack):
                        node = stack[-1]
        return path[::-1]
