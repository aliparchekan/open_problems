class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (temp:= image[sr][sc]) == color:
            return image
        m = len(image)
        n = len(image[0])
        def dfs(r, c):
            if image[r][c] == temp:
                image[r][c] = color
                if r >= 1: 
                    dfs(r - 1, c)
                if r + 1 < m:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < n:
                    dfs(r, c + 1)
        dfs(sr, sc)
                
                
        
        return image