class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = [1 for _ in range(rowIndex+1)]
        if rowIndex ==0:
            return curr_row
        prev = self.getRow(rowIndex-1)
        for i in range(1,len(prev)):
            curr_row[i] = prev[i-1]+prev[i]
        return curr_row
