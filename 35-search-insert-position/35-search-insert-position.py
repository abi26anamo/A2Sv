class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        elif target > nums[-1]: return len(nums)
        else:
            i, mid, j = 0, 0, len(nums) - 1
            while(i <= j):
                mid = (i + j) // 2
                if nums[mid] > target: j = mid -1
                elif nums[mid] < target: i = mid + 1
                else: return mid
            return mid + 1 if target > nums[mid] else mid