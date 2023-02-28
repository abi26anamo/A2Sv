class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [(target-position[i])/speed[i] for i in range(n)]
        cars = [(x,y) for x,y in zip(position,time)]
        cars.sort()
        stack =[]
        for car in cars:
            while stack and stack[-1][1]<=car[1]:
                stack.pop()
            stack.append(car)
        return len(stack)
        
