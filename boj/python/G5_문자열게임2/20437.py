from collections import defaultdict

T = int(input())

for _ in range(T):
    W = input() # 각 테스트 케이스의 문자열
    K = int(input()) # 포함되어야하는 문자의 개수
    curr_answer = -1
    
    pos = defaultdict(list)
    for i, c in enumerate(W):
        pos[c].append(i)
    
    min_len = float('inf')
    max_len = float('-inf')
    
    for c, pos in pos.itmes():
        if len(pos) < K:
            continue
        
        for i in range(len(pos) - K + 1):
            length = pos[i + K - 1] - pos[i] + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)
        
    if max_len == float('-inf'):
        