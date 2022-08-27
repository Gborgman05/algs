# reverses words but maintains the order of words in a sentence s
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            word = list(word)
            l = 0
            h = len(word) - 1
            while l < h:
                tmp = word[l]
                word[l] = word[h]
                word[h] = tmp
                l += 1
                h -= 1
            return "".join(word)
        return " ".join([reverse(word) for word in s.split()])