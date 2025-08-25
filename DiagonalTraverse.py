'''
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]


Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])

        odd = {}
        even = {}

        for i in range(m):
            for j in range(n):
                k = i + j
                if k % 2 == 1:
                    if k not in odd:
                        odd[k] = [mat[i][j]]
                    else:
                        odd[k].append(mat[i][j])
                else:
                    if k not in even:
                        even[k] = [mat[i][j]]
                    else:
                        even[k].append(mat[i][j])

        for i in even:
            even[i] = even[i][::-1]
        
        res = []
        i = 0
        k = m + n - 2

        while i<=k:
            if i in odd:
                res.extend(odd[i])
                odd.pop(i)
            else:
                res.extend(even[i])
                even.pop(i)
            i += 1
        

        return res

                

