from collections import deque

n = int(input())
queue = deque()
answer = []

for _ in range(n):
    command = input().split()
    if command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "push_front":
        queue.appendleft(command[1])
        
    elif command[0] == "pop_front":
        if len(queue) == 0:
            answer.append("-1")
        else:
            answer.append(queue.popleft())
            
    elif command[0] == "pop_back":
        if len(queue) == 0:
            answer.append("-1")
        else:
            answer.append(queue.pop())
            
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
        else:
            answer.append(str(queue[0]))
            
    elif command[0] =="back":
        if len(queue) == 0:
            answer.append("-1")
        else:
            answer.append(str(queue[-1]))

print("\n".join(answer))