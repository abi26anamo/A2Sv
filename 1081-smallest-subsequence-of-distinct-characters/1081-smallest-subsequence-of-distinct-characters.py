class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d ={c:i for i,c in enumerate(s)}
        res =[]
        seen = set()
        for i,c in enumerate(s):
            if c not in res:
                while res and d[res[-1]]>=i and c <res[-1]:
                    res.pop()
                res.append(c)
        return "".join(res)
        