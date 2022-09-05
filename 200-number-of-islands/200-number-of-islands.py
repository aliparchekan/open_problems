class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        result = 0
        def checkLand(r, c):
            if not ((r,c) not in visited and 0<= r <m and 0<= c < n and  grid[r][c] == '1'):
                return
            visited.add((r,c))
            checkLand(r + 1, c)
            checkLand(r - 1, c)
            checkLand(r, c + 1)
            checkLand(r, c - 1)
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == '1':
                    result += 1
                    checkLand(r,c)
        
        return result
                