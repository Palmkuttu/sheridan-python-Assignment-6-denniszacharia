class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")

        self.n = n
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        # Stop condition
        if self.n < 0:
            raise StopIteration

        if self.index > self.n:
            raise StopIteration

        # First value
        if self.index == 0:
            self.index += 1
            return 0

        # Second value
        if self.index == 1:
            self.index += 1
            return 1

        # Fibonacci calculation
        value = self.a + self.b
        self.a = self.b
        self.b = value

        self.index += 1
        return value
