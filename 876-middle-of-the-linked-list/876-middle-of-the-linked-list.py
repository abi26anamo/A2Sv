# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size_lst = 0
        start=node =head
        while start:
            size_lst +=1
            start=start.next
        middle = size_lst//2
        
        counter =0
        while node:
            if counter == middle:
                return node
            else:
                counter+=1
                node = node.next
        return None