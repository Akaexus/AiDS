def counting_sort(array):
    array_size = len(array)
    max_element = array[0]
    for i in range(1, array_size):
        if array[i] > max_element:
            max_element = array[i]
    count_array = [0] * (max_element + 1)
    for i in range(0, array_size):
        count_array[array[i]] += 1

    occurences_before = [0] * (max_element + 1)
    occurences_before[0] = count_array[0]
    for i in range(1, max_element + 1):
        occurences_before[i] = occurences_before[i - 1] + count_array[i]

    final_array = [0] * array_size
    for i in range(0, len(array))[::-1]:
        final_array[occurences_before[array[i]] - 1] = array[i]
        occurences_before[array[i]] -= 1
    return final_array
