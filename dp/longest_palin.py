class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        # def check_palindrome(s):
        #     for i in range(len(s) // 2):
        #         if s[i] == s[-i-1]:
        #             continue
        #         else:
        #             return False
        #     return True
        # longest = None
        # while start < len(s) and end < len(s):
        #     if check_palindrome(s[start:end]):
        #         if not longest or len(longest) < len(s[start:end]):
        #             longest = s[start:end]
        #         end += 1
        #     else:
        #         start += 1
        # return longest
        table = [len(s) * [0]] * len(s)
        for i in range(len(table)):
            table[i][i] = 1
        print(table)
            
        