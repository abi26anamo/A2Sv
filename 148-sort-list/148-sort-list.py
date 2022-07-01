# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ans = head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next 
        sorted_lst = sorted(lst)
        count = 0 
        while cur:
            cur.val = sorted_lst[count]
            cur = cur.next
            count += 1
            
        return ans
        