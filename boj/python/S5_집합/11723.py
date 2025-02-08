S = set()

M = int(input()) # 수행해야하는 연산의 수
answer = []

for _ in range(M):
    command = input().stript().split()
    if command[0] == 'add':
        S.add(command[1])
        
    elif command[0] == 'remove':
        S.discard(command[1]) # remove 말고 discard() 사용 -> KeyError 방지
    
    elif command[0] == 'check':
        answer.append(1 if command[1] in S else 0)
    
    elif command[0] == 'toggle':
        if  command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    
    elif command[0] == 'all':
        # S = set(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        S = set(range(1,21))
    
    elif command[0] == 'empty':
        S.clear()

for ans in answer:
    print(ans)
