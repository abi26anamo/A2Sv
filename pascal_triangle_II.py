class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(i):
            if i==0:
                return [[1]]
            curr = helper(i-1)
            arr = [1]
            for j in range(1,len(curr[-1])):
                arr.append(curr[-1][j-1]+curr[-1][j])
            arr.append(1)
            curr.append(arr)
            return curr
        return helper(rowIndex)[-1]
