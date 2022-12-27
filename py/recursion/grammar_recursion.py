class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n):
            if k == 1:
                return 0
            else:
                val = helper((k + 1) // 2)
                if k % 2 == 0:
                    if val == 0:
                        return 1
                    return 0
                return val
        return helper(n)
                
        
        # counter = 1
        # while counter < n:
        #     stri = ""
        #     for char in last:
        #         if char == "0":
        #             stri += "01"
        #         else:
        #             stri += "10"
        #     last = stri
        #     counter += 1
        # return last[k-1]