# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         curr = head
#         N=0
#         while curr:
#             N+=1
#             curr =curr.next
            
#         mid = N//2
#         i=0
#         def reverse(head):
#             ans= None
#             while head:
#                 nxt = head.next
#                 head.next = ans
#                 ans =head
#                 head = nxt
#             return ans
#         first = second = head
#         while i <mid:
#             second = second.next
#             i+=1
#         second =reverse(second)
#         while first and second:
#             if first.val != second.val:return False
#             first = first.next
#             second =second.next
#         return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]

