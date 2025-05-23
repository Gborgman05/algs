class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        curr = []

        def helper(total, combination, i):
            if target == total:
                final.append(combination[:])
                return
            elif target < total or i >= len(candidates):
                return
            
            combination.append(candidates[i])
            helper(total + candidates[i], combination, i)
            combination.pop()
            helper(total, combination, i + 1)

        
        helper(0, [], 0)
        return final
        