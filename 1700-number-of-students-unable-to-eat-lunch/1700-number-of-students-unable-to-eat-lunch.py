class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if Counter(students) == Counter(sandwiches):
             return 0
        student= Counter(students)
        sandwich= Counter(sandwiches)
    
        queue = deque(students)
        while queue:
            x = queue.popleft()
            if student[sandwiches[0]] == 0:
                return len(queue)+1
            if x != sandwiches[0]:
                queue.append(x)

            else:
                sandwiches.pop(0)
                student[x] -= 1
                sandwich[x] -= 1