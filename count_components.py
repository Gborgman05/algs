class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class Node:
            def __init__(self, id):
                self.id = id
                self.adjacent = []
        id_to_node = {
            id:Node(id) for id in range(n)
        }
        for edge in edges:
            a, b = edge[0], edge[1]
            if a not in id_to_node[b].adjacent:
                id_to_node[b].adjacent.append(a)
            if b not in id_to_node[a].adjacent:
                id_to_node[a].adjacent.append(b)
        seen = {}
        i = 0
        components = 0
        while len(seen) < n:
            while i in seen:
                i += 1
            components += 1
            explore = [i]
            while explore:
                curr = id_to_node[explore.pop()]
                seen[curr.id] = 1
                explore += [id for id in curr.adjacent if id not in seen]
        return components
            