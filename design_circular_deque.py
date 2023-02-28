class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size =k
        self.queue = [None]*self.max_size
        self.head =0
        self.tail =0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.head = (self.head -1)%self.max_size
            self.queue[self.head] = value
            self.count += 1
            return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.count += 1
            return True
        
        

    def deleteFront(self) -> bool:
          if self.isEmpty():
            return False
          else:
            self.count -= 1
            self.head = (self.head + 1) % self.max_size
            return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail - 1) % self.max_size
            self.count -= 1
            return True
        

    def getFront(self) -> int:
         if self.isEmpty():
            return -1
         else:
            return self.queue[self.head]
        

    def getRear(self) -> int:
         if self.isEmpty():
            return -1
         else:
            return self.queue[self.tail - 1]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.max_size
        
