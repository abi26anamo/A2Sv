# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leftNode =left= ListNode(0)
        rightNode =right= ListNode(0)
        parity =1
        while head:
            if parity%2:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
            parity+=1
        right.next =None
        left.next =rightNode.next
        return leftNode.next
