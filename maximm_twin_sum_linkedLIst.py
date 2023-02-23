class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        vals = []
        while fast and fast.next:
            vals.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        max_sum = 0
        i = len(vals)-1
        while i>=0 and slow:
            max_sum =  max(max_sum,vals[i]+slow.val)
            slow = slow.next
            i-=1
        return max_sum
