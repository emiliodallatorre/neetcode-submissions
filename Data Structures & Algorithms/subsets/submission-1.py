class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
 
        def bt(idx: int, partial: list[int]):
            if idx == len(nums):
                res.append(partial)
                return
 
            bt(idx + 1, partial)
            bt(idx + 1, partial + [nums[idx]])
 
        bt(0, [])
        return res