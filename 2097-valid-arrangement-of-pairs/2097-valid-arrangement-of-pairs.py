
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1 
            in_degree[end] +=1


        
        # Step 2: Find the starting node for the Eulerian path
        starting_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                starting_node = node
                break
        
        # Step 3: Hierholzer's algorithm to find the Eulerian path
        stack = [starting_node]
        result = []

        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)

            result.append(stack.pop())



        # Step 4: Format the result in reverse order
        pairs = []
        result.reverse()
        for i in range(len(result)-1):
            pairs.append([result[i], result[i+1]])
        return pairs





# class Solution:
#     def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#         # Step 1: Build the graph and degree counts
#         graph = defaultdict(deque)  # Adjacency list using deque for efficient pops
#         in_degree = defaultdict(int)
#         out_degree = defaultdict(int)

#         for u, v in pairs:
#             graph[u].append(v)  # Add edge u → v
#             out_degree[u] += 1  # Increase out-degree of u
#             in_degree[v] += 1   # Increase in-degree of v

#         # Step 2: Find the starting node
#         start = pairs[0][0]  # Default start (any node)
#         for node in graph:
#             if out_degree[node] - in_degree[node] == 1:
#                 start = node  # Start from the special node
#                 break

#         # Step 3: Hierholzer's Algorithm to find the Eulerian path
#         result = []
#         def dfs(node):
#             while graph[node]:
#                 next_node = graph[node].popleft()  # Remove edge node → next_node
#                 dfs(next_node)  # Recur on next_node
#             result.append(node)  # Append the node to the result

#         dfs(start)
#         return [[result[i], result[i + 1]] for i in range(len(result) - 1)]  # Convert path to pairs