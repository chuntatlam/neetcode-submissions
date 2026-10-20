class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCurr, rowNext = 0, len(matrix) - 1
        while rowCurr < rowNext:
            mid = (rowCurr + rowNext) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                rowNext = mid - 1
            else:
                rowCurr = mid + 1
        # target is possibly in rowCurr
        start, end = 1, len(matrix[rowCurr]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[rowCurr][mid] == target:
                return True
            if matrix[rowCurr][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False