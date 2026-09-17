class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = [set() for i in range(9)]
        seen3x3 = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            seen_row = set()
            for j in range(9):
                # Row Check
                if board[i][j] not in seen_row and board[i][j].isdigit():
                    seen_row.add(board[i][j])
                elif board[i][j] in seen_row and board[i][j].isdigit():
                    return False
                
                #Col Check
                if board[i][j] not in seen_col[j] and board[i][j].isdigit():
                    seen_col[j].add(board[i][j])
                elif board[i][j] in seen_col[j] and board[i][j].isdigit():
                    return False

                #3x3 Check
                x, y = i//3, j//3
                if board[i][j] not in seen3x3[x][y] and board[i][j].isdigit():
                    seen3x3[x][y].add(board[i][j])
                elif board[i][j] in seen3x3[x][y] and board[i][j].isdigit():
                    return False
        return True