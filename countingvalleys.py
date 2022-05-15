def countingValleys(steps, path):
    # Write your code here
    vc = level = 0
    dic = {"U":1,"D":-1}
    for step in path:
        level+=dic[step]
        if level == 0 and step =='U':
            vc+=1
    return vc
