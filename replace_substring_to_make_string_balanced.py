class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        each_occurence = n//4
        invalids = {}
        for key in count:
            if count[key] >each_occurence:
                invalids[key]= count[key]-each_occurence
    
        if len(invalids)==0:
            return 0
        left = 0
        min_len =n
        number_of_invalids = len(invalids)
        for right in range(n):
            if s[right] in invalids: 
                invalids[s[right]] -= 1
                if invalids [s[right]] == 0: number_of_invalids -= 1

            while left<=right and number_of_invalids == 0:
                min_len = min(min_len, right - left + 1)
                if s[left] in invalids:
                    invalids[s[left]] += 1
                    if invalids [s[left]] == 1: 
                        number_of_invalids += 1 
                left += 1
        return min_len
    



            
            
            



            
           



      
        
