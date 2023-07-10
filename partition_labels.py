class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        for idx,val in enumerate(s):
            hash_map[val] = idx
        ans = []
        left = 0
        right = 0
        for idx,val in enumerate(s):
            right = max(right,hash_map[val])

            if right == idx:
                ans.append(right-left+1)
                left = right+1
        return ans

        
