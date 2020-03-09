def bubble_sort(array):
    array_size = len(array)
    for i in range(0, array_size):
        for j in range(0, array_size - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]