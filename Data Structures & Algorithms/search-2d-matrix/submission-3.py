class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        target_row = -1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                target_row = row
                break

        if target_row == -1:
            return False

        l, r = 0, len(matrix[target_row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[target_row][mid]:
                return True
            if target < matrix[target_row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False