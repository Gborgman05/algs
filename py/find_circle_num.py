class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen =[]
        def dfs(city, i):
            if i in seen:
                return
            seen.append(i)
            for j in range(len(city)):
                if i == j:
                    pass
                elif city[j] == 1:
                    dfs(isConnected[j], j)
                    
        access = []
        for i  in range(len(isConnected)):
            dfs(isConnected[i], i)
            access.append(seen)
            seen = []
        i = []
        for elem in access:
            if set(elem) in i:
                pass
            else:
                i.append(set(elem))
        return len(i)
            