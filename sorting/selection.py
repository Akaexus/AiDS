def selection_sort(array):
    array_size = len(array)
    for pivot in range(0, array_size):
        min_element_index = pivot
        for i in range(pivot, array_size):
            if array[min_element_index] > array[i]:
                min_element_index = i
        array[min_element_index], array[pivot] = array[pivot], array[min_element_index]
    return array