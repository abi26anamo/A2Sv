class Solution:
    def average(self, salary: List[int]) -> float:
        minsal = float('inf')
        maxsal = 0
        n = len(salary)
        tot =0
        for i in range(n):
            minsal = min(minsal,salary[i])
            maxsal = max(maxsal,salary[i])
        for i in range(n):
            if salary[i]==minsal or salary[i]==maxsal:
                continue
            else:
                tot+=salary[i]
        return tot/(n-2)
        

        
    
            
        
       