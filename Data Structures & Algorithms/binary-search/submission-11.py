class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            pointer: int = (h - l) // 2 + l

            if nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                l = pointer + 1
            elif nums[pointer] > target:
                h = pointer - 1

        return -1
