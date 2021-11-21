# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
# 
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
#
# Input: nums = [1,1]
# Output: [2]
#  
#
#  Constraints:
#
#  n == nums.length
#  1 <= n <= 105
#  1 <= nums[i] <= n
#

class Solution:
    def findDisappearedNumbers(self, nums):
        
        disappeared_numbers = [ i for i in range(0, len(nums) + 1) ]
        
        for n in nums:
            if disappeared_numbers[n] > 0:
                disappeared_numbers[n] *= -1
            
        disappeared_numbers.pop(0)
                    
        return [ i for i in disappeared_numbers if i > 0 ]

solution = Solution()
print( solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) )
