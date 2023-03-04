class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [1 if nums[i]%2!=0 else 0 for i in range(n)]

        prefix_sum = 0
        hash_map = {0:1}
        count = 0
        print(arr)
 
        for right in range(n):
            prefix_sum+=arr[right]

            if prefix_sum-k in hash_map:
                count+= hash_map[prefix_sum-k]
                if prefix_sum in hash_map:
                      hash_map[prefix_sum]+=1
                else:
                    hash_map[prefix_sum]=1
 
            elif prefix_sum in hash_map:
                hash_map[prefix_sum]+=1
            else:
                hash_map[prefix_sum]=1
        return count
