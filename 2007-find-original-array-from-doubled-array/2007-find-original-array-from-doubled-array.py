class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        if count[0] % 2:
            return []
        for x in sorted(count):
            if count[x] > count[2 * x]:
                return []
            if x == 0:
                if count[x] % 2:
                    return []
                else:
                    count[x] = count[x] // 2 
            else:
                count[2 * x] -= count[x]  
        return list(count.elements())
            
            