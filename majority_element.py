class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        this = {}
        for i in range(len(nums)):
            if nums[i] not in this:
                this[nums[i]] = 1
            else:
                this[nums[i]] += 1
            # if i > len(nums) // 2 - 1:
                # print(nums[i])
                # print(this[nums[i]])
                # print(len(nums) // 2)
                # if this[nums[i]] > len(nums) // 2:
                    # return nums[i]
        return max(this, key=this.get)