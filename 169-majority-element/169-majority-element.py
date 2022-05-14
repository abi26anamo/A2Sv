class Solution:
    def majorityElement(self, nums: List[int]) -> int:
                mp = {}
                for i in range(0, len(nums)):
                    if nums[i] in mp.keys():
                         mp[nums[i]] += 1
                    else:
                            mp[nums[i]] = 1
                for key in mp:
                    if mp[key] > (len(nums)/ 2):
                        return key
                return -1