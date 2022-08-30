class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while( start <= end):
            sumed =  numbers[start] + numbers[end]
            if sumed == target:
                return [start + 1, end + 1]
            if sumed > target:
                end = end - 1
            else:
                start = start + 1
        