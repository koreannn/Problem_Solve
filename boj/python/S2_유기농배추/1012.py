"""
지렁이가 있는 배추 -> 인접한 배추까지 안전 -> 인접한 배추의 인접한 배추까지 싹 다 안전

구하는것: 필요한 최소 지렁이 수
"""
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, position):
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        
        if (next_x, next_y) in position:
            position.remove((next_x, next_y))
            dfs(next_x, next_y, position)
    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    position = set() # 배추가 위치한 좌표
    
    for _ in range(K):
        x, y = map(int, input().split())
        position.add((x, y))
    
    answer = 0
    while position:
        curr = next(iter(position))
        position.remove(curr)
        dfs(curr[0], curr[1], position)
        answer += 1

    print(answer)
