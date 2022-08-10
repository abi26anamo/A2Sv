class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        def dfs(node):
            for i,adj in enumerate(isConnected[node]):
                if adj and i not in seen:
                    seen.add(i)
                    dfs(i)
        ans = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans
       