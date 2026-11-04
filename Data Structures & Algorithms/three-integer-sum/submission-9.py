from operator import itemgetter 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        sums: list[list[int]] = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            elif i > 0 and nums[i - 1] == num:
                continue
            
            j: int = i + 1
            k: int = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > -1 * num:
                    k -= 1
                elif nums[j] + nums[k] < -1 * num:
                    j += 1
                else:
                    sums.append(itemgetter(i, j, k)(nums))
                    k -= 1
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return sums

            