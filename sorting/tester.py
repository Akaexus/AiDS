import random
import time
from sorting.insertion import insertion_sort
from sorting.bubble import bubble_sort
from sorting.selection import selection_sort

MAX_VALUE = 2**31
MIN_VALUE = 0


multipliers = [1, 2, 3, 4, 5]
tens = [0, 1, 2, 3, 4]
sizes = []
for ten in tens:
    for multiplier in multipliers:
        sizes.append(multiplier*(10**ten))

max_array = []
for i in range(0, sizes[-1]):
    max_array.append(random.randint(MIN_VALUE, MAX_VALUE))

sorting_algorithms = {
    'insertion_sort': insertion_sort,
    'bubble_sort': bubble_sort,
    'selection_sort': selection_sort,
}
results = {}
for algorithm in sorting_algorithms:
    print('Benchmarking algorithm {}'.format(algorithm))
    results[algorithm] = {}
    f = sorting_algorithms[algorithm]
    for size in sizes:
        print('\t array size {}: '.format(size), end='')
        array = max_array[0:size]
        start_time = int(time.time()*1000)
        f(array)
        end_time = int(time.time()*1000)
        elapsed_time = end_time - start_time
        print('{}s'.format(elapsed_time/1000))
        results[algorithm][size] = elapsed_time



