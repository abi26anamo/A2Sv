class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            new_num =0
            for i in range(len(str(num))):
                new_num +=int(str(num)[i])
            num= new_num
        return num