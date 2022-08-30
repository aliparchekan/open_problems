class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[lastNonZero] = nums[current]
                lastNonZero += 1
        
        for current in range(lastNonZero, len(nums)):
            nums[current] = 0
            
            
                
        