class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        middle = begin + (end - begin) // 2
        while(begin <= end):
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                begin = middle + 1
            else:
                end = middle - 1
            middle = begin + (end - begin) // 2
        
        return -1
        
        