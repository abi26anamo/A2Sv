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
        i = 0 
        while cur:
            cur.val = sorted_lst[i]
            cur = cur.next
            i += 1
            
        return ans
        