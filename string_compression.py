class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        left =0
        right = 0
        s = ""
        while right < n:
            s+=chars[left]
            while right <n and chars[right]==chars[left]:
                right+=1
            if (right-left)>1:
                s+=str(right-left)
            left = right
        len_s = len(s)
        for i in range(len_s):
            chars[i] = s[i]
        chars = chars[:len_s]
        return len(chars)
