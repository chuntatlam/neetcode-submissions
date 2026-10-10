class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = collections.defaultdict(set)
        column_hash = collections.defaultdict(set)
        box_hash = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_hash[r] or board[r][c] in column_hash[c] or board[r][c] in box_hash[(r//3,c//3)]):
                    return False
                row_hash[r].add(board[r][c])
                column_hash[c].add(board[r][c])
                box_hash[(r//3,c//3)].add(board[r][c])
        
        return True
