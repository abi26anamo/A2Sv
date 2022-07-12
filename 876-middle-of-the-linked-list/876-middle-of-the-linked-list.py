# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast =head 
#         slow = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
          
            count =0
            middle = head
            while head:
                count+=1
                if count%2==0:
                    middle = middle.next
                head=head.next
            return middle 
            
         
