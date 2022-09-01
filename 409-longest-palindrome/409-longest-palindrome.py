class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired = set()
        pairs = 0
        for char in s:
            if char in unpaired:
                pairs += 1
                unpaired.remove(char)
            else:
                unpaired.add(char)
            
        return 2*pairs + int(len(unpaired) > 0)
        