# beats 83%, beats 5%
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start = None
        for i in range(len(nums)):
            if start is None:
                start = nums[i]
            elif not( nums[i] == nums[i-1] + 1):
                ranges.append([start, nums[i-1]])
                start = nums[i]
        if start is not None and nums[-1] == start:
            ranges.append([start])
        elif len(nums) > 1 and start is not None and nums[-1] == nums[-2] + 1:
            ranges.append([start, nums[-1]])
        def convert(r):
            if len(r) > 1 and r[0] != r[1]:
                return f"{r[0]}->{r[1]}"
            else:
                return str(r[0])
        return [convert(r) for r in ranges]            