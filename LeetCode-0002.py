# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        pow = 1
            
        num1 = l1.val * pow
        num2 = l2.val * pow
        
        while l1.next != None:
     
            pow *= 10
            
            l1 = l1.next
 
            num1 += l1.val * pow
            
            if l2.next != None:
                l2 = l2.next
             
                num2 += l2.val * pow
                
        while l2.next != None:
     
            pow *= 10
            
            l2 = l2.next
 
            num2 += l2.val * pow
    
        # summation of the two linked lists reversed by using slice operation [::-1]#
        return_number_s = str(num1 + num2)[::-1]
        
        sum_list = ListNode()
        temp_list = sum_list
        
        for i in range(len(return_number_s)):
            c = return_number_s[i]
            temp_list.val = int(c)
            
            if i != (len(return_number_s) - 1):
                temp_list.next = ListNode()
                temp_list = temp_list.next
                
        return sum_list
               
solution = Solution()

num1 = ListNode()
temp = num1
temp.val = 2
temp.next = ListNode()
temp = temp.next
temp.val = 4
temp.next = ListNode()
temp = temp.next
temp.val = 3

num2 = ListNode()
temp = num2
temp.val = 5
temp.next = ListNode()
temp = temp.next
temp.val = 6
temp.next = ListNode()
temp = temp.next
temp.val = 4

answer_list = solution.addTwoNumbers(num1, num2)

print(answer_list.val)

while answer_list.next != None:
	answer_list = answer_list.next

	print(answer_list.val,)
