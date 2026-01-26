class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        store = {0: 1}
        for num in nums:
            new_store = {}
            for key in store:
                if key + num in new_store:
                    new_store[key + num] += store[key]
                else:
                    new_store[key + num] = store[key]
                if key - num in new_store:
                    new_store[key - num] += store[key]
                else:
                    new_store[key - num] = store[key]
            store = new_store
        # print(store)
        if target not in store:
            return 0
        return store[target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        lets try naive first where we try every possible + - for each 
        this is like O(2^n) where n is the length of nums
        this is because you double the size of the can_make array
        for each new number you add. 
        """
        can_make = [0]
        for num in nums:
            new_can_make = []
            for make_num in can_make:
                new_can_make.append(make_num-num)
                new_can_make.append(make_num+num)
            can_make = new_can_make
        return len([1 for num in can_make if num==target])
        