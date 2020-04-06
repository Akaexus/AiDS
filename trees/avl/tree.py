from avl.node import AVLNode
from bst.tree import Tree
from bst.tree import bcolors

class AVLTree(Tree):
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
                string += '{}{}{} [{}{}{}] ({}{}{})'.format(
                    bcolors.OKGREEN, node.value, bcolors.ENDC,
                    bcolors.OKBLUE, node.key, bcolors.ENDC,
                    bcolors.FAIL, node.balance_factor, bcolors.ENDC
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


    # type RR, RL, LL, LR
    def rotate(self, a, type):
        type = type.lower()
        if type == 'rr':
            b = a.right
            super().rotate(b, 'left')
            if b.balance_factor == -1:
                a.balance_factor = 0
                b.balance_factor = 0
            else:
                a.balance_factor = -1
                b.balance_factor = 1
        elif type == 'll':
            b = a.left
            super().rotate(b, 'right')
            if b.balance_factor == 1:
                a.balance_factor = 0
                b.balance_factor = 0
            else:
                a.balance_factor = 1
                b.balance_factor = -1
        elif type == 'rl':
            b = a.right
            c = b.left
            super().rotate(c, 'right')
            super().rotate(c, 'left')
            if c.balance_factor == -1:
                a.balance_factor = 1
            else:
                a.balance_factor = 0
            if c.balance_factor == 1:
                b.balance_factor = -1
            else:
                b.balance_factor = 0
            c.balance_factor = 0
        elif type == 'lr':
            b = a.left
            c = b.right
            super().rotate(c, 'left')
            super().rotate(c, 'right')
            if c.balance_factor == 1:
                a.balance_factor = -1
            else:
                a.balance_factor = 0
            if c.balance_factor == -1:
                b.balance_factor = 1
            else:
                b.balance_factor = 0
            c.balance_factor = 0

    def add(self, entity):
        node = None
        if isinstance(entity, AVLNode):
            node = entity
        else:
            node = AVLNode(entity)
            node.key = entity
        current = self.get_root()

        if current:
            self.nodes[node.key] = node
            while True:
                if node.key < current.value:
                    if current.left is None:
                        current.add_child(node, 'left')
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.add_child(node, 'right')
                        break
                    current = current.right

            parent = node.parent
            # FAZA 2
            # przypadek pierwszy - tylko jedno dziecko
            if parent.balance_factor != 0:
                parent.balance_factor = 0
            else:
                if parent.left == node:
                    parent.balance_factor = 1
                else:
                    parent.balance_factor = -1

                r = parent.parent
                t = False

                while r:
                    if r.balance_factor:
                        t = True
                        break
                    if r.left == parent:
                        r.balance_factor = 1
                    else:
                        r.balance_factor = -1
                    parent = r
                    r = r.parent

                if t:
                    if r.balance_factor == 1:
                        if r.right == parent:
                            r.balance_factor = 0
                        elif parent.balance_factor == -1:
                            self.rotate(r, 'lr')
                        else:
                            self.rotate(r, 'll')
                    else:
                        if r.left == parent:
                            r.balance_factor = 0
                        elif parent.balance_factor == 1:
                            self.rotate(r, 'rl')
                        else:
                            self.rotate(r, 'rr')
        else:
            # sam korzen
            self.nodes[node.key] = node






