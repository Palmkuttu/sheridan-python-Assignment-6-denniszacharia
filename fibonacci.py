class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError

        self.n = n
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.n:
            raise StopIteration

        if self.index == 0:
            self.index += 1
            return 0

        if self.index == 1:
            self.index += 1
            return 1

        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return self.b
