'''
3003. Maximize the Number of Partitions After Operations

avatar
Discuss Approach
arrow-up
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

Choose the longest prefix of s containing at most k distinct characters.
Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
Finally, we remove "a" and s becomes empty, so the procedure ends.
Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

Constraints:

1 <= s.length <= 104
s consists only of lowercase English letters.
1 <= k <= 26
'''


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        @cache
        def dfs(index: int, current_chars: int, can_change: int) -> int:
            """
            Dynamic programming function to find maximum partitions.
          
            Args:
                index: Current position in string
                current_chars: Bitmask representing characters in current partition
                can_change: Flag indicating if we can still change one character (1 = can change, 0 = already used)
          
            Returns:
                Maximum number of partitions from current position
            """
            # Base case: reached end of string
            if index >= n:
                return 1
          
            # Get bitmask for current character
            char_bit = 1 << (ord(s[index]) - ord('a'))
          
            # Add current character to the partition
            next_chars = current_chars | char_bit
          
            # Check if adding current character exceeds k distinct characters
            if next_chars.bit_count() > k:
                # Start new partition with current character
                result = dfs(index + 1, char_bit, can_change) + 1
            else:
                # Continue with current partition
                result = dfs(index + 1, next_chars, can_change)
          
            # If we can still change one character
            if can_change:
                # Try changing current character to each possible letter
                for letter_index in range(26):
                    # Create bitmask for the new character
                    next_chars = current_chars | (1 << letter_index)
                  
                    if next_chars.bit_count() > k:
                        # Start new partition with the changed character
                        result = max(result, dfs(index + 1, 1 << letter_index, 0) + 1)
                    else:
                        # Continue with current partition including changed character
                        result = max(result, dfs(index + 1, next_chars, 0))
          
            return result
      
        # Store string length
        n = len(s)
      
        # Start DFS from index 0, empty partition, with ability to change one character
        return dfs(0, 0, 1)