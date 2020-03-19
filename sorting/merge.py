

def merge_sort(array):
    def divide(array, start, end):
        if end - start <= 1:
            return array
        pivot = int((end - start) / 2) + start
        divide(array, start, pivot)
        divide(array, pivot, end)
        left = array[start:pivot]
        right = array[pivot:end]
        left_max = pivot - start -1
        right_max = end - pivot -1
        left_counter = 0
        right_counter = 0
        for i in range(start, end):
            if left_counter > left_max:
                array[i] = right[right_counter]
                right_counter += 1
            elif right_counter > right_max:
                array[i] = left[left_counter]
                left_counter += 1
            else:
                if left[left_counter] < right[right_counter]:
                    array[i] = left[left_counter]
                    left_counter += 1
                else:
                    array[i] = right[right_counter]
                    right_counter += 1
    divide(array, 0, len(array))
    return array