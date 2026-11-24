import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list: node -> list of (neighbor, weight)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # shortest known distance from k to every node, all start at infinity
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0

        # min-heap of (current_distance, node)
        pq = [(0, k)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            # stale entry, we already found a shorter path to this node
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        answer = max(distances.values())
        return answer if answer < float('inf') else -1

        
# my plan:
# - set up a dictionary to keep track of the shortest node , start it all at infinity and at the start its going to be 0
# - i push the start node with distance 0 to the min-heap
# - while loop priority is not empty, pop the smallest node
# - for each neighbour, if i find a cheaper path through the current node, i update the distance and push the path to the heap.









# [[2, 1, 1], [2, 3, 1], [3,4,1]], n = 4, k = 2

# node 2 -> 1 unit of time to go to node 1 and node 3
# node 3 -> 4 = 1 unit of time to go there

# maximum time to reach all nodes is 2.






