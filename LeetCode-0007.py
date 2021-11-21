# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 
#  
# 
# Example 1:
# 
# Input: x = 123
# Output: 321
# Example 2:
# 
# Input: x = -123
# Output: -321
# Example 3:
# 
# Input: x = 120
# Output: 21
# Example 4:
# 
# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x):
        
        reversed_s = str(x).rstrip('0')
        
        if (reversed_s == ''):
            return 0
        
        reversed_l = list(reversed_s)
        reversed_l.reverse()
        
        if reversed_l[-1] == '-':
            reversed_l.remove('-')
            
            reversed_l = ['-'] + reversed_l
            
        reversed_i = int(''.join(reversed_l))
        
        if (reversed_i >= ((2**31) - 1)) or (reversed_i < (-1 * (2**31))):
            reversed_i = 0
        
        return reversed_i

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
