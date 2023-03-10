class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = Counter()
        max_vote = 0
        self.lead =[]
        for i,c in enumerate(times):
            count[persons[i]] +=1
            if count[persons[i]] >=max_vote:
                max_vote = count[persons[i]]
                self.lead.append([c,persons[i]])
                
        

    def q(self, t: int) -> int:
        l=0
        r =len(self.lead)-1
        while l <=r:
            mid = (l+r)//2
            if self.lead[mid][0]<=t:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return self.lead[res][1]
