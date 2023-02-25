class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left =0
        max_len = 0
        hash_map = defaultdict(lambda:0)
        for right in range(n):
            
            while len(hash_map)==2 and fruits[right] not in hash_map:
                
                hash_map[fruits[left]]-=1
                
                if hash_map[fruits[left]]==0:
                    del hash_map[fruits[left]]
                left+=1
                    
            hash_map[fruits[right]]+=1
            max_len = max(max_len,right-left+1)
            
        return max_len
            
                
