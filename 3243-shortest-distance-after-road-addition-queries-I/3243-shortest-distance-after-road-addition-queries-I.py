class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0,0))
            visited_node = set()
            visited_node.add((0,0))

            while q:
                current_node, length = q.popleft()
                if current_node == n-1:
                    return length
                
                for neighbour in adj[current_node]:
                    if neighbour not in visited_node:
                        visited_node.add(neighbour)
                        q.append((neighbour, length + 1))
                        

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res
        