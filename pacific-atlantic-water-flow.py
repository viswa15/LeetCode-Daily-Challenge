'''
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue: deque, visited: set) -> None:
            """
            Perform BFS to find all cells that can reach the ocean.
            Start from ocean edges and move to cells with equal or greater height.
            """
            while queue:
                # Process all cells at current level
                level_size = len(queue)
                for _ in range(level_size):
                    curr_row, curr_col = queue.popleft()
                  
                    # Check all 4 adjacent cells (up, down, left, right)
                    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                    for delta_row, delta_col in directions:
                        next_row = curr_row + delta_row
                        next_col = curr_col + delta_col
                      
                        # Check if next cell is valid and water can flow backwards
                        # (from next cell to current cell, which means next >= current)
                        if (0 <= next_row < rows and 
                            0 <= next_col < cols and 
                            (next_row, next_col) not in visited and 
                            heights[next_row][next_col] >= heights[curr_row][curr_col]):
                          
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))
      
        # Get grid dimensions
        rows = len(heights)
        cols = len(heights[0])
      
        # Initialize visited sets and queues for both oceans
        pacific_visited = set()
        atlantic_visited = set()
        pacific_queue = deque()
        atlantic_queue = deque()
      
        # Add border cells to respective ocean queues
        for row in range(rows):
            for col in range(cols):
                # Pacific ocean: top edge (row=0) or left edge (col=0)
                if row == 0 or col == 0:
                    pacific_visited.add((row, col))
                    pacific_queue.append((row, col))
              
                # Atlantic ocean: bottom edge (row=rows-1) or right edge (col=cols-1)
                if row == rows - 1 or col == cols - 1:
                    atlantic_visited.add((row, col))
                    atlantic_queue.append((row, col))
      
        # Find all cells reachable from each ocean
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
      
        # Return cells that can reach both oceans (intersection of both sets)
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_visited and (row, col) in atlantic_visited:
                    result.append([row, col])
      
        return result