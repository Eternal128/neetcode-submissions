class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set() # visited set, so we do count any visited cell twice
        max_area = 0

        def get_area(r: int, c: int): # helper function to explore the islands using DFS
            # check if its out of bound or already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r, c)) #mark that this land is visited
            
            area = 1
            area += get_area(r + 1, c) # right
            area += get_area(r - 1, c) # left
            area += get_area(r, c + 1) # top
            area += get_area(r, c - 1) # down

            return area
        
        
        for r in range(rows):
            for c in range(cols):
                # if we find land and it not visited yet
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = get_area(r, c)
                    max_area = max(max_area, current_area)
        
        return max_area















