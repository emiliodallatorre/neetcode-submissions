class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lines: dict = defaultdict(int)
        result: int = 0

        for num in nums:
            if not lines[num]:
                lines[num] = lines[num - 1] + lines[num + 1] + 1
                lines[num - lines[num - 1]] = lines[num]
                lines[num + lines[num + 1]] = lines[num]

                result = max(result, lines[num])
        
        return result