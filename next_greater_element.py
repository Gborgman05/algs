class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        final = []
        for i in range(len(nums2)):
            store[nums2[i]] = i
        for i in range(len(nums1)):
            final.append(-1)
            for j in range(store[nums1[i]], len(nums2)):
                if nums1[i] < nums2[j]:
                    final[-1] = nums2[j]
                    break
        return final

                