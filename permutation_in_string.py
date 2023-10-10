class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count_s1 = Counter(s1)
        permut = {}
        contains = False
        
        for right in range(len(s2)):
            if s2[right] in count_s1:
                if s2[right] in permut:
                     permut[s2[right]]+=1
                else:
                    permut[s2[right]]=1
            else:
                left = right+1
                permut = {}
                
            if right-left+1==len(s1):
                if permut == count_s1:
                    contains =True
                    break
                    
                #move window
                permut[s2[left]] -= 1
                if permut[s2[left]] == 0:
                    del permut[s2[left]]
                left += 1    
                
        return contains
