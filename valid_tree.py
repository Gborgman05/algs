class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_to_edge = {}
        for edge in edges:
            l, r = edge
            if l not in node_to_edge:
                node_to_edge[l] = [r]
            else:
                node_to_edge[l].append(r)
            if r not in node_to_edge:
                node_to_edge[r] = [l]
            else:
                node_to_edge[r].append(l)
        visited = {}
        curr = 1
        for key in node_to_edge.keys():
            curr = key
            break
        todo = [(curr, -1)]
        nxt = []
        while todo:
            # print(todo)

            curr, my_parent = todo.pop()
            if curr in visited:
                return False
            else:
                if curr in node_to_edge:
                    parent = curr
                    nxt = [(node, parent) for node in node_to_edge[curr] if node != my_parent]
            visited[curr] = 1
            todo = todo + nxt
        print("at the end)")
        return len(visited) == n

        