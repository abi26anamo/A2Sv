class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse =True)
        self.min_fair = float('inf')
        def helper(idx,children):
            for i in range(k):
                if idx == len(cookies):
                    self.min_fair = min(self.min_fair,max(children))
                    return self.min_fair
                if self.min_fair <= max(children):
                    return
                for i in range(k):
                    children[i]+=cookies[idx]
                    helper(idx+1,children)
                    children[i]-=cookies[idx]
                return self.min_fair

        return helper(0,[0]*k)            
