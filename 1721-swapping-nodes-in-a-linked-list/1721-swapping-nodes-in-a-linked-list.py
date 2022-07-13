# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow= head
        left= right = ListNode(None)
        for i in range(k-1):
            fast = fast.next
            i+=1
        left = fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        right = slow
        left.val,right.val = right.val,left.val
        return head