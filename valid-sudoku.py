'''
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def mat_check(i,j):
            if 0<=i<=2:
                if 0<=j<=2:
                    return 0
                elif 3<=j<=5:
                    return 1
                else:
                    return 2
            elif 3<=i<=5:
                if 0<=j<=2:
                    return 3
                elif 3<=j<=5:
                    return 4
                else:
                    return 5
            else:
                if 0<=j<=2:
                    return 6
                elif 3<=j<=5:
                    return 7
                else:
                    return 8
        
        r = [[] for _ in range(9)]
        c = [[] for _ in range(9)]
        sub = [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    s = mat_check(i,j)
                    if board[i][j] in r[i]:  #row check
                        return False
                    if board[i][j] in c[j]: #col check
                        return False
                    if board[i][j] in sub[s]:  #sub matrix check
                        return False
                    
                    r[i].append(board[i][j])
                    c[j].append(board[i][j])
                    sub[s].append(board[i][j])
            
                        
        
        

        return True



