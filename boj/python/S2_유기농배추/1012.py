from collections import deque

T = int(input())
answer_list = []

dx = [0, 0, -1, 1] # 좌, 우 이동방향
dy = [1, -1, 0, 0] # 상, 하 이동방향

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 수
    field = [[0]*M for _ in range(N)] # 초기 배추밭
    visited = [[False]*M for _ in range(N)] # 방문한곳 표기용

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1 # 배추 위치
        
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if (0 <= nx < M) and (0<= ny < N):
                    