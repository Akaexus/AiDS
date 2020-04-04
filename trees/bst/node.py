class Node:
    parent = None,
    left = None,
    right = None,
    key = None,
    value = None,

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left if left != 0 else None
        self.right = right if right != 0 else None

    def __str__(self):
        return str({
            'self': id(self),
            'value': self.value,
            'key': self.key,
            'parent': id(self.parent) if self.parent is not None else None,
            'left': id(self.left),
            'right': id(self.right),

        })

    def isvisited(self):
        return hasattr(self, 'visited')

    def __repr__(self):
        return self.__str__()

    def get_parent_side(self):
        if self.parent.left == self:
            return 'left'
        elif self.parent.right == self:
            return 'right'
        else:
            return None
