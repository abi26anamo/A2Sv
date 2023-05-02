class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        slots = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        queue = deque()
        visited = set("0000")
        queue.append(("0000", 0))
        while queue:
            wheels, moves = queue.popleft()
            if wheels == target:
                return moves
            for i in range(4):
                right_rotation = wheels[:i] + slots[(int(wheels[i]) + 1) % 10] + wheels[i + 1:]
                if right_rotation not in visited and right_rotation not in deadends:
                    queue.append((right_rotation, moves + 1))
                    visited.add(right_rotation)

                left = int(wheels[i]) - 1
                if left == -1:
                    left = 9
                left_rotation = wheels[:i] + slots[left] + wheels[i + 1:]
                if left_rotation not in visited and left_rotation not in deadends:
                    queue.append((left_rotation, moves + 1))
                    visited.add(left_rotation)
        return -1    
