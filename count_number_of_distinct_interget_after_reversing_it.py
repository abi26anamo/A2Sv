class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def reversenum(num):
            reversed_int = 0
            while num>0:
                last_digit = num%10
                reversed_int = reversed_int*10+last_digit
                num = num//10
            return reversed_int
        
        new_arr =[]
        for num in nums:
            new_arr.append(num)
            new_arr.append(reversenum(num))
            
        return len(set(new_arr))
