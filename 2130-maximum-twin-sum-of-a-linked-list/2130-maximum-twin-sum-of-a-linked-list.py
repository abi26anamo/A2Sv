# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast =head 
        slow = ListNode(0,head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = None
        slow.next = prev
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first = head
        second = prev
        res =0
        while first:
            res = max(res,first.val+second.val)
            first= first.next
            second = second.next
        return res