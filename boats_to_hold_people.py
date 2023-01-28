class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        right = len(people)-1
        left = 0
        while left<=right:
            if people[right]+people[left]<=limit:
                boats+=1
                left+=1
                right-=1
            else:
                boats+=1
                right-=1
        return boats
