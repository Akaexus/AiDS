def heap_sort(array):
    def fix_tree(tree, n):
        for i in range(1, n + 1)[::-1]:
            if tree[i] > tree[int((i - 1) / 2)]:
                tree[i], tree[int((i - 1) / 2)] = tree[int((i - 1) / 2)], tree[i]
        return tree
    maxIndex = len(array) - 1
    while maxIndex >= 1:
        fix_tree(array, maxIndex)
        array[0], array[maxIndex] = array[maxIndex], array[0]
        maxIndex -= 1
    return array