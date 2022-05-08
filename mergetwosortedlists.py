class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        tail = node 
        
        while list2 and list1:
            if list1.val < list2.val:
                tail.next = list1
                list1=list1.next
            else:
                tail.next = list2
                list2=list2.next
            tail= tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return node.next

    
