class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = [set() for i in range(9)]
        seen3x3 = [set() for i in range(9)]
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
                if i < 3:
                    if j < 3:
                        if board[i][j] not in seen3x3[0] and board[i][j].isdigit():
                            seen3x3[0].add(board[i][j])
                        elif board[i][j] in seen3x3[0] and board[i][j].isdigit():
                            return False
                    elif j >= 3 and j < 6:
                        if board[i][j] not in seen3x3[1] and board[i][j].isdigit():
                            seen3x3[1].add(board[i][j])
                        elif board[i][j] in seen3x3[1] and board[i][j].isdigit():
                            return False
                    else:
                        if board[i][j] not in seen3x3[2] and board[i][j].isdigit():
                            seen3x3[2].add(board[i][j])
                        elif board[i][j] in seen3x3[2] and board[i][j].isdigit():
                            return False
                elif i >= 3 and i < 6:
                    if j < 3:
                        if board[i][j] not in seen3x3[3] and board[i][j].isdigit():
                            seen3x3[3].add(board[i][j])
                        elif board[i][j] in seen3x3[3] and board[i][j].isdigit():
                            return False
                    elif j >= 3 and j < 6:
                        if board[i][j] not in seen3x3[4] and board[i][j].isdigit():
                            seen3x3[4].add(board[i][j])
                        elif board[i][j] in seen3x3[4] and board[i][j].isdigit():
                            return False
                    else:
                        if board[i][j] not in seen3x3[5] and board[i][j].isdigit():
                            seen3x3[5].add(board[i][j])
                        elif board[i][j] in seen3x3[5] and board[i][j].isdigit():
                            return False
                else:
                    if j < 3:
                        if board[i][j] not in seen3x3[6] and board[i][j].isdigit():
                            seen3x3[6].add(board[i][j])
                        elif board[i][j] in seen3x3[6] and board[i][j].isdigit():
                            return False
                    elif j >= 3 and j < 6:
                        if board[i][j] not in seen3x3[7] and board[i][j].isdigit():
                            seen3x3[7].add(board[i][j])
                        elif board[i][j] in seen3x3[7] and board[i][j].isdigit():
                            return False
                    else:
                        if board[i][j] not in seen3x3[8] and board[i][j].isdigit():
                            seen3x3[8].add(board[i][j])
                        elif board[i][j] in seen3x3[8] and board[i][j].isdigit():
                            return False
        return True