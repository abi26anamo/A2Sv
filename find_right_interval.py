class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        dic = defaultdict(lambda:-1)
        for idx,val in enumerate(intervals):
            dic[val[0]] = idx

        res = [-1]*len(intervals)
        intervals.sort()
        
        for i in range(len(intervals)):
            left = -1
            right = len(intervals)
            while left+1 < right:
                mid = (left+right)//2
                if intervals[i][1] <=intervals[mid][0] :
                    right = mid
                else:
                    left = mid
                if 0<=right<len(intervals):
                    res[dic[intervals[i][0]]]  = dic[intervals[right][0]]
        return res
