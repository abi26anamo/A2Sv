class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i=0
        j=1
        t=len(target)
        ans=[]
        while (i < t) :
            ans.append("Push")
            if target[i] == j:
                i+=1
                j+=1
            else:
                ans.append("Pop")
                j+=1
        return ans