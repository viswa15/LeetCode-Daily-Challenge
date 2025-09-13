
'''
3541. Find Most Frequent Vowel and Consonant

You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
 

Example 1:

Input: s = "successes"

Output: 6

Explanation:

The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
The output is 2 + 4 = 6.
Example 2:

Input: s = "aeiaeia"

Output: 3

Explanation:

The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
There are no consonants in s. Hence, maximum consonant frequency = 0.
The output is 3 + 0 = 3.
 

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters only.
'''

class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {}
        c = {}

        for i in s:
            if i == 'a' or i =='e' or i=='i' or i=='o' or i=='u':
                v[i] = v.get(i,0) + 1
            else:
                c[i] = c.get(i,0) + 1
        
        f,r = 0,0


        if v != {}: f = max(v.values())
        if c != {}: r = max(c.values())

        res = 0

        for i in v:
            if v[i] == f:
                res += f
                break
        for i in c:
            if c[i] == r:
                res += r
                break

        return res 
