from collections import deque

N, K = map(int, input().split()) # 수빈의 위치, 동생의 위치
answer = 0 # 찾는데 걸리는 시간

# 동생 찾기
MAX = 100000
visited = [-1]*(MAX+1) # 방문 체크 (시간으로 기록) (-1 : 방문하지 않은 위치)

queue = deque([N])
visited[N] = 0 # 시작점 방문 시간 : 0초

while queue:
    curr = queue.popleft()

    if curr == K:
        answer = visited[curr]
    
    for next_pos in (curr-1, curr+1, curr*2):
        if (next_pos>=0 and next_pos<=MAX) and visited[next_pos] == -1:
            visited[next_pos] = visited[curr]+1
            queue.append(next_pos)
            
print(answer)