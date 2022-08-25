class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid
        if left % 2 == 0:
            return nums[left]
        return nums[right]
                    
        