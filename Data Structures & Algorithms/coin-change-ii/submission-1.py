class Solution:
    def backtrack(self, remaining: int, start: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0

        key = (remaining, start)
        if key in self.memo:
            return self.memo[key]

        count = 0
        for i in range(start, len(self.coins)):
            count += self.backtrack(remaining - self.coins[i], i)

        self.memo[key] = count
        return count

    def change(self, amount: int, coins: list[int]) -> int:
        self.coins = coins
        self.memo: dict[tuple[int, int], int] = {}
        return self.backtrack(amount, 0)

