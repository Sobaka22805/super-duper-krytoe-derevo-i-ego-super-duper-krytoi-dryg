print('Lesson 7: Iterators, Closure function')


class Counter:
    limit: int
    index: int
    step_iteration: int

    def __init__(self, limit: int, step_iteration: int):
        self.index = 0
        self.limit = limit
        self.step_iteration = step_iteration

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += self.step_iteration
        if self.index > self.limit:
            raise StopIteration
        return self.index


numbers = ['one', 'two', 3, 4, 'five', 'c++', 'c#']
counter = Counter(len(numbers), 2)

try:
    for i in counter:
        print(numbers[i])
except Exception as e:
    print('Catch some error', e.__str__())
