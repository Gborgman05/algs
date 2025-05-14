class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counts = defaultdict(int)
        for char in t:
            counts[char] += 1
        
        chars_remaining = len(t)
        min_window = (0, float("inf"))
        start_index = 0

        for i, char in enumerate(s):
            if counts[char] > 0:
                chars_remaining -= 1
            counts[char] -= 1

            if chars_remaining == 0:
                while True:
                    char_start = s[start_index]
                    # what happens to the irrelevant characters
                    # they were subtracted when added into the window, so they must be < 0
                    if counts[char_start] == 0:
                        break
                    counts[char_start] += 1
                    start_index += 1

                if i - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, i)
                counts[s[start_index]] += 1
                chars_remaining += 1
                start_index += 1
        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]
            
