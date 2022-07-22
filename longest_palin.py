class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counts = {}
        for char in s:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
        counts = letter_counts.values()
        odd = False
        total = 0
        for count in counts:
            total += (count // 2) * 2
            if count % 2 == 1:
                odd = True
        if odd:
            total += 1
        return total