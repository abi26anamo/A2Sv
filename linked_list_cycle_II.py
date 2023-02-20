
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast and fast.next == None:
            return None
        
        if fast == slow:
            slow = head
            while fast!=slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return None
