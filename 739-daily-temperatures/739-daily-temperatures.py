class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        output= [0]*n
        stack =[]
        for idx,val in enumerate(temperatures):
            while stack and val >stack[-1][0]:
                temp,index = stack.pop()
                output[index] = (idx-index)
            stack.append([val,idx])
        return output
            