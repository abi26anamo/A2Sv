from collections import defaultdict


number_test_cases = int(input())

for _ in range(number_test_cases):
    len_array = int(input())
    number_array =  input().split()
    string_array = input()

    frequency = defaultdict(list)
    
    
    for index in range(len_array):
        frequency[number_array[index]].append(string_array[index])

    ispossible = True
    for key in frequency:
        if len(set(frequency[key]))!=1:
            ispossible = False
            
    if ispossible:
        print("YES")
    else:
        print("NO")
