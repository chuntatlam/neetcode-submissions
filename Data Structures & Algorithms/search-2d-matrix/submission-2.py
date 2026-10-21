class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            target_row = (top + bot) // 2
            if matrix[target_row][0] > target:
                bot = target_row - 1
            elif matrix[target_row][-1] < target:
                top = target_row + 1
            else:
                break
        if not (top <= bot):
            return False
        start, end = 0, len(matrix[target_row]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False