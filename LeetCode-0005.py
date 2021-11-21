class Solution:
    def longestPalindrome(self, s):
        max_palindrome_substring = ''
        
        current_substring_l = []

        while len(max_palindrome_substring) < len(s):

            for c in list(s):

                current_substring_l.append(c)
                current_substring_s = ''.join(current_substring_l)

                if current_substring_s == current_substring_s[::-1]:
                    if len(current_substring_s) > len(max_palindrome_substring):
                        max_palindrome_substring = current_substring_s
                
            s = s[1::]
            current_substring_l = []
                
        return max_palindrome_substring

solution = Solution()
print(solution.longestPalindrome('cbbd'))
