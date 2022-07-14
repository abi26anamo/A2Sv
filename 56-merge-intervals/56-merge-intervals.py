class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack =[]
        intervals.sort()
        for curr in intervals:
            if not stack or curr[0] > stack[-1][-1]:
                stack.append(curr)
            else:
                if stack[-1][-1] < curr[-1]:
                    stack[-1][-1] = curr[-1]
        return stack
      
        
                
            

            
            
            