class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        result = 0
        mapping = {'R': 1, 'L': -1}
        for char in s:
            counter = counter + mapping[char]
            result = result + int(counter == 0)
        
        return result