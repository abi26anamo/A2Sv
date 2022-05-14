class Solution:
    def frequencySort(self, s: str) -> str:
        c= Counter(list(s))
        result = []
        for ch in sorted(c,key=lambda x:c[x],reverse = True):
                result.append(ch*c[ch])
        return "".join(result)
        