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

    def checkForCycles(self):
        size = len(self.matrix)
        path = []
        visited = {}
        for i in range(1, size + 1):
            visited[i] = False
        stack = []
        while len(path) != size:
            for index in visited:
                if not visited[index]:
                    node = index
                    break
            stack.append(node)
            visited[node] = True

            while len(stack):
                found_successor = False
                for index in self.matrix[node]:
                    direction = self.matrix[node][index]
                    if direction == 1 and not visited[index]:
                        found_successor = True
                        node = index
                        stack.append(node)
                        visited[node] = True
                        break
                    elif direction == 1:
                        if index in stack:
                            return True
                if not found_successor:
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
        visited = {}
        for i in range(1, size + 1):
            visited[i] = False
        stack = []
        while len(path) != size:
            for index in visited:
                if not visited[index]:
                    node = index
                    break
            stack.append(node)
            visited[node] = True

            while len(stack):
                found_successor = False
                for index in self.matrix[node]:
                    direction = self.matrix[node][index]
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
        disabled_nodes = {}
        for i in range(1, size + 1):
            disabled_nodes[i] = False
        # disabled_nodes = [False] * size
        path = []
        node = None
        while len(path) < size:
            for index in self.matrix:
                if -1 not in self.matrix[index].values() and disabled_nodes[index] == False:
                    node = index
                    disabled_nodes[index] = True
                    break
            path.append(node)
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
        visited = {}
        for i in range(1, size+1):
            visited[i] = False
        stack = []
        while len(path) != size:
            for index in visited:
                if not visited[index]:
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
        nodes_status = {}
        for i in range(1, size + 1):
            nodes_status[i] = True
        path = []
        while len(path) < size:
            # poszukaj node z in(n) = 0
            predecessor_status = {}
            for i in range(1, size + 1):
                predecessor_status[i] = True

            for index in self.lst:
                if nodes_status[index]:
                    for successor in self.lst[index]:
                        predecessor_status[successor] = False
                else:
                    predecessor_status[index] = False
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
        available = [True] * (size+1)
        path = []
        while len(path) < size:
            for index in matrix:
                if matrix[index][max_key - 1] == 0 and available[index]:
                    path.append(index)
                    available[index] = False
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
        available = {}
        stack = []
        for i in range(1, size+1):
            available[i] = True
        node = None
        while len(path) != size:
            for node_index in available:
                if available[node_index]:
                    node = node_index
                    break
            stack.append(node)
            available[node] = False
            while len(stack):
                successor_found = False
                for successor in range(1, size+1):
                    if 0 < self.matrix[node][successor] <= size and available[successor]:
                        successor_found = True
                        node = successor
                        stack.append(node)
                        available[node] = False
                        break
                if not successor_found:
                    path.append(node)
                    stack.pop()
                    if len(stack):
                        node = stack[-1]
        return path[::-1]
