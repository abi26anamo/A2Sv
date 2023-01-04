from collections import Counter

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    number_of_planet,cost_of_second_machine = input().split()
    oribits = input().split()

    min_cost = 0
    same_oribit_planets = Counter(oribits)

    for planet in same_oribit_planets:
        if same_oribit_planets[planet]>1:
            if same_oribit_planets[planet]>=int(cost_of_second_machine):
                 min_cost+=int(cost_of_second_machine)
            else:
                min_cost+=int(same_oribit_planets[planet])
        else:
            min_cost+=1
    print(min_cost)
