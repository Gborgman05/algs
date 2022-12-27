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
class Solution:
    def longestPalindrome(self, s: str) -> str:
#         l_ptr = r_ptr = start = 0
        
#         longest = 0
        
#         longest_l = longest_r = 0
#         flipper = True
#         while start < len(s):
#             if s[l_ptr:r_ptr] == s[r_ptr:l_ptr:-1]:
#                 if len(s[l_ptr:r_ptr]) > longest:
#                     longest = len(s[l_ptr:r_ptr])
#                     longest_l = l_ptr
#                     longest_r = r_ptr
#             if l_ptr == 0 and r_ptr >= len(s) - 1:
#                 # we reached the end here
#                 start += 1
#                 l_ptr = r_ptr = start
#                 continue
#             if flipper and l_ptr > 0:
#                 l_ptr-= 1
#             if not flipper and r_ptr < len(s):
#                 r_ptr += 1
#             flipper = not flipper
#             # print("l ", l_ptr)
#             # print("r ", r_ptr)
#         return s[longest_l:longest_r+1]
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
    def helper(self,s,l,r):

        while 0<=l and r < len(s) and s[l]==s[r]:
            l-=1; r+=1
        return s[l+1:r] 

                
            
            
            
        
        