N = int(input())
stack = []
answer = []

for _ in range(N):
    command = input().split()
    
    if command[0] == '1': # 값을 넣는 연산일 경우
        stack.append(command[-1])
        
    elif command[0] == '2':
        if len(stack):
            poped = stack.pop()
            answer.append(str(poped))
        else:
            answer.append('-1')
            
    elif command[0] == '3':
        answer.append(str(len(stack)))
        
    elif command[0] == '4':
        answer.append('1') if len(stack) == 0 else answer.append('0')
        
    else: # '5'연산
        answer.append(str(stack[-1])) if len(stack) > 0 else answer.append('-1')
            
        
print('\n'.join(answer))