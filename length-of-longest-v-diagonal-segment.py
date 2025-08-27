'''
3459. Length of Longest V-Shaped Diagonal Segment

You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

 

Example 1:
Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 5
Explanation: The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:
Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
Output: 4
Explanation: The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:
Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
Output: 5
Explanation: The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:
Input: grid = [[1]]
Output: 1
Explanation: The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

 

Constraints:
n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
'''

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [(-1,-1),(-1,1),(1,1),(1,-1)] #t_1,t_r,b_l,b_r


        @cache
        def dfs(i, j, target, turn, dir):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != target:
                return 0
        
            target = 0 if target==2 else 2
            ni = i + dirs[dir][0]
            nj = j + dirs[dir][1]
            total = 0

            if turn:
                #move in same direction
                total = max(total, dfs(ni,nj,target,True,dir)+1)
            else:
                #move in same direction
                total = max(total, dfs(ni,nj,target,False,dir)+1)

                #move in another direction
                new_d = (dir + 1) % 4
                ni = i + dirs[new_d][0]
                nj = j + dirs[new_d][1]
                total = max(total, dfs(ni,nj,target,True,new_d)+1)
            
            return total

            


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        res = max(res, dfs(i + dirs[d][0], j + dirs[d][1],2,False,d)+1)
                    

        return res