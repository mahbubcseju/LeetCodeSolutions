class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        price, res = prices[0], 0
        for j in range(1, len(prices)):
            res = max(prices[j]-price, res)
            price = min(price, prices[j])
        return res