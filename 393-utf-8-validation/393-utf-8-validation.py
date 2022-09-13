class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = ['{0:08b}'.format(d) for d in data]
        i = 0
        
        while i < len(data):
            n = 0
            d = data[i]
            j = 0
            while j < len(d) and d[j] == '1':
                n += 1
                j += 1
            if n > 4 or n == 1:
                return False
            elif n == 0: 
                i+=1
            else:
                i += 1
                while i < len(data) and data[i][:2] == '10' and n > 1:
                    i += 1
                    n -= 1
                if n != 1: return False
        return True