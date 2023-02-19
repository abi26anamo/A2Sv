from collections import  defaultdict
t = int(input())

for _ in range(t):
    row, col = (int(i) for i in input().split())
    matrix = []
    for _ in range(row):
        matrix.append([int(i) for i in input().split()])
    
    top_right_bottom_left = defaultdict(int)
    top_left_bottom_right = defaultdict(int)
    
    for r in range(row):
        for c in range(col):
            top_right_bottom_left[r+c] += matrix[r][c]
            top_left_bottom_right[r-c] += matrix[r][c]
            
    maximal_attack = 0
    for r in range(row):
        for c in range(col):
            curr_attack = top_right_bottom_left[r+c] + top_left_bottom_right[r-c] - matrix[r][c]
            maximal_attack = max(maximal_attack, curr_attack)
    
    print(maximal_attack)
        
