# O(n + m)
# n = length of nums1
# m = length of nums2
# hash table is O(1) insert and lookup
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store1 = {}
        for i in nums1:
            store1[i] = 1
        ret = []
        for j in nums2:
            if j in store1:
                ret.append(j)
                del store1[j]
        return ret