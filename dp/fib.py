class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            counter = 1
            other = 0
            last = 1
            while counter < n:
                new = other + last
                counter += 1
                other = last
                last = new
            return new
        