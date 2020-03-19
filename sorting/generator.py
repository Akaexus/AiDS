import random

class Generator:
    array_types = [
        'random',
        'increasing',
        'decreasing',
        'v_shaped',
        'a_shaped',
    ]

    INT_MIN = 0
    INT_MAX = 2**20

    @staticmethod
    def random(size):
        array = [0] * size
        for i in range(0, size):
            array[i] = random.randint(Generator.INT_MIN, Generator.INT_MAX)
        return array

    @staticmethod
    def increasing(size, start=0):
        step = random.randint(1, 25)
        return list(range(start, size * step, step))

    @staticmethod
    def decreasing(size, start=0):
        step = random.randint(1, 25)
        return list(range(0, size * step, step))[::-1]

    @staticmethod
    def a_shaped(size):
        half = int(size / 2)
        increasing = Generator.increasing(half)
        decreasing = Generator.decreasing(half, increasing[-1])
        return increasing + decreasing

    @staticmethod
    def v_shaped(size):
        half = int(size / 2)
        decreasing = Generator.decreasing(half)
        increasing = Generator.increasing(half, decreasing[-1])
        return decreasing + increasing
