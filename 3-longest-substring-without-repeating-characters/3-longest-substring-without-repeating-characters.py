class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        table = {}
        left = 0
        right = 0
        result = 0
        while(right < len(s)):
            if s[right] in table:
                left = max(left, table[s[right]] + 1)
                
            table[s[right]] = right
                
            result = max(result, right - left + 1)
            
            right = right + 1
                
        return result
                
            
        