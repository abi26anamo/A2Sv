# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]
        heapq.heapify(heap)
        for i in lists:
            head =i
            while head:
                heapq.heappush(heap,head.val)
                head = head.next
        final = ListNode(None)
        res = final
        while heap:
            temp = heapq.heappop(heap)
            final.next = ListNode(temp)
            final = final.next
        return res.next
    
    
    
