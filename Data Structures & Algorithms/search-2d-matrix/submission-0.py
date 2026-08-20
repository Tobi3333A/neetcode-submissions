class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        m = len(matrix)
        n = len(matrix[0])
        ind = 0

        while left < right:
            mid = (left + right)//2
            if target > matrix[mid][n-1]:
                left = mid + 1
            else:
                right = mid
            if left == right:
                ind = left
                break
        
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if target > matrix[ind][mid]:
                left = mid + 1
            elif target < matrix[ind][mid]:
                right = mid - 1
            else:
                return True

        return False