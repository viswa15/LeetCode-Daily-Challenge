'''
812. Largest Triangle Area

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
'''

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
      
        # Iterate through all possible combinations of three points
        for point1 in points:
            x1, y1 = point1
          
            for point2 in points:
                x2, y2 = point2
              
                for point3 in points:
                    x3, y3 = point3
                  
                    # Calculate vectors from point1 to point2 and point1 to point3
                    vector1_x = x2 - x1
                    vector1_y = y2 - y1
                    vector2_x = x3 - x1
                    vector2_y = y3 - y1
                  
                    # Calculate area using cross product formula
                    # Area = |cross_product| / 2
                    cross_product = vector1_x * vector2_y - vector2_x * vector1_y
                    area = abs(cross_product) / 2.0
                  
                    # Update maximum area if current area is larger
                    max_area = max(max_area, area)
      
        return max_area