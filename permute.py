class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = self.permute(nums[1:])
        print(res)
        cur = nums[0]
        my_res = []
        for permute in res:
            for i in range(len(permute)):
                my_res.append(permute)
                my_res[-1].insert(i, cur)
            my_res.append(permute)
            my_res[-1].append(cur)
        return my_res
            
            
        
        
        