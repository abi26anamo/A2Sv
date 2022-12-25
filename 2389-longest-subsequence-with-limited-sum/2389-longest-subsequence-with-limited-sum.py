class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for q in queries:
            sub_sum =0
            sub_length =0
            for num in nums:
                if num + sub_sum <=q:
                    sub_sum+=num
                    sub_length+=1
                else:
                    break
            answer.append(sub_length)
        return answer
        