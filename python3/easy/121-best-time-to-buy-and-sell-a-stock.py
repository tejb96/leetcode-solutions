class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price=prices[0]
        max_profit=0

        for right in range(len(prices)):
            if prices[right]<buy_price:
                buy_price=prices[right]

            max_profit=max(max_profit, prices[right]-buy_price)
        
        return max_profit