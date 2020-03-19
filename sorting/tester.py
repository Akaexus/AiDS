# coding: utf8
import time
from sorting.sorter import Sorter
from sorting.generator import Generator
powers = [1, 2, 3, 4, 5]  # 10**x
multipliers = [1, 2, 3, 4, 5, 7]
ROUNDS = 10

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

array_types = [
    'random',
    'increasing',
    'decreasing',
    'v_shaped',
    'a_shaped',
]

print('Wprowadź ciąg liczb oddzielony spacjami:')
userArray = [int(x) for x in input().split()]

results = {}

algorithms = {}
for name in algorithm_names:
    algorithms[name] = getattr(Sorter, name)
    results[name] = {}
    for array_type in array_types:
        results[name][array_type] = {}
print(results)
for round in range(0, ROUNDS):
    for power in powers:
        for multiplier in multipliers:
            size = multiplier * 10 ** power
            for array_type in array_types:
                print('[#{}] Size: {}\tType: {}'.format(round, size, array_type))
                array = getattr(Generator, array_type)(size)
                for algorithm_name in algorithms:
                    if size not in results[algorithm_name][array_type]:
                        results[algorithm_name][array_type] = {
                            'time': [],
                            'comparisons': [],
                            'swaps': []
                        }
                    f = algorithms[algorithm_name]
                    # print('[#{}] Sorting {} array at size {} using {}'.format(round, array_type, size, algorithm_name))

                    f(array)



