class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            if ((n := sum(nums[:i])) == (total - nums[i] - n)):
                return i
        return -1    
        
        