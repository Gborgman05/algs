# common problem variant, the input array is sorted 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers traverse from others
        start = 0
        end = len(numbers) - 1
        while start < end:
            summ = numbers[start] + numbers[end] 
            if summ > target:
                end -= 1
            elif summ < target:
                start += 1
            else:
                return [start+1, end+1]