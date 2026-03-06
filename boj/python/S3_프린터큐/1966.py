from collections import deque

T = int(input())
answer = []

for _ in range(T):
    N, M = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄되는지 궁금한 문서의 현재 위치
    importances = list(map(int, input().split())) # 문서의 중요도
    q = deque((importance, idx) for idx, importance in enumerate(importances)) # (중요도, 위치)의 쌍
    curr_count = 1
    
    while True:
        curr_importance, origin_position = q[0]
        if (origin_position == M) and curr_importance >= max(x[0] for x in q):
            answer.append(str(curr_count))
            break
        
        if curr_importance < max(x[0] for x in q): # (자신 포함) 더 중요한 문서가 있을 경우
            q.rotate(-1)
            curr_count += 1
        else: 
            q.popleft()

print('\n'.join(answer))