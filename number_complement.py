class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        bit_len = num.bit_length()
        while bit_len >0:
            num^=mask
            mask<<=1
            bit_len-=1
        return num
       
