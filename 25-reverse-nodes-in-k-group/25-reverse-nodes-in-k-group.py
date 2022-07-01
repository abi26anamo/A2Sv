# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        beg, end, nextNode = self.reverseK(head, k)
        while nextNode is not None:
            end.next, end, nextNode = self.reverseK(nextNode, k)
        return beg
            
    def reverseK(self, head, k):
        curr = head
        while curr is not None and k > 1:
            curr = curr.next
            k -= 1
        if curr is None:
            return head, None, None
        nextNode = curr.next
        curr.next = None
        return self.reverse(head), head, nextNode
    
    def reverse(self, head):
        curr, prev = head, None
        while curr is not None:
            curr.next, curr, prev = prev, curr.next, curr
        return prev

            
        