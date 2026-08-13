class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0

        for i, p in enumerate(prices):
            cmin: int = p

            for j, q in enumerate(reversed(prices[:i])):
                if q < cmin:
                    cmin = q
                if q > p:
                    break
            
            profit = max(profit, p - cmin)

        return profit