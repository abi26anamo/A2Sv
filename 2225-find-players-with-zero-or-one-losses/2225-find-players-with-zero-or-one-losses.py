class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        res =[]
        for match in matches:
            if match[1] not in dic:
                dic[match[1]] =1
            else:
                dic[match[1]]+=1
        zeroLoser = set()
        for match in matches:
            if match[0] not in dic:
                zeroLoser.add(match[0])
        oneLoser =[]
        for k,v in dic.items():
            if v ==1:
                oneLoser.append(k)
        zeroLoser = sorted(zeroLoser)
        oneLoser.sort()
        res.append(zeroLoser)
        res.append(oneLoser)
        return res
                
        
        