class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
    
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        # Find all treasure chests and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # Process all cells level by level
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # If the neighbor is within bounds and is an empty land cell
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
