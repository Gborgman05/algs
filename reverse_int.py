    def reverse(self, x: int) -> int:
        final = 0
        while x != 0:
            dig = x % 10
            final *= 10
            final += dig
            x = x // 10
        return final
