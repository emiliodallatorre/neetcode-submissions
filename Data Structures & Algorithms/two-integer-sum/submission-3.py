class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            difference: int = target - num

            if difference in nums:
                if difference != num or nums.index(difference) < i:
                    return [min(i, nums.index(difference)), max(i, nums.index(difference))]
                
