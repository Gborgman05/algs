class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        build = []
        candidates.sort()
        def dfs(value, index, cur):
            if value == target:
                build.append(cur)
                return
            elif value > target:
                return
            else:
                for i in range(index, len(candidates)):
                    dfs(value + candidates[i], i, cur + [candidates[i]])
        dfs(0, 0, [])
        return build
