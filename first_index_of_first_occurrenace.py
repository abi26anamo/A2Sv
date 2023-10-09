class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0]*len(needle) 

        prev,curr = 0,1
        while curr<len(needle):
            if needle[prev] == needle[curr]:
                lps[curr] = prev+1
                prev+=1
                curr+=1
            elif prev>0:
                prev = lps[prev-1]
            else:
                curr+=1
        
        ned_idx, str_idx = 0,0
        while str_idx <len(haystack):
            if needle[ned_idx] ==  haystack[str_idx]:
                ned_idx+=1
                str_idx+=1
            elif ned_idx>0:
                ned_idx = lps[ned_idx-1]
            else:
                str_idx+=1
        
            if ned_idx == len(needle):
                return str_idx-ned_idx
        return -1
