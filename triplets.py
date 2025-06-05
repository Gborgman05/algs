class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        done = [False, False, False]
        for i in range(len(target)):
            for triplet in triplets:
                if triplet[i] == target[i] and triplet[(i+1) % len(target)] <= target[(i+1) % len(target)] and  triplet[(i+2) % len(target)] <= target[(i+2) % len(target)]:
                    done[i] = True
                    break
        return all(done)