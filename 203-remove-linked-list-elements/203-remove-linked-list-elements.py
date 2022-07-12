# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp:
            if temp.val !=val:
                prev= temp
            else:
                if temp == head:
                    head = temp.next
                else:
                    prev.next = temp.next
            temp = temp.next
        return head
          
                
                