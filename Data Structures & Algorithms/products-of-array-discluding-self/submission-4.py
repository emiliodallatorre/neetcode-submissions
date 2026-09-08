class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes: list[int] = []
        suffixes: list[int] = []

        for i in range(len(nums)):
            if not prefixes:
                prefixes.append(nums[i])
            else:
                prefixes.append(nums[i] * prefixes[-1])
            
            if not suffixes:
                suffixes.append(nums[-1-i])
            else:
                suffixes.append(nums[-1-i] * suffixes[-1])

        suffixes = list(reversed(suffixes))

        solution: list[int] = []

        for i in range(len(nums)):
            value: int = 1
            
            if i > 0:
                value *= prefixes[i-1]
            if i < len(nums) - 1:
                value *= suffixes[i+1]

            solution.append(value)

        return solution