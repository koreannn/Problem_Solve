from collections import deque

def solution(rows, columns, queries):
    answer = []
    num_map = []
    curr_start = 1
    
    # 오리지널 맵 만들기
    for _ in range(rows):    
        num_map.append([num for num in range(curr_start, curr_start + columns)])
        curr_start += columns
    
    # 회전시키기
    for i in range(len(queries)):
        curr_deq = deque()
        
        # 쿼리 -> 인덱스값 변환
        col_start = queries[i][1] - 1 # 열방향 시작 인덱스값
        col_end = queries[i][3] - 1 # 열방향 끝 인덱스값
        row_start = queries[i][0] - 1 # 행방향 시작 인덱스값
        row_end = queries[i][2] - 1 # 행방향 끝 인덱스값
        
        # 위쪽 열방향 원소 담기 (왼 -> 오)
        for col in range(col_start, col_end+1): # col_start ~ col_end
            curr_deq.append(num_map[row_start][col])
            
        # 오른쪽 행방향 원소 담기 (위 -> 아래)
        for row in range(row_start+1, row_end+1): # row_start+1 ~ row_end // 모서리값은 담기지 않게, +1
            curr_deq.append(num_map[row][col_end])
            
        # 아래쪽 열방향 원소 담기 (오 -> 왼)
        for col in range(col_end-1, col_start-1, -1): # col_end-1 ~ col_start // 모서리값은 담기지 않게, col_end-1
            curr_deq.append(num_map[row_end][col])
        
        # 왼쪽 행방향 원소 담기 (아래 -> 위)
        for row in range(row_end-1, row_start, -1): # row_end-1 ~ row_start-1 // 모서리값은 담기지 않게, row_end-1
            curr_deq.append(num_map[row][col_start])
        
        
        curr_deq.rotate(1) # 시계방향 한칸 회전
        answer.append(min(curr_deq)) # 회전 후 최소값 담기
        
        idx = 0 # 덱 탐색을 위한 인덱스
        # 회전 후의 값 num_map에 다시 넣어주기(왼 -> 오)
        for col in range(col_start, col_end+1): # col_start ~ col_end
            num_map[row_start][col] = curr_deq[idx]
            idx += 1
            
        # (위 -> 아래)
        for row in range(row_start+1, row_end+1): # row_start+1 ~ row_end // 모서리값은 담기지 않게, +1
            num_map[row][col_end] = curr_deq[idx]
            idx += 1
            
        # (오 -> 왼)
        for col in range(col_end-1, col_start-1, -1): # col_end-1 ~ col_start // 모서리값은 담기지 않게, col_end-1
            num_map[row_end][col] = curr_deq[idx]
            idx += 1
        
        # (아래 -> 위)
        for row in range(row_end-1, row_start, -1): # row_end-1 ~ row_start-1 // 모서리값은 담기지 않게, row_end-1
            num_map[row][col_start] = curr_deq[idx]
            idx += 1
        
    return answer

# test
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]])) # [1]