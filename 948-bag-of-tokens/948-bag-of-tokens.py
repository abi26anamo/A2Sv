class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        queue =deque(sorted(tokens))
        score =0
        max_score =0
        while queue:
            if power >=queue[0]:
                token = queue.popleft()
                power-=token
                score+=1
                max_score = max(score,max_score)
            elif score >0:
                token = queue.pop()
                power+=token
                score-=1
            else:
                break
        return max_score
            