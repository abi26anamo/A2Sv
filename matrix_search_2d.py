class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper_search(l, target):
            start, end = 0, len(matrix[0])-1
            
            while start <= end:
                mid = (start+end)//2
                if l[mid] == target:
                    return True
                elif l[mid] < target:
                    start = mid + 1
                else:
                    end = mid-1
            return False
            
        if matrix == [] or matrix == [[]]:
            return False
        start, end = 0 ,len(matrix)-1
        
        while start <= end:
            mid = (start + end)//2
            # inner binary search on the row
            value = helper_search(matrix[mid], target)
            if value == True:
                return True
            elif matrix[mid][-1] > target:
                end = mid-1
            else:
                start = mid + 1
        return False
