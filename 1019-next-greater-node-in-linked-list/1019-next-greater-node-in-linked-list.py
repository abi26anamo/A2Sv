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
                arr =[]
                current = head
                while current:
                    arr.append(current.val)
                    current = current.next
                ans =[0]*len(arr)
                stack =[]
                for i in reversed(range(len(arr))):
                    while len(stack)>0 and stack[-1] <= arr[i]:
                        stack.pop()
                    if len(stack)!=0:
                        ans[i] = stack[-1]
                    stack.append(arr[i])
                return ans
                # prev = None
                # while head:
                #     temp = head.next
                #     head.next = prev
                #     prev = head
                #     head = temp
                # head = prev
                # res = []
                # st = []
                # while head:
                #     while st and st[-1] <= head.val:
                #         st.pop()
                #     if st:
                #         res.append(st[-1])
                #     else:
                #         res.append(0)
                #     st.append(head.val)
                #     head = head.next
                # return res[::-1]