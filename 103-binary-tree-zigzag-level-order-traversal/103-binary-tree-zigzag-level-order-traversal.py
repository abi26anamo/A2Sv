# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        queue = deque([root])
        output = []
        while queue:
            levelCount =len(queue)
            ans = []
            for i in range(levelCount):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(ans)
            res =[]
            for i in range(len(output)):
                if i%2 !=0:
                     res.append(output[i][::-1])
                else:
                    res.append(output[i])
        return res
            
                
        # res =[]
        # stack = [root]
        # dirc = 1
        # if not root:
        #     return []
        # while stack:
        #     temp = []
        #     for x in range(len(stack)):
        #         node = stack.pop(0)
        #         temp.append(node.val)
        #         if node.left !=None:
        #             stack.append(node.left)
        #         if node.right!=None:
        #             stack.append(node.right)
        #     if dirc % 2 ==0:
        #         res.append(temp[::-1])
        #     else:
        #         res.append(temp[::1])
        #     dirc+=1
        # return res