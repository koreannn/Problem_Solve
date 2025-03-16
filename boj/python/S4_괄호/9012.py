import sys

input = sys.stdin.readline
T = int(input())
answer = []

for _ in range(T):
    ps = input().strip()
    stack = []
    is_valid = True
    
    for char in ps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_valid = False
                break
    
    if is_valid and not stack:
        answer.append("YES")
    else:
        answer.append("NO")

print('\n'.join(answer))