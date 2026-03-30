from collections import deque

N, M = map(int, input().split()) # 행 크기, 열 크기
maps = []
visited = [[False] * M for _ in range(N)]
move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
answer = 0

for _ in range(N):
    row = list(input())
    maps.append(row)

def graph_search(curr_row, curr_col):
    q = deque()
    depth = 1
    q.append((curr_row, curr_col, depth))
    visited[curr_row][curr_col] = True
    
    while q:
        curr_row, curr_col, curr_depth = q.popleft()
        
        if curr_row == N-1 and curr_col == M-1:
            return curr_depth
        
        
        for dc, dr in move:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if 0 <= next_row < N and 0<= next_col < M and maps[next_row][next_col] == '1':
                if not visited[next_row][next_col]:
                    q.append((next_row, next_col, curr_depth + 1))
                    visited[next_row][next_col] = True

answer = graph_search(0, 0)
print(answer)