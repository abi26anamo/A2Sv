class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n  = len(bills)
        dic =defaultdict(int)
        for i in range(n):
            if bills[i] ==5:
                dic[5]+=1
            elif bills[i] ==10:
                dic[10]+=1
                if not dic[5]:
                    return False
                else:
                    dic[5]-=1
            else:
                if not dic[5]:
                    return False
                elif not dic[10] and dic[5]<3:
                    return False
                elif dic[5] and dic[10]:
                    dic[5]-=1
                    dic[10]-=1
                elif not dic[10] and dic[5]>=3:
                    dic[5]-=3
        return True
            

           
