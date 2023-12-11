from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =  0
        buy_i, sell_i = 0, 0

        while sell_i < len(prices):
            if sell_i <= buy_i:
                sell_i += 1
                continue
            elif prices[sell_i] < prices[buy_i]:
                buy_i = sell_i

            # this is slightly faster than max?
            current_proft = prices[sell_i] - prices[buy_i]
            if current_proft > max_profit:
                max_profit = current_proft
            # max_profit = max(max_profit, prices[sell_i] - prices[buy_i])
                
            sell_i += 1

        return max_profit
        # O(n^2) solution
        # while i < len(prices):
        #     buy_price = prices[i]
        #     j = i + 1
        #     while j < len(prices):
        #         current_profit = prices[j] - buy_price
        #         if current_profit > max_profit:
        #             # print(f"new max profit: prices: {prices[j]} - {buy_price} = {current_profit}")
        #             max_profit = current_profit
        #         j += 1
        #     i += 1
        # return max_profit

# prices = [7,1,5,3,6,4]
# print(Solution.maxProfit(Solution, prices))
# print(prices)