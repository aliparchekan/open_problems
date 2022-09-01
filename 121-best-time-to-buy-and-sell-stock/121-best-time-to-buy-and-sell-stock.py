import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = 0
        sell = 1
        max_revenue = 0
        while sell < len(prices):
            current_revenue = prices[sell] - prices[buy]
            if current_revenue <= 0:
                buy = sell
            else:
                max_revenue = max(max_revenue, current_revenue)
            sell += 1
        return max_revenue
            