from terminaltables import AsciiTable
import copy
class Knapsack:
    n = 0
    b = 0
    items = {}

    def color(s, color='okblue'):
        return '{}{}{}'.format(Knapsack.colors[color], s, Knapsack.colors['endc'])
    colors = {
        'header':'\033[95m',
        'okblue':'\033[94m',
        'okgreen':'\033[92m',
        'warning':'\033[93m',
        'fail':'\033[91m',
        'endc':'\033[0m',
        'bold':'\033[1m',
        'underline':'\033[4m',
    }
    @staticmethod
    def printBackpack(backpack):
        def backpackTable(b):
            table = [list(map(Knapsack.color, ['Item', 'Weight', 'Price']))]
            price = 0
            weight =0
            for id in b:
                table.append([
                    Knapsack.color(id, 'okgreen'),
                    b[id]['weight'],
                    b[id]['price'],
                ])
                weight += b[id]['weight']
                price += b[id]['price']
            table.append(['-'] * 3)
            table.append([Knapsack.color('SUM', 'warning'), weight, price])
            return AsciiTable(table).table

        if isinstance(backpack, dict):
            return backpackTable(backpack)
        else:
            output = ''
            for i in range(len(backpack)):
                output += 'Backpack #{}\n'.format(i + 1)
                output += backpackTable(backpack[i])
                output += '\n' * 2
            return output

    def __str__(self):
        printable_matrix = [['ID', 'Weight', 'Price']]
        for id in self.items:
            printable_matrix.append([id, self.items[id]['weight'], self.items[id]['price']])
        table = AsciiTable(printable_matrix)
        return 'Items: {}\nBackpack capacity: {}\n'.format(self.n, self.b) + str(table.table)

    @staticmethod
    def load(string):
        obj = Knapsack()
        string = string.split('\n')
        obj.n, obj.b = [int(x) for x in string[0].split()]
        i = 1
        for row in string[1::]:
            weight, price = [int(x) for x in row.split()]
            obj.items[i] = {'weight': weight, 'price': price}
            i += 1
        return obj

    def brutalforce(self):
        results = {}
        for matrix in range(1, 2 ** self.n):
            id = matrix
            results[id] = {
                'weight': 0,
                'price': 0
            }
            i = 1
            while matrix:
                if matrix & 1:
                    results[id]['weight'] += self.items[i]['weight']
                    results[id]['price'] += self.items[i]['price']
                matrix >>= 1
                i+=1
        max_price_id = 0
        max_price = 0
        for id in results:
            result = results[id]
            if result['weight'] <= self.b and result['price'] > max_price:
                max_price_id = id
                max_price = result['price']
        items = {}
        i = 1
        while max_price_id:
            if max_price_id & 1:
                items[i] = self.items[i]
            max_price_id >>= 1
            i += 1
        return items

    def printDynamicMatrix(self, matrix):
        table = [['i\j'] + list(map(Knapsack.color, list(range(self.b + 1))))]
        for i, row in enumerate(matrix):
            table.append([Knapsack.color(i)] + row)
            # table.append([Knapsack.color(i)] + row)
        return '\nDynamic programming array\n' + AsciiTable(table).table


    def greedyAlgorithm(self):
        items = sorted(
            self.items.items(),
            key=lambda item: item[1]['price']/item[1]['weight'],
            reverse=True
        )
        backpack = {}
        capacity = self.b
        for i in range(self.n):
            if items[i][1]['weight'] <= capacity:
                capacity -= items[i][1]['weight']
                backpack[items[i][0]] = items[i][1]
            else:
                break
        return backpack

    def dynamicAlgorithm(self):
        matrix = [[0] * (self.b + 1)]
        # wypelnainie macierzy
        for i in range(1, len(self.items) + 1):
            matrix.append([0] * (self.b + 1))
            weight = self.items[i]['weight']
            price = self.items[i]['price']
            for j in range(1, self.b + 1):
                if weight > j:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight] + price)

        # wyswietlanie macierzy
        print(self.printDynamicMatrix(matrix))

        paths = [[[self.n, self.b, True]]]
        final_paths = []
        while len(paths):
            for index, path in enumerate(paths):
                i = path[-1][0]
                j = path[-1][1]
                if i and j:
                    upper = matrix[i-1][j]
                    left = matrix[i-1][j - self.items[i]['weight']] + self.items[i]['price']
                    if upper == left:
                        path2 = copy.deepcopy(path)
                        path[-1][2] = False
                        path.append([i - 1, j, True])
                        path2.append([i-1, j - self.items[i]['weight'], True])
                        paths.append(path2)
                    elif upper == matrix[i][j]:
                        path[-1][2] = False
                        path.append([i - 1, j, True])
                    elif left == matrix[i][j]:
                        path.append([i-1, j - self.items[i]['weight'], True])
                else:
                    final_paths.append(paths.pop(index))
        backpack_sets = []
        for path in final_paths:
            set = {}
            for step in path:
                if step[0] and step[1] and step[2]:
                    set[step[0]] = self.items[step[0]]
            backpack_sets.append(set)
        return backpack_sets






