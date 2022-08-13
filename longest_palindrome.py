class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        reversable = []
        best_middle = 0
        for i in range(len(words)):
            rever = words[i][::-1]
            # print(word, " ", rever)
            if words[i] == rever:
                best_middle = 2
                continue
            if rever in words and words[i] not in reversable:
                reversable.append(rever)
        return 2 * sum([len(elem) for elem in reversable]) + best_middle
        