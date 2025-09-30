class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        highest_freq = 0
        for num in nums:
            counts[num] += 1
            if counts[num] > highest_freq:
                highest_freq = counts[num]
        total_count = 0
        for freq in counts.values():
            if freq == highest_freq:
                total_count += freq
        return total_count

