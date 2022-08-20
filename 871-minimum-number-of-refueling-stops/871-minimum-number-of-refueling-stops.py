class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        que = []
        res, i, cur = 0, 0, startFuel
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heappush(que, -stations[i][1])
                i += 1
            if not que: return -1
            cur += -heappop(que)
            res += 1
        return res
        