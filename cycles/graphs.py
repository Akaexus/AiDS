from terminaltables import AsciiTable
import copy
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
                matrix[j][i] = 1

        matrix = AdjacencyMatrix(matrix)
        matrix.number_of_edges = number_of_edges
        return matrix

    # algorytm Robertsa-Floresa
    def getHamiltonianCycle(self):
        size = len(self.matrix)
        stack = []
        stack_size = 0
        visited = {}
        for i in self.matrix:
            visited[i] = False
        start_node = list(visited.keys())[0]
        def hamiltonianCycle(node):
            nonlocal stack_size
            nonlocal visited
            nonlocal stack
            nonlocal size
            visited[node] = True
            stack_size += 1

            # szukamy nastepnika
            for successor in self.matrix[node]:
                if self.matrix[node][successor] == 1:
                    # warunek koncowy - zrobilismy pelen cykl
                    if successor == start_node and stack_size == size:
                        return True
                    # nieodwiedzony nastepnik
                    if not visited[successor]:
                        if hamiltonianCycle(successor):
                            stack.append(successor)
                            return True
            # jesli wczesniej nie bylo returna
            # to jest to slepa sciezka, wracamy
            visited[node] = False
            stack_size -= 1
            return False

        hamiltonianCycle(start_node)
        if len(stack) == size - 1:
            return "Cykl Hamiltona: {}".format([start_node] + stack[::-1] + [start_node])
        else:
            return "Graf wejściowy nie zawiera cyklu Hamiltona."
        return "Cykl Hamiltona: {}".format(stack)


    def getEulerCycle(self):
        stack = []
        matrix = copy.deepcopy(self.matrix)
        start_node = list(matrix.keys())[0]
        # dfs
        def euler(node):
            # szukamy nastepnika
            for successor in matrix[node]:
                if matrix[node][successor]:
                    # usuwamy krawedz
                    matrix[node][successor] = 0
                    matrix[successor][node] = 0
                    euler(successor)
            stack.append(node)
        euler(start_node)
        if len(stack) == self.number_of_edges + 1 and stack[0] == stack[-1]:
            return "Cykl Eulera: {}".format(stack)
        else:
            return "Graf wejściowy nie zawiera cyklu Eulera."


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

        graph = SuccessorList(lst)
        graph.number_of_edges = number_of_edges
        return graph

    # algorytm Robertsa-Floresa
    def getHamiltonianCycle(self):
        size = len(self.lst)
        stack = []
        stack_size = 0
        visited = {}
        for i in self.lst:
            visited[i] = False
        start_node = list(visited.keys())[0]

        def hamiltonianCycle(node):
            nonlocal stack_size
            nonlocal visited
            nonlocal stack
            nonlocal size
            visited[node] = True
            stack_size += 1

            # szukamy nastepnika
            for successor in self.lst[node]:
                # warunek koncowy - zrobilismy pelen cykl
                if successor == start_node and stack_size == size:
                    return True
                # nieodwiedzony nastepnik
                if not visited[successor]:
                    if hamiltonianCycle(successor):
                        stack.append(successor)
                        return True
            # jesli wczesniej nie bylo returna
            # to jest to slepa sciezka, wracamy
            visited[node] = False
            stack_size -= 1
            return False
        hamiltonianCycle(start_node)
        if len(stack) == size - 1:
            return [start_node] + stack[::-1] + [start_node]
        else:
            return "Graf wejściowy nie zawiera cyklu Hamiltona."
        return "Cykl Hamiltona: {}".format(stack)

    def getEulerCycle(self):
        stack = []
        lst = copy.deepcopy(self.lst)
        start_node = list(lst.keys())[0]

        #dfs
        def euler(node):
            # szukamy nastepnika
            for index, successor in enumerate(lst[node]):
                if successor:
                    # usuwamy krawedz
                    lst[node][index] = 0
                    euler(successor)
            stack.append(node)
        euler(start_node)
        if stack[0] == stack[-1] and len(stack) != self.number_of_edges:
            return "Cykl Eulera: {}".format(stack[::-1])
        else:
            return "Graf wejściowy nie zawiera cyklu Eulera."
