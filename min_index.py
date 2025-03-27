class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l_dom = 0
        l_count= 0
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        dominant, dom_count = max(store.items(), key=lambda item: item[1])
        print(dominant, " ", dom_count)
        r_dom = dom_count
        r_count = len(nums)
        i = -1
        while r_count > 0 and ((l_count == 0 or l_dom / l_count <= .5) or r_dom / r_count <= .5):
            i += 1
            if nums[i] == dominant:
                l_dom += 1
                r_dom -= 1
            l_count += 1
            r_count -= 1
            #print(" ".join([str(l_dom), str(l_count), str(r_dom), str(r_count)]))
        if not r_count > 0:
            return -1
        else:
            return i            


