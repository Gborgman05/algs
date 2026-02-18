class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        start = 0
        while end < len(numbers):
            while numbers[end] + numbers[start] > target:
                end -= 1
            while numbers[end] + numbers[start] < target:
                start += 1
            if numbers[end] + numbers[start] == target:
                return [start+1, end+1]


