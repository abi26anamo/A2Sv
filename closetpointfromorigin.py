import random
class Solution:
    def find(self,lst,k):
        if len(lst)== k:
            return [i[0] for i in list]
        random_tuple = random.choice(lst)
        pivot = random_tuple[1]
        i=0
        left = []
        right =[]
        equal =[]
        
        while i < len(lst):
            curr = lst[i]
            distance = curr[1]
            if distance < pivot:
                left.append(curr)
            elif distance == pivot:
                equal.append(curr)
            else:
                right.append(curr)
            i+=1
        len_left = len(left)
        if len_left == k:
            return [(i[0] for i in left)]
        if len_left + len(equal) == k:
            return [i[0] for i in left ] + [i[0] for i in equal]
        if k < len_left:
            return self.find(left,k)
        else :
            return [i[0] for i in left] + [i[0] for i in equal] + self.find(right ,k-len_left - len(equal))
    def distance(self,pt):
        return pt[0]**2 + pt[1]**2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = [(i,self.distance(i)) for i in points]
        return self.find(lst,k)
