'''
3349. Adjacent Increasing Subarrays Detection I


Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

 

Constraints:

2 <= nums.length <= 100
1 < 2 * k <= nums.length
-1000 <= nums[i] <= 1000
'''



class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
         # Track the maximum achievable length of valid adjacent subarrays
        max_valid_length = 0
      
        # Length of the previous strictly increasing subarray
        previous_length = 0
      
        # Length of the current strictly increasing subarray being built
        current_length = 0
      
        # Iterate through the array with index and value
        for i, current_value in enumerate(nums):
            # Extend current strictly increasing subarray
            current_length += 1
          
            # Check if we've reached the end of a strictly increasing sequence
            # This happens when we're at the last element or next element is not greater
            if i == len(nums) - 1 or current_value >= nums[i + 1]:
                # Update maximum valid length considering two cases:
                # 1. Split current subarray into two equal parts (current_length // 2)
                # 2. Use previous and current as two adjacent subarrays (min of their lengths)
                max_valid_length = max(
                    max_valid_length,
                    current_length // 2,
                    min(previous_length, current_length)
                )
              
                # Move to next sequence: current becomes previous, reset current
                previous_length = current_length
                current_length = 0
      
        # Check if we can form two adjacent subarrays of at least length k
        return max_valid_length >= k