class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)

        def bt(target: int, nums: list[int]) -> list[list[int]]:
            solutions: list[list[int]] = []

            if target < min(nums):
                return None
            elif target in nums:
                solutions.append([target])
            
            for i, num in enumerate(nums[:len(nums)-1]):
                if nums[i] == nums[i-1] and i:
                    continue

                opts: list[int] = bt(target - num, nums[i+1:])

                if opts is not None:
                    for opt in opts:
                        solutions.append([num, *opt])
            
            return solutions

        result = bt(target, nums)
        if result is None:
            result = []

        return result