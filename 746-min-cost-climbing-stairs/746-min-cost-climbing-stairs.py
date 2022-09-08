class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [-1] * (len(cost) + 1)
        if len(cost) == 2:
            return min(cost)
        steps[0] = 0
        steps[1] = 0
        def calculateCost(n):
            if n == 0 or n == 1:
                return 0
            if steps[n - 1] == -1:
                steps[n - 1] = calculateCost(n - 1)
            return min(steps[n - 1] + cost[n - 1], steps[n - 2] + cost[n - 2])
        return calculateCost(len(cost))