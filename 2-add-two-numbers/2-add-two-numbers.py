# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        carry = 0
        while l1 is not None or l2 is not None:
            Sum = carry
            if l1 is not None:
                Sum += l1.val
                l1 =  l1.next
                
                
            if l2 is not None:
                Sum+= l2.val
                l2 = l2.next
            node = ListNode(Sum % 10)

            carry = Sum // 10

            if prev is None:
                prev = head = node

            else:
                prev.next = node
                prev = prev.next

        if carry > 0:
            prev.next = ListNode(carry)
        return head


            
           