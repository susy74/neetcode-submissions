class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (right + left) // 2
            x = matrix[mid // n][mid % n]
            if target > x:
                left = mid + 1 
            elif target == x:
                return True
            else:
                right = mid - 1
        return False
        