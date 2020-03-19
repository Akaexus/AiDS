import math


def shell_sort(array):
    size = len(array)
    # knuth
    k = int(math.log(2 * size / 3 + 1, 3))
    # k = int(size/2)-
    while k >= 1:
        for offset in range(0, k):
            # insertion sort
            for pivot in range(offset, size, k):
                for i in range(offset, pivot, k)[::-1]:
                    if array[i] > array[i + k]:
                        array[i], array[i + k] = array[i + k], array[i]
                    else:
                        break
        k = int(k / 2)
    return array