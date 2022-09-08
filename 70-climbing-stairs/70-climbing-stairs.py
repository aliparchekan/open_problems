class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        steps = [-1] * (n + 1)
        steps[0] = 1
        steps[1] = 1
        def count_ways(n):
            if n == 0:
                return 1
            if steps[n - 1] == -1:
                steps[n - 1] = count_ways(n - 1)
            return steps[n - 1] + steps[n - 2]
        return count_ways(n)
            
            
        