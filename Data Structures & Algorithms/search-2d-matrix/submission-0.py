class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        l: int = 0
        h: int = rows * cols - 1

        while l <= h:
            p: int = (h - l) // 2 + l
            pd: int = matrix[p // cols][p % cols]

            if pd == target:
                return True
            elif pd < target:
                l = p + 1
            elif pd > target:
                h = p - 1

        return False