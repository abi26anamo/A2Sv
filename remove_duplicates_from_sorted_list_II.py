class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        dummy.next= head
        while curr and curr.next and curr.next.next:
            if curr.next.val==curr.next.next.val:
                temp = curr
                while temp.next and temp.next.next and temp.next.val==temp.next.next.val:
                    temp = temp.next
                curr.next = temp.next.next
                
            else:
                curr = curr.next
        return dummy.next
