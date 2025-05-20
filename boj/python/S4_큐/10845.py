from collections import deque

queue = deque()
N = int(input()) # 1<= N <= 10,000
answer = []

for i in range(N):
    command = input().split() # command, data
    
    if command[0] == "push":
        queue.append(command[-1])
    
    elif command[0] == "pop":
        if len(queue) == 0:
            answer.append("-1")
            continue
        poped_front = queue.popleft()
        answer.append(poped_front)
    
    elif command[0] == "size":
        answer.append(str(len(queue)))
    
    elif command[0] == "empty":
        if len(queue) == 0:
            answer.append("1")
        else:
            answer.append("0")
    
    elif command[0] == "front":
        if len(queue) == 0:
            answer.append("-1")
            continue
        answer.append(queue[0])
    
    else:
        if len(queue) == 0:
            answer.append("-1")
            continue
        answer.append(queue[-1])
        
print('\n'.join(answer))
