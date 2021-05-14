from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        buyingPrice : int = prices[0]
        profit : int = 0
        for price in prices:
            if price > buyingPrice:
                profit = max(price - buyingPrice, profit)
            else:
                buyingPrice = price
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))