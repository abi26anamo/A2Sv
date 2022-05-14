class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')' :'(','}':'{',']':'['}
        stack =[]
        for ch in s:
                if ch in dic.values():
                    stack.append(ch)
                elif stack and dic[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []
        