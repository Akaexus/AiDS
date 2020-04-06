from bst.node import Node
import pprint
pp = pprint.PrettyPrinter(indent=4)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tree:
    root = None
    nodes = {}

    @staticmethod
    def build_from_data(data):
        tree = Tree()
        tree.nodes = {index: Node(v[0], v[1], v[2]) for index, v in data.items()}

        # tworzenie połączeń, nadawanie keyów
        for index, node in tree.nodes.items():
            node.key = index
            if node.left is not None:
                node.left = tree.nodes[node.left]
                node.left.parent = node

            if node.right is not None:
                node.right = tree.nodes[node.right]
                node.right.parent = node

        return tree

    def get_root(self):
        for index in self.nodes:
            if self.nodes[index].parent is None:
                return self.nodes[index]
        return False

    def __str__(self):
        if len(self.nodes) == 0:
            return ''

        current = self.get_root()
        visited_nodes = []
        depth = 0
        output = []

        def reverse_in_order(node, level=0, side=None):
            if node:
                #prawy
                reverse_in_order(node.right, level + 1, 'right')
                visited_nodes.append(node.key)

                # printowanie
                string = ''
                if side:
                    arc = '┌─' if side == 'right' else '└─'
                    string = '  ' * (level - 1) + arc
                else:
                    string = ' ' * 2 *level
                string += '{}{}{} [{}{}{}]'.format(
                    bcolors.OKGREEN, node.value, bcolors.ENDC,
                    bcolors.OKBLUE, node.key, bcolors.ENDC
                )
                output.append(string)
                # lewy
                reverse_in_order(node.left, level + 1, 'left')

        reverse_in_order(self.get_root())

        # napraw pionowe linie w schemacie
        def fix_schema(schema, char):
            matrix = [0] * max(map(len, schema))
            for line_index, line in enumerate(schema):
                line = list(line)
                for char_index, flag in enumerate(matrix):
                    if char_index < len(line):
                        if flag:
                            if line[char_index] == ' ':
                                line[char_index] = '|'
                            else:
                                matrix[char_index] = 0  # wyłącz wstawianie pionowych linii
                        else:
                            if line[char_index] == char:
                                matrix[char_index] = 1

                schema[line_index] = ''.join(line)
            return schema

        output = fix_schema(output, '┌')
        output = fix_schema(output[::-1], '└')[::-1]
        return '\n'.join(output)

    def add(self, value):
        node = Node(value)
        if len(self.nodes):
            current = self.get_root()  # root
            # przeszukaj drzewo w poszukiwaniu ścieżki do ostatniego pasującego liścia
            while current.value > value and current.left is not None or current.value <= value and current.right is not None:
                if current.value > value:
                    if current.left:
                        current = current.left
                else:
                    if current.right:
                        current = current.right
            # przy ostatnim pasującym liściu zdecyduj która strona
            if current.value > value:
                current.left = node
                node.parent = current
                node.key = node.parent.key * 2 + 1
            else:
                current.right = node
                node.parent = current
                node.key = node.parent.key * 2 + 2

        else:
            node.key = 0
            node.parent = None
            self.nodes[0] = node
        self.nodes[node.key] = node

    @staticmethod
    def build_random(n, min=0, max=64):
        import random
        tree = Tree()
        for i in range(n):
            tree.add(random.randint(min, max))
        return tree

    def find_min(self):
        current = self.get_root()
        path = []
        while current.left:
            path.append(current.value)
            current = current.left
        return {
            'path': path,
            'min': current.value
        }

    def find_max(self):
        current = self.get_root()
        path = []
        while current.right:
            path.append(current.value)
            current = current.right
        return {
            'path': path,
            'min': current.value
        }

    def get_successor(self, node):
        # wezel posiada prawego syna
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current
        else:
            current = node
            while current.get_parent_side() != 'left':
                if current.parent:
                    current = current.parent
                else:
                    return None
            return current.parent

    def delete_node(self, entity):
        if isinstance(entity, Node):
            key = entity.key
        else:
            key = entity
        if key not in self.nodes:
            return False

        node = self.nodes[key]
        # samotny węzeł
        if node.parent is None:
            del self.nodes[node.key]
        # bezdzietny węzeł
        elif not node.left and not node.right:
            if node.get_parent_side() == 'left':
                node.parent.left = None
            else:
                node.parent.right = None
                # del self.nodes[key]
            self.nodes[key] = None
            self.nodes.pop(key)
        elif bool(node.left) ^ bool(node.right):  # xor
            parent = node.parent
            if parent.left == node:
                if node.right:
                    parent.left = node.right
                else:
                    parent.left = node.left
            else:
                if node.right:
                    parent.right = node.right
                else:
                    parent.right = node.left
            # del self.nodes[key]
            self.nodes.pop(key)
        else: # ma wszystkie dzieci
            successor = self.get_successor(node)
            node.value = successor.value
            node.key = successor.key
            self.delete_node(successor)

    def in_order(self):
        visited = []

        def in_order(node):
            if node:
                in_order(node.left)
                visited.append(node.value)
                in_order(node.right)

        in_order(self.get_root())
        return visited

    def pre_order(self, key=0):
        visited = []

        def pre_order(node):
            if node:
                visited.append(node.value)
                pre_order(node.left)
                pre_order(node.right)

        pre_order(self.nodes[key])
        return visited

    def delete_post_order(self):
        visited = []

        def post_order(node):
            if node:
                post_order(node.left)
                post_order(node.right)
                self.delete_node(node)
                print('=== Deleting ===')
                print(node)
                print(self)

        post_order(self.get_root())
        return visited

    # turn  string  'left' lub 'right'
    def rotate(self, b, turn):
        a = b.parent
        a_parent = a.parent
        a_parent_side = a.get_parent_side()
        if turn == 'right':
            br = b.right
            a.add_child(br, 'left')
            b.add_child(a, 'right')
            if a_parent:
                a_parent.add_child(b, a_parent_side)
            else:
                b.parent = None
        else:
            bl = b.left
            a.add_child(bl, 'right')
            b.add_child(a, 'left')
            if a_parent:
                # parent_side = a.get_parent_side()
                a_parent.add_child(b, a_parent_side)
            else:
                b.parent = None

    def balance(self):
        root = self.get_root()
        current = root
        root = root.right
        # faza 1 - lista liniowa idąca w prawo
        n = 1
        while current.right or current.left:
            while current.left is not None:
                self.rotate(current.left, 'right')
                current = current.parent
            current = current.right
            n += 1

        def log2(x):
            y = 1
            x >>= 1
            while x:
                x >>= 1
                y <<= 1
            return y

        s = n + 1 - log2(n+1)
        root = self.get_root()
        current = root.right
        for i in range(s):
            self.rotate(current, 'left')
            if current.right:
                current = current.right.right

        n -= s
        root = self.get_root()
        while n > 1:
            n >>= 1
            current = root.right
            root = current
            for i in range(n):
                self.rotate(current, 'left')
                if current.right:
                    current = current.right.right








