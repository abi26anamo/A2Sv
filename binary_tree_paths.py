class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      def helper(node,curr_path,answer):
          if not node.left and not node.right:
              curr_path.append(str(node.val))
              answer.append("->".join(curr_path))
              return answer

          curr_path.append(str(node.val))
          if node.left:
              helper(node.left,curr_path,answer)
              curr_path.pop()
          if node.right:
              helper(node.right,curr_path,answer)
              curr_path.pop()
          return answer
          
      return helper(root,[],[])
