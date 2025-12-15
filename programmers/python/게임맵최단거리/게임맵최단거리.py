from collections import deque

def solution(maps):
    row_length, col_length = len(maps), len(maps[0]) # 행 길이, 열 길이
    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]
    q = deque([(0, 0, 1)])
    visited = [[False] * col_length for _ in range(row_length)]
    
    while q:
        curr_row, curr_col, curr_distance = q.popleft()
        if (curr_row == row_length - 1) and (curr_col == col_length - 1):
            return curr_distance
        
        for i in range(4):
            next_row, next_col = curr_row + dr[i], curr_col + dc[i]
            
            if (maps[next_row][next_col] == 1) and (0 <= next_row < row_length) and (0 <= next_col < col_length):
                if not visited[curr_row][curr_col]:
                    visited[curr_row][curr_col] = True
                    q.append(next_row, next_col, curr_distance + 1)
    
    return -1

# test
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1
