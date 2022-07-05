# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1=dum = ListNode(0)
        dum.next = head
        while dum.next and dum.next.next:
            first = dum.next
            second = dum.next.next
            dum.next,first.next,second.next =second,second.next,first
            dum=first
        return d1.next
    
        