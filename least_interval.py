class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = {}
        counts = 0
        max_count = 0
        for task in tasks:
            counts += 1
            if task in store:
                store[task] += 1
            else:
                store[task] = 1
            if store[task] > max_count:
                max_count += 1
        num_max = sum(1 for a in store.values() if a == max_count)
        return max(counts, (max_count-1) * (n + 1) + num_max)


        