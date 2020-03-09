def insertion_sort(array):
    for pivot in range(0, len(array)):
        for i in range(0, pivot)[::-1]:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            else:
                break
    return array
