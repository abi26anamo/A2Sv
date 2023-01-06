
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        posatives = []
        negatives =[]
        for num in nums:
            if num >0:
                posatives.append(num)
            else:
                negatives.append(num)
        res =[]   
        for i in range(len(nums)//2):
            res.append(posatives[i])
            res.append(negatives[i])
        return res
            
