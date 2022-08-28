class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        n = 0
        for i in range(len(nums)):
            if (n == (total - nums[i] - n)):
                return i
            n += nums[i]
        return -1    
        
        