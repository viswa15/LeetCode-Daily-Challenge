'''
407. Trapping Rain Water II
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
'''

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        #get dimensions of a heightMap
        rows,cols = len(heightMap),len(heightMap[0])

        #track visited cells to avoid processing them multiple times
        visited = [[False] * cols for _ in range(rows)]

        #Min-heap to process cells by height (water flows from lowest boundary)
        #Each element is (height,row,col)
        min_heap = []

        #add all boundary cells to the heap as starting points
        #water can not be trapped at boundaries - it flows out
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows-1 or col == 0 or col == cols - 1:
                    heappush(min_heap,(heightMap[row][col],row,col))
                    visited[row][col] = True
        
        #total water trapped
        total_water = 0

        #direction vectots to explore adjacent cells
        d = (-1,0,1,0,-1)

        #process cells from lowest boundary height to highest
        while min_heap:
            #get the cell with the minimim height from boundary
            current_height,current_row,current_col = heappop(min_heap)

            #check all four adjacent cells
            for i in range(4):
                next_row = current_row + d[i]
                next_col = current_col + d[i+1]

                #check if adjacents are valid and un visited
                if (0<=next_row<rows and 0<=next_col<cols) and not visited[next_row][next_col]:
                    total_water += max(0,current_height-heightMap[next_row][next_col])

                    visited[next_row][next_col] = True

                    heappush(min_heap,(max(current_height,heightMap[next_row][next_col]),next_row,next_col))

        return total_water

