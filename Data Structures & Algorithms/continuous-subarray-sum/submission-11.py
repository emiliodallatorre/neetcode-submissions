class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i, n in enumerate(nums[:-1]):
            rest_so_far: int = n % k
            print(n)
            
            for j, o in enumerate(nums[i+1:]):
                if (rest_so_far + o) % k == 0:
                    return True
                else:
                    rest_so_far = (rest_so_far + o) % k       
        
        return False