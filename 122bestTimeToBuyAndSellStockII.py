from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits =  0
        buy_i, sell_i = 0, 1

        while sell_i < len(prices):
            profit = prices[sell_i] - prices[buy_i]
            profits += profit if profit > 0 else 0
            buy_i += 1
            sell_i += 1

        return profits
        

# prices = [7,1,5,3,6,4]
# print(Solution.maxProfit(Solution, prices))
# prices = [1,2,3,4,5]
# print(Solution.maxProfit(Solution, prices))

# print(prices)