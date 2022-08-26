class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = None
        for char in s:
            if char == 'I':
                result = result + 1
                prev = 'I'
            elif char == 'V':
                if prev == 'I':
                    result = result + 3
                else:
                    result = result + 5
                prev = 'V'
            elif char == 'X':
                if prev == 'I':
                    result = result + 8
                else:
                    result = result + 10
                prev = 'X'
            elif char == 'L':
                if prev == 'X':
                    result = result + 30
                else:
                    result = result + 50
                prev = 'L'
            elif char == 'C':
                if prev == 'X':
                    result = result + 80
                else:
                    result = result + 100
                prev = 'C'
            elif char == 'D':
                if prev == 'C':
                    result = result + 300
                else:
                    result = result + 500
            elif char == 'M':
                if prev == 'C':
                    result = result + 800
                else:
                    result = result + 1000
        return result
        