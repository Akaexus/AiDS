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
        printable_matrix = copy.deepcopy(self.matrix)
        header = ['\\'] + list(range(size))
        header = list(map(lambda x: '{}{}{}'.format(bcolors.OKBLUE, x, bcolors.ENDC), header))
        printable_matrix.insert(0, header)
        for index in range(size):
            printable_matrix[index + 1].insert(0, '{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC))
        table = AsciiTable(printable_matrix)
        return str(table.table)

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        matrix = [[0] * (size) for i in range(size)]
        for edge in string[1:]:
            if edge != '':
                i, j = map(int, edge.split())
                matrix[i][j] = 1
                matrix[j][i] = -1

        return AdjacencyMatrix(matrix)

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
        visited = [False] * size
        stack = []
        while len(path) != size:
            for index, is_visited in enumerate(visited):
                if not is_visited:
                    node = index
                    break
            stack.append(node)
            visited[node] = True

            while len(stack):
                found_successor = False
                for index, direction in enumerate(self.matrix[node]):
                    if direction == 1 and not visited[index]:
                        found_successor = True
                        node = index
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
        size = len(self.matrix)
        disabled_nodes = [False] * size
        path = []
        node = None
        while len(path) < size:
            for index, row in enumerate(self.matrix):
                if -1 not in row and disabled_nodes[index] == False:
                    node = index
                    disabled_nodes[index] = True
                    break
            path.append(node)
            for successor, direction in enumerate(self.matrix[node]):
                if direction:
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
            print(index, self.lst[index])
            row = ['{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC), self.lst[index]]
            array.append(row)
        table = AsciiTable(array)
        return str(table.table)
        return ''

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        lst = {}
        for index in range(size):
            lst[index] = []
        for edge in string[1:]:
            if edge != '':
                i, j = map(int, edge.split())
                lst[i].append(j)
        return SuccessorList(lst)

    def dfs_sort(self):
        size = len(self.lst)
        path = []
        visited = [False] * size
        stack = []
        while len(path) != size:
            for index, is_visited in enumerate(visited):
                if not is_visited:
                    node = index
                    break
            stack.append(node)
            visited[node] = True
            while len(stack):
                found_successor = False
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
        nodes_status = [True] * size
        path = []
        while len(path) < size:
            # poszukaj node z in(n) = 0
            predecessor_status = [True] * size

            for index in self.lst:
                if nodes_status[index]:
                    for successor in self.lst[index]:
                        predecessor_status[successor] = False
                else:
                    predecessor_status[index] = False
            for node, status in enumerate(predecessor_status):
                if status:
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
        header = ['\\'] + list(range(1, size+3))
        header = list(map(lambda x: '{}{}{}'.format(bcolors.OKBLUE, x, bcolors.ENDC), header))
        printable_matrix.append(header)
        for index in range(1, size):
            row = ['{}{}{}'.format(bcolors.OKBLUE, index, bcolors.ENDC)]
            row += self.matrix[index].values()
            printable_matrix.append(row)
        table = AsciiTable(printable_matrix)
        return str(table.table)

    @staticmethod
    def load(string):
        string = string.split('\n')
        size, number_of_edges = map(int, string[0].split())
        edges = list(filter(lambda e: e!= '', string[1:]))
        matrix = {}
        for i in range(1, size+2):
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
                    matrix[i][j] = successors_list[i][-1] if len(successors_list[i]) else 0
                if rev_edge_exists:
                    matrix[i][j] = size + predecessors_list[i][-1]
                if not edge_exists and not rev_edge_exists:
                    matrix[i][j] = -no_incident_list[i][-1]

            print(matrix)








        return GraphMatrix(matrix)
