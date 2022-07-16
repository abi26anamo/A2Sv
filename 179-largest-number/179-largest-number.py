class Solution:
    def largestNumber(self, nums: List[int]) -> str:
              
                # if len(nums) == 1:
                #     return str(nums)
                nums = map(str,nums)
                # for i in range(len(nums)):
                #     for j in range(i+1,len(nums)):
                #         if nums[j]+nums[i] > nums[i]+nums[j]:
                #             nums[i],nums[j] = nums[j],nums[i]
                # res = "".join(nums)
                # if res == [0]*len(res):
                #     return '0'
                # else:
                #     return res
                            
                def comp(a,b):
                    if a+b >b+a :
                        return -1
                    elif a+b < b+a:
                        return 1
                    else:
                        return 0
                   
                nums = sorted(nums,key = functools.cmp_to_key(comp))
                
                if nums ==[0]*len(nums):
                    return 0
                else:
                    return str(int("".join(nums)))
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            

                    
            
        