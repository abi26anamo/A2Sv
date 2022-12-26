import textwrap

def wrap(string, max_width):
    s = ''
    while len(string)> max_width:
        s += string[:max_width]
        s += '\n'
        string = string[max_width:]
    s += string
    return s
    


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
