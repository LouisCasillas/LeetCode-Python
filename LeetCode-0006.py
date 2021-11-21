# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
#  
# 
# Example 1:
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
# 
# Input: s = "A", numRows = 1
# Output: "A"

class Solution:
	def convert(self, s, numRows):

		zigzag = []
	
		for i in range(numRows):
			zigzag.append([])	

		i = -1
		direction = 1
		for c in s:

			if i == (numRows - 1):
				direction = -1

			if i == 0:
				direction = 1

			i += (direction * 1)

			if (i < 0):
				i = 0

			if (i >= numRows):
				i = (numRows - 1)

			zigzag[ i ].append(c)

		zigzag_s = ''

		for line in zigzag:
			zigzag_s += (''.join(line))

		return zigzag_s

solution = Solution()
print(solution.convert('PAYPALISHIRING', 4))
print(solution.convert('A', 1))
print(solution.convert('AB', 1))
