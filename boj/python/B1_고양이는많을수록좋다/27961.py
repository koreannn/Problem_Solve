curr = 0 # 현재 가지고있는 고양이 마리수
answer = 0 # 행동 횟수

N = int(input()) # 목표 고양이 마리수 (갱신되는값으로 사용)

while(N != 0): # N값이 0이될때까지 반복
    if N == 0:
        answer += 1
        break
    # elif N == 1: 
    #     answer += 1
    #     break
    else: # N >= 2일 경우
        if curr == 0:
            curr+=1
            answer+=1
            N = N-1
            continue
            
        min_val = float('inf')
        for i in range(0, curr+1): # 0이상 curr이하
            if abs(N-i) < min_val:
                min_val = abs(N-i) # 최적의 값 찾기 위한 값
                add_val = i # 실제로 더해지는 고양이의 마리수
        N = N-add_val
        curr += add_val
        answer+=1

print(answer) # 최소한의 행동 횟수