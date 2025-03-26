class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # check possible
        rem = None
        total = 0
        count = 0
        nums = []
        for row in grid:
            for num in row:
                if rem is not None:
                    if num % x != rem:
                        return -1
                else:
                    rem = num % x
                count += 1
                total += num
                nums.append(num)
        avg = self.round_to_multiple(total / count, x)
        nums = sorted(nums)
        furthest = 0
        ops = 0
        while True:
            if abs(avg - nums[0]) < abs(nums[-1] - avg):
                futhest = len(nums) - 1
            if nums[furthest] > avg:
                while nums[furthest] > avg:
                    nums[furthest] -= x
                    ops += 1
            elif nums[furthest] < avg:
                while nums[furthest] < avg:
                    nums[furthest] += x
                    ops += 1
            else:
                return ops
            print(nums)
            avg = self.round_to_multiple(sum(nums) / len(nums), x)
    def round_to_multiple(self, to_round, x):
        return round(to_round / x) * x

        

