K = int(input())
stack = []
answer = 0

for _ in range(K):
    num = int(input())
    if num == 0:
        _ = stack.pop()
    else:
        stack.append(num)
        
answer = sum(stack)
print(answer)