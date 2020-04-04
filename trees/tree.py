from bst.tree import Tree

# data = {}
#
# for i in range(int(input())):
#     data[i] = ([int(x) for x in input().split()])
# print(data)

string_data = '''
5 1 2
2 3 4
7 5 6
3 7 8
8 9 0
9 0 10
1 0 11
6 0 0
5 0 0
3 0 0
0 0 0
2 0 0
'''
data = {}
i = 0
for line in string_data.split('\n'):
    if line:
        data[i] = [int(x) for x in line.split()]
        i += 1
# print(data)
# tree = Tree.build_from_data(data)
# print(tree)

tree = Tree.build_random(10)
print(tree)
tree.delete_node(int(input()))
print(tree)