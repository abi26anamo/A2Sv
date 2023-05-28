class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        middle_one = float('inf')

        for i in range(len(nums)):
            if nums[i]<=smallest:
                smallest = nums[i]
            elif nums[i]<=middle_one:
                middle_one = nums[i]
            else:
                return True
        return False

        
