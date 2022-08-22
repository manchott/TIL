T = int(input())
for tc in range(1, T + 1):
    s = input()
    stack = []
    result = []
    isp = {'*' : 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*' : 2, '/': 2, '+': 1, '-': 1, '(': 3}
    top = -1
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[top] != '(':
                result.append(stack.pop())
                top -= 1
            stack.pop()
        elif i in isp.values():
            if 
