class RandomizedSet:

    def __init__(self):
        self.randomized = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.randomized.keys():
            self.randomized[val] =val
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.randomized.keys():
            del self.randomized[val]
            return True
        return False

    def getRandom(self) -> int:
        n =len(self.randomized)
        idx = random.randint(0,n-1)
        return list(self.randomized.keys())[idx]
