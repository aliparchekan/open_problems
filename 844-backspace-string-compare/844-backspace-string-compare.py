class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildString(s):
            step = 0
            result = ''
            for char in reversed(s):
                if char == '#':
                    step += 1
                    continue
                if step > 0:
                    step -= 1
                    continue
                result += char
            return result
        
        return buildString(s) == buildString(t)
                    
                