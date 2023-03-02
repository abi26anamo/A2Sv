class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_map = defaultdict(lambda:-1)
        montonic_stack = []
        for i in range(2*n):
            i = i%n
            while montonic_stack and montonic_stack[-1][0]<nums[i]:
                _,idx = montonic_stack.pop()
                hash_map[idx]=nums[i]
                
            montonic_stack.append((nums[i],i))
            
        return [hash_map[i] for i in range(n)]
