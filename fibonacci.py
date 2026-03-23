class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")

        self.n = n
        self.current = 0
        self.next_val = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration

        if self.count > self.n:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return 0

        if self.count == 1:
            self.count += 1
            return 1

        value = self.current + self.next_val
        self.current = self.next_val
        self.next_val = value
        self.count += 1
        return value
