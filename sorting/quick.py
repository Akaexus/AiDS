def quick_sort(array):
    def quicc(array, start, end):
        if end - start < 2:
            return array
        else:
            pivot_index = start + int((end - start) / 2)
            array[pivot_index], array[end] = array[end], array[pivot_index]

            i = start
            j = end - 1
            while True:
                while i < j and array[i] < array[end]:
                    i += 1
                while i < j and array[j] >= array[end]:
                    j -= 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                else:
                    break

            array[j], array[end] = array[end], array[j]
            quicc(array, start, j - 1)
            quicc(array, j + 1, end)

    quicc(array, 0, len(array) - 1)
    return array

array = [3, 9, 6, 1, 4, 10, 6, 8, 4, 2]

print(quick_sort(array))