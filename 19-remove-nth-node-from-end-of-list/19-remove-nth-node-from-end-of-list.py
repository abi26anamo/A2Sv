# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first = second = head
        # for _ in range(n):
        #     first = first.next
        #     if not first:
        #         return head.next
        # while first.next:
        #     first = first.next
        #     second = second.next
        # second.next = second.next.next
        # return head
        
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        count = count-n
        temp = head
        if count ==0:
            return head.next
        while count >1:
            count-=1
            temp = temp.next
        temp.next = temp.next.next
        return head
        