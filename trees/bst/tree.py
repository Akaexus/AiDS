from bst.node import Node

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

    def __str__(self):
        current = self.nodes[0]
        visited_nodes = []
        depth = 0
        output = []

        def reverse_in_order(node, level=0, side=None):
            if node:
                #prawy
                reverse_in_order(node.right, level +1, 'right')
                visited_nodes.append(node.key)

                # printowanie
                string = ''
                if side:
                    arc = '┌─' if side == 'right' else '└─'
                    string = '  ' * (level - 1) + arc + str(node.key)
                else:
                    string = ' ' * 2 *level + str(node.key)
                output.append(string)
                # lewy
                reverse_in_order(node.left, level + 1, 'left')

        reverse_in_order(self.nodes[0])

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


        print('\n'.join(output))

        print(visited_nodes)
        return ''
