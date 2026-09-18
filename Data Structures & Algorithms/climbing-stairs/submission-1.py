class Solution:
    def climbStairs(self, n: int) -> int:
        memo: dict = {}
        
        def w(o: int) -> int:
            if o in memo:
                return memo[o]

            if o == 2:
                return 2
            if o == 1:
                return 1

            memo[o - 1] = w(o - 1)
            memo[o - 2] = w(o - 2)

            return w(o - 1) + w(o - 2)
        
        return w(n)