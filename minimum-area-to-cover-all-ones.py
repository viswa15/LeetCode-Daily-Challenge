'''
3195. Find the Minimum Area to Cover All Ones I
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:
1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
'''

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        t,b = m,0
        l,r = n,0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    t,b = min(t,i),max(b,i)
                    l,r = min(l,j),max(r,j)
        
        return (b-t+1) * (r-l+1)