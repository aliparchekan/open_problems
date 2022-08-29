class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        position = 0
        for char in s:
            n = t.find(char, position)
            if n == -1:
                return False
            position = n + 1
        
        return True
            