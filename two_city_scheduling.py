class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [ [abs(costs[i][0] - costs[i][1]), i] for i in range(len(costs))]

        diff.sort(reverse=True)
        a = 0
        total = 0
        n = len(costs)//2
        for i in range(len(diff)):
            
            cost , index = diff[i]
            costa, costb = costs[index]
            if costa < costb and a < n :
                a += 1
                total += costa
            elif costb <= costa and i-a < n:
                total += costb  
            elif a < n:
                a += 1 
                total += costa 
            else:
                total += costb
                
        return total
