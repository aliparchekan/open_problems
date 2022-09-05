class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def check_area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r,c) not in visited and grid[r][c]):
                return 0
            visited.add((r,c))
            return 1 + check_area(r + 1, c) + check_area(r - 1, c) + check_area(r, c + 1) + check_area(r, c - 1)
    
        return max(check_area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
                