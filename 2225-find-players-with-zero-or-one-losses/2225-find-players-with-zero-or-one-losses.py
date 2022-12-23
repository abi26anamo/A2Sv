class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic ={}
        answer =[]
        for m in matches:
            if m[1] not in dic:
                dic[m[1]] =1
            else:
                dic[m[1]]+=1
        zeroLoser =set()
        for i in matches:
            if i[0] not in dic:
                zeroLoser.add(i[0])
        oneLoser =[]
        for k,v in dic.items():
            if v ==1:
                oneLoser.append(k)
        zeroLoser = list(zeroLoser)
        zeroLoser.sort()
        oneLoser.sort()
        answer.append(zeroLoser)
        answer.append(oneLoser)
        return answer
                
       
    
            
        
        