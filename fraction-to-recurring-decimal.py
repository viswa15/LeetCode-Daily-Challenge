'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n,d = numerator,denominator
        
        if n%d == 0: return str(n//d)

        res = []

        if (n>0 and d<0) or (n<0 and d>0): res.append('-')

        n,d = abs(n),abs(d)

        res.append(str(n//d))
        res.append('.')

        rem = n % d

        seen = {}

        while rem != 0:
            if rem in seen:
                res.insert(seen[rem],'(')
                res.append(')')
                break
        
        

            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem//d))
            rem %= d
        
        return "".join(res)