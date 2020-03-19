import math


class Sorter:
    algorithm_names = [
        'bubble_sort',
        'counting_sort',
        'heap_sort',
        'insertion_sort',
        'merge_sort',
        'selection_sort',
        'shell_sort',
        'quick_sort',
    ]

    @staticmethod
    def bubble_sort(array, verbose=False, debug=False):
        array_size = len(array)
        for i in range(0, array_size):
            for j in range(0, array_size - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def counting_sort(array, verbose=False, debug=False):
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

    @staticmethod
    def heap_sort(array, verbose=False, debug=False):
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

    @staticmethod
    def insertion_sort(array, verbose=False, debug=False):
        for pivot in range(0, len(array)):
            for i in range(0, pivot)[::-1]:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                else:
                    break
        return array

    @staticmethod
    def merge_sort(array, verbose=False, debug=False):
        def divide(array, start, end):
            if end - start <= 1:
                return array
            pivot = int((end - start) / 2) + start
            divide(array, start, pivot)
            divide(array, pivot, end)
            left = array[start:pivot]
            right = array[pivot:end]
            left_max = pivot - start - 1
            right_max = end - pivot - 1
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

    @staticmethod
    def quick_sort(array, verbose=False, debug=False):
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

    @staticmethod
    def selection_sort(array, verbose=False, debug=False):
        array_size = len(array)
        for pivot in range(0, array_size):
            min_element_index = pivot
            for i in range(pivot, array_size):
                if array[min_element_index] > array[i]:
                    min_element_index = i
            array[min_element_index], array[pivot] = array[pivot], array[min_element_index]
        return array

    @staticmethod
    def shell_sort(array, verbose=False, debug=False):
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