class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLocation(nums, target, left):
            start = 0
            end = len(nums) - 1
            location = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                    continue
                elif nums[mid] > target:
                    end = mid - 1
                    continue
                else:
                    location = mid
                    if left:
                        start = location + 1
                    else:
                        end = location - 1
                        
            return location
        
        return [findLocation(nums, target, False), findLocation(nums, target, True)]