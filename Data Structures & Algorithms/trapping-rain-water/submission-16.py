class Solution:
    def trap(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1

        i_max = height[i]
        j_max = height[j]

        storage: int = 0

        while i < j:
            if i_max < j_max:
                i += 1
                i_max = max(i_max, height[i])
                storage += i_max - height[i]
            else:
                j -= 1
                j_max = max(j_max, height[j])
                storage += j_max - height[j]

        return storage
