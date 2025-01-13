class Solution:
    def minimumLength(self, s: str) -> int:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] +=1
        final_sum = 0
        print(counts)
        for value  in counts.values():
            # final_sum += value % 3
            # print(value)
            while value > 2:
                value -= 2
            final_sum += value
        return final_sum
            