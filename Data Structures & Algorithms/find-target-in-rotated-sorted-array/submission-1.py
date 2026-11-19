class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1

        def get_m(l: int, r: int) -> int:
            return (r - l) // 2 + l

        while l < r - 1:
            # cases: l m r = binary; m 
            if nums[l] > nums[get_m(l, r)] and target >= nums[l]:
                r = get_m(l, r)
            elif nums[r] < nums[get_m(l, r)] and target <= nums[r]:
                l = get_m(l, r)
            else:
                if target > nums[get_m(l, r)]:
                    l = get_m(l, r)
                else:
                    r = get_m(l, r)

        if nums[r] != target:
            if nums[l] == target:
                return l
            return -1
            
        return r


