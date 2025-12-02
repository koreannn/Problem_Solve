"""
- 미로는 0과 1로 이루어져있으며, 각각 이동할 수 없는 벽, 이동 가능한 길을 의미한다.
- 출발지점과 도착지점은 각각 2, 4로 나타낸다. 
- 최단 거리를 통해 이동한 경로는 3으로 나타내야한다 (즉 해당 경로가 최단 경로라면 1 -> 3으로 변경해야한다).
- 상하좌우 이동만 가능하며, 최단 경로가 없을 수도 있다.

[입력 예시]
2 0 1 1 1
1 0 1 0 1
1 1 1 0 1
0 0 1 1 1
1 1 1 0 4

[출력 예시]
2 0 1 1 1
3 0 1 0 1
3 3 3 0 1
0 0 3 3 3
1 1 1 0 4

최단 거리 이동 : 8 회
"""
from collections import deque

N, M = map(int, input().split()) # 가로 길이, 세로 길이
map_ = [input().split() for _ in range(M)]

distance = [[-1] * N for _ in range(M)]
prev =  [[None] * N for _ in range(M)]
movement = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동

# 도착 지점 인덱스 찾기
def bfs(start_x, start_y):
    count = 0
    q = deque()
    q.append(start_x, start_y)
    distance[start_x][start_y] = 0 # 시작점까지의 거리
    
    while q:
        curr_x, curr_y = q.popleft()
        
        if map_[curr_x][curr_y] == '4': # 도착 지점일 경우
            end_point = (curr_x, curr_y) 
            break
        
        for dx, dy in movement: # 현재 위치에서 상하좌우 각각 움직여보기
            next_x, next_y = curr_x + dx, curr_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:
                # 벽이 아니고, 방문하지 않았을 때만
                if map_[next_x][next_y] in ('1', '4') and distance[next_x][next_y] == -1:
                    distance[next_x][next_y] = distance[curr_x][curr_y] + 1
                    prev[next_x][next_y] = (curr_x, curr_y)
                    
                    q.append((next_x, next_y))
    return end_point
