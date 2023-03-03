class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left+1 < right:
            mid = left+(right-left)//2
            if isBadVersion(mid):
                right =mid
            else:
                left = mid
        return right
