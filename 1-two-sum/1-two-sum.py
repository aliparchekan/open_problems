class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[target - nums[i]] = i
        for i in range(len(nums)):
            if (n:=table.get(nums[i])) != None and n != i:
                return [i, n]
        
        
        