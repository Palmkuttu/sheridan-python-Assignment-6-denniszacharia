class Fibonacci:
    def __init__(self, n):
        # Validate input
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")

        self.n = n
        self.current = 0
        self.next_val = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Handle negative case
        if self.n < 0:
            raise StopIteration

        # Stop when done
        if self.count > self.n:
            raise StopIteration

        # First value
        if self.count == 0:
            self.count += 1
            return 0

        # Second value
        elif self.count == 1:
            self.count += 1
            return 1

        # Fibonacci logic
        else:
            value = self.current + self.next_val
            self.current = self.next_val
            self.next_val = value
            self.count += 1
            return value
