'''
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        # cache = {}

        # def dfs(r,c):
        #     if r == rows or c == cols or matrix[r][c] == 0:
        #         return 0

        #     if (r,c) in cache:
        #         return cache[(r,c)]
            
        #     cache[(r,c)] = 1 + min(dfs(r+1,c),dfs(r,c+1),dfs(r+1,c+1))
        #     return cache[(r,c)]
        
        # res = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         res += dfs(i,j)
        # return res

        dp = defaultdict(int)

        res = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]:
                    dp[(r,c)] = 1 + min(dp[(r,c-1)],dp[(r-1,c)],dp[(r-1,c-1)])
                    res += dp[(r,c)]
        return res
