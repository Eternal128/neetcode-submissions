class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for dr, dc in [(0,1), (-1,0), (1,0), (0,-1)]:
                next_r, next_c = r + dr, c + dc

                if 0 <= next_r < rows and 0 <= next_c < cols and (next_r, next_c) not in reachable:
                    if heights[next_r][next_c] >= heights[r][c]:
                        dfs(next_r, next_c, reachable)
                    

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)
        
        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols - 1, atlantic_reachable)
        
        return list(atlantic_reachable & pacific_reachable)
                








    # [1, 2, 2]
    # [2, 3, 2]
    # [2, 4, 3]

    
#     [(0, 0)]. visited: {(0, 0)}. 


# Edge case 1:
# [[1]]
# [[0, 0]]

# edge case 2:
# [[1, 2, 3]]
# [[0, 2]]

# edge case 3:
# [] 
# []

# i am going to use DFS to start backward.



