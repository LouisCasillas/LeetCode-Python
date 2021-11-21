# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# Example 1:
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
# 
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
# 
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
# 
# Input: nums1 = [2], nums2 = []
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        added_numbers = nums1 + nums2
        added_numbers.sort()
        
        median = 0
        
        num_of_numbers = len(added_numbers)
        
        if ((num_of_numbers % 2) == 0):
            middle_i = int(num_of_numbers / 2)
            median = (added_numbers[middle_i - 1] + added_numbers[middle_i]) / 2
        else:
            middle_i = int(num_of_numbers / 2)
            median = added_numbers[middle_i]
            
        return median

solution = Solution()

print(solution.findMedianSortedArrays([1,3], [2]))
print(solution.findMedianSortedArrays([1,2], [3,4]))
