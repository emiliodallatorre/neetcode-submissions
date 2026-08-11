from math import ceil

class Solution:
    def evalTime(self, piles: List[int], k: int) -> int:
        return sum(ceil(x / k) for x in piles)

    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        l, h = 1, max(piles)
        sol: int = max(piles)

        while l <= h:
            p = (h - l) // 2 + l
            hrs: int = self.evalTime(piles, p)

            if hrs <= hours:
                h = p - 1
                sol = min(sol, p)
            elif hrs > hours:
                l = p + 1

        return sol

                
                
