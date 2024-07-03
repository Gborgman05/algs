class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        else:
            final = []
            for i in range(len(nums)):
                unused = nums.pop(0)
                ans = self.permute(nums)
                for a in ans:
                    a.append(unused)
                final.extend(ans)
                nums.append(unused)
            return final
            
#         def gen_combos(nums, unused):
#             for num in nums:
#                 num.append(unused)
#             return nums
        
#         def helper(arr, unused):
#             print(arr)
#             if len(arr) == 1:
#                 return gen_combos([arr], unused)
#             else:
#                 answers = []
#                 for i in range(len(nums)):
#                     tmp = arr[:]
#                     tmp.pop(i)
#                     answers.extend(helper(tmp, arr[i]))                
#                     if unused:
#                         #initial entrypoint
#                         return gen_combos(answers, unused)
#                     else:
#                         return answers
#         return helper(nums, None)
            