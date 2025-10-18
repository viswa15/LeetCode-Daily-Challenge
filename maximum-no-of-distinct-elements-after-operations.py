'''
3397. Maximum Number of Distinct Elements After Operations

avatar
Discuss Approach
arrow-up
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
'''


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
      
        # Initialize the count of distinct elements
        distinct_count = 0
      
        # Track the previous assigned value (start with negative infinity)
        previous_value = float('-inf')
      
        # Process each number in sorted order
        for num in nums:
            # Calculate the optimal value for current element:
            # 1. We want it to be at least previous_value + 1 (to ensure distinctness)
            # 2. But it cannot be less than num - k (lower bound of modification range)
            # 3. And it cannot be greater than num + k (upper bound of modification range)
          
            # The earliest valid position is max(num - k, previous_value + 1)
            # But we're limited by the upper bound num + k
            current_value = min(num + k, max(num - k, previous_value + 1))
          
            # If we can assign a value greater than the previous one, it's distinct
            if current_value > previous_value:
                distinct_count += 1
                previous_value = current_value
      
        return distinct_count