# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            middle = start + (end - start) // 2
            if isBadVersion(middle):
                end = middle - 1
            else:
                start = middle + 1
                
        return end + 1
        