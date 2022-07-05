# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def nextLargerNodes(self, head):
                """
                :type head: ListNode
                :rtype: List[int]
                """
                prev = None
                while head:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
                head = prev
                res = []
                st = []
                while head:
                    while st and st[-1] <= head.val:
                        st.pop()
                    if st:
                        res.append(st[-1])
                    else:
                        res.append(0)
                    st.append(head.val)
                    head = head.next
                return res[::-1]