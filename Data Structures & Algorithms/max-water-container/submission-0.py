class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i: int = 0
        j: int = len(heights) - 1

        max_i: int = heights[i]
        max_j: int = heights[j]

        pool: int = 0

        max_area: int = min(max_i, max_j) * (j - i)

        while i < j:
            if max_i < max_j:
                i += 1
                max_i = max(max_i, heights[i])

                max_area: int = max(max_area, min(max_i, max_j) * (j - i))
            if max_i >= max_j:
                j -= 1
                max_j = max(max_j, heights[j])

                max_area: int = max(max_area, min(max_i, max_j) * (j - i))

        return max_area

