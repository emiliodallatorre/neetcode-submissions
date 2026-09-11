class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [[]]
        nums = sorted(nums)

        def bt(target: int, nums: list[int]) -> list[list[int]]:
            solutions: list[list[int]] = []

            if target < min(nums):
                return None
            elif target in nums:
                solutions.append([target])
            
            for i, num in enumerate(nums):
                opts: list[int] = bt(target - num, nums[i:])

                if opts is not None:
                    for opt in opts:
                        solutions.append([num, *opt])
            
            return solutions

        result = bt(target, nums)

        return result