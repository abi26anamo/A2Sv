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
