class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i, n in enumerate(nums[:-1]):
            rest_so_far: int = n % k
            
            for j, o in enumerate(nums[i+1:]):
                rest_so_far = (rest_so_far + o) % k
                if not rest_so_far:
                    return True
        
        return False