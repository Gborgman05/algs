class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        class my_sorted:
            def __init__(self):
                self.arr = []
            def push(self, item):
                if item in self.arr:
                    pass
                else:
                    if len(self.arr) < 3:
                        self.arr.append(item)
                        self.arr = sorted(self.arr, reverse=True)
                    elif self.arr[-1] < item:
                        self.arr.append(item)
                        self.arr = sorted(self.arr, reverse=True)
                    else:
                        pass
                    if len(self.arr) > 3:
                        self.arr.pop()
                print(self.arr)
        sorter = my_sorted()
        i  = 0
        while i  < len(nums):
            sorter.push(nums[i])
            i += 1
        if len(sorter.arr) == 3:
            return sorter.arr[-1]
        else:
            return sorter.arr[0]