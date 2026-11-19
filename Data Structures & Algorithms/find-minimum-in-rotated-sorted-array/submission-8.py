class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        def get_m(l, r):
            return (r - l) // 2 + l

        while l < r - 1:
            if nums[l] >= nums[get_m(l, r)]:
                r = get_m(l, r)
            elif nums[get_m(l, r)] >= nums[r]:
                l = get_m(l, r)
            else:
                r = l

        return nums[r]