class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len([n for n in nums if n < num]) for num in nums ]

            