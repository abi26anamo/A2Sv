
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box:box[1],reverse=True)
        units =0
        for i,j in boxTypes:
            if i <= truckSize and truckSize > 0:
                units += i * j
                truckSize -=i
            else:
                units += truckSize * j
                truckSize -= truckSize
        return units