from typing import Optional
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squs[(i // 3, j // 3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squs[(i // 3, j // 3)].add(board[i][j])
        
        return True

s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))