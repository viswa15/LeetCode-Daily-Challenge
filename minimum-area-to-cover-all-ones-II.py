'''3197. Find the Minimum Area to Cover All Ones II

You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:
The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.

Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:
The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:
1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.'''

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def area(t,b,l,r):
            top = b+1
            bottom = -1
            left = r + 1
            right = -1

            for i in range(t,b+1):
                for j in range(l,r+1):
                    if grid[i][j] == 1:
                        top = min(top,i)
                        bottom = max(bottom,i)
                        left = min(left,j)
                        right = max(right,j)
            return (bottom - top + 1) * (right-left+1)
        

        def solve():
            res = float("inf")
            n = len(grid)
            m = len(grid[0])

            for i in range(n):
                for j in range(m):
                    res = min(
                        res,
                        area(0,i,0,j) +
                        area(0,i,j+1,m-1) + 
                        area(i+1,n-1,0,m-1)
                    )

                    res = min(
                        res,
                        area(0,i,0,m-1) + 
                        area(i+1,n-1,0,j) +
                        area(i+1,n-1,j+1,m-1)
                    )
            
            for i in range(n-1):
                for j in range(i+1 ,n-1): # here j is initiated as i+1 because to know the last index..
                    res = min(
                        res,
                        area(0,i,0,m-1) +
                        area(i+1,j,0,m-1) +
                        area(j+1,n-1,0,m-1)
                    )
            return res
        
        out = solve()
        print(out)
        n = len(grid)
        m = len(grid[0])

        new_grid = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_grid[j][n-1-i] = grid[i][j]
        
        grid = new_grid
        return min(out,solve())