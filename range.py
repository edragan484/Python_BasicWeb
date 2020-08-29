from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x))          # next(x) ~ x.__next__() x -- iterator
print(next(x))
print(next(x))
print(next(x))


