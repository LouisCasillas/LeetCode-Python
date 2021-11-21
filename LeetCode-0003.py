# Given a string s, find the length of the longest substring without repeating characters.
# 
#  
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
# 
# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s):
        max_substring = 0
        temp_max = 0
        
        current_substring = []
        
        for c in list(s):
            temp_max += 1
            
            if c in current_substring:
                
                c_index = current_substring.index(c)
                
                current_substring = current_substring[c_index + 1:]
                
                temp_max -= (c_index + 1)
                
            current_substring.append(c)

            if temp_max > max_substring:
                max_substring = temp_max

        return max_substring

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
