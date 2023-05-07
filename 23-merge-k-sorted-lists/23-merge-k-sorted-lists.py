class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]
        for i in lists:
            head =i
            while head:
                heapq.heappush(heap,head.val)
                head = head.next

        dummy = ListNode(0)
        head = dummy
        while heap:
            node = heapq.heappop(heap)
            head.next = ListNode(node)
            head = head.next
        return dummy.next
    
    
